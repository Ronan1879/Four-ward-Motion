import numpy as np
import stddraw
import universe as u
import matplotlib.pyplot as plt
dt=20000

def scale_1000(x):
    x = x - np.min(x)
    x = x/(np.max(x))
    x = x*100
    x = np.round(x)
    return x.astype(int)

def get_theta(o, v):
    m_o = np.sqrt(o @ o)
    m_v = np.sqrt(v @ v)

    print("o @ v: ", (o @ v))
    print("m_o * m_v: ", (m_v * m_o))

    theta = np.arccos((o @ v)/(m_o * m_v))

    return theta

def get_velocity(x, y):
    d_origin = np.array([-x, -y])
    theta = np.pi/2 + 1

    print("")

    while np.abs(theta) >= np.pi/2:
        d_v = np.random.randn(2)
        theta = get_theta(d_origin, d_v)

    return d_v

def rotate(vels):
    max_fac = 6
    min_fac = 15
    theta = np.pi/max_fac*np.random.randn()
    while theta < np.pi/min_fac:
        theta = np.pi/max_fac*np.random.randn()
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c,-s],[s,c]])

    rot_vels = np.array([vec @ R for vec in vels])
    return rot_vels

# pos_x = -3.5e10
# pos_y = 0.0e00
# vel_x = 7.0e02
# vel_y = 7.0e02
# mass = 3.0e28

pos_x = 0.0e00
pos_y = 0.0e00
vel_x = 7.0e02
vel_y = 7.0e02
mass = 3.0e27

pos_scale = 3e10
v_scale =7e3
offset = 0

database = []
labels = []

#for j in range(1,4):
    #labels.append(j)


# for n in [2, 3, 4]:
for n in [4]:

    for i in range(1):
        f = open('temp_data.txt', 'w')
        radius = 1.0e11 
        f.write(' '+str(n)+' ')
        f.write(f'\n')
        f.write(' '+str(radius)+' ')
        f.write(f'\n')

        # for k in range(0,n):

        #     new_pos_x = np.random.randint(pos_x-1e2,pos_x+1e2)
        #     new_pos_y = np.random.randint(pos_y-1e2,pos_y+1e2)
        #     # new_vel_x = np.random.randint(vel_x-1e1,vel_x+1e1)
        #     # new_vel_y = np.random.randint(vel_y-1e1,vel_y+1e1)

        #     new_vel_x, new_vel_y = 1e1*get_velocity(new_pos_x, new_pos_y)
        #     print(new_pos_x, new_pos_y, new_vel_x, new_vel_y)
        #     plt.quiver(new_pos_x, new_pos_y, new_vel_x, new_vel_y, color="r")
        #     plt.quiver(new_pos_x, new_pos_y, -new_pos_x, -new_pos_y, color="b")
        #     params = [new_pos_x,new_pos_y,new_vel_x,new_vel_y,mass]
        #     for ii in range(len(params)):
        #         if params[ii] < 0.0:
        #             f.write(str(params[ii])+' ')
        #         else:
        #             f.write(' '+str(params[ii])+' ')
        #     f.write('\n')

        new_pos_x = pos_scale*np.random.randn(n)
        new_pos_y = pos_scale*np.random.randn(n)

        pos = np.concatenate((new_pos_x.reshape(len(new_pos_x),1), new_pos_y.reshape(len(new_pos_y),1)))

        #Center of Mass vector, but slightly off
        com = np.array([np.sum(new_pos_x)/(len(new_pos_x)+offset), np.sum(new_pos_y)/(len(new_pos_y) + offset)])

        pos2com = -(pos - com)
        mag_pos2com = np.array([np.sqrt(_[0]**2 + _[1]**2) for _ in pos2com])
        mag_pos2com = np.concatenate((mag_pos2com.reshape(len(mag_pos2com),1), mag_pos2com.reshape(len(mag_pos2com),1)), axis=1)
        unit_pos2com = pos2com/mag_pos2com
        
        vels = v_scale*unit_pos2com
        vels = rotate(vels)

        for k in range(n):
            params = [new_pos_x[k], new_pos_y[k], vels[k][0], vels[k][1], mass]
            for ii in range(len(params)):
                if params[ii] < 0.0:
                    f.write(str(params[ii])+' ')
                else:
                    f.write(' '+str(params[ii])+' ')
            f.write('\n')


        f.close()

        universe = u.Universe("temp_data.txt")

        for j in range(500):
            universe.increaseTime(dt)
            stddraw.clear()
            universe.draw()
            stddraw.show(10)


        x_arr = universe._xtracks
        y_arr = universe._ytracks

        #coords = zip(x_array_p[n],y_array_p)

        img_rows, img_cols = 110, 110
        #imgs = np.zeros((n, img_rows, img_cols))

        for ii in range(n):
            img = np.zeros((img_rows, img_cols))


            xvals = scale_1000(x_arr[ii])
            yvals = scale_1000(y_arr[ii])
            for xval, yval in zip(xvals, yvals):
                img[xval][yval] = 1
            # plt.imshow(img)
            # plt.show()
            database.append(img.flatten().tolist())
            #labels.append(label.flatten().tolist())
    database_file = open(str(n)+"bodies_database.txt","w")
    labels_file = open(str(n)+"bodies_labels.txt","w")
    database_file.write(str(database))
    #labels_file.write(str(labels))

