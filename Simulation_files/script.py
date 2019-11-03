import numpy as np
import stddraw
import universe as u
dt=10000

def scale_1000(x):
    x = x - np.min(x)
    x = x/(np.max(x))
    x = x*100
    x = np.round(x)
    return x.astype(int)

pos_x = -3.5e10
pos_y = 0.0e00
vel_x = 0.0e00
vel_y = 1.4e03
mass = 3.0e28

database = []
labels = []

#for j in range(1,4):
    #labels.append(j)


for n in [2, 3, 4]:


    for i in range(10):
        f = open('temp_data.txt', 'w')
        radius = 5.0e10 
        f.write(' '+str(n)+' ')
        f.write(f'\n')
        f.write(' '+str(radius)+' ')
        f.write(f'\n')

        for k in range(0,n):

            new_pos_x = np.random.randint(pos_x-1e2,pos_x+1e2)
            new_pos_y = np.random.randint(pos_y-1e2,pos_y+1e2)
            new_vel_x = np.random.randint(vel_x-1e1,vel_x+1e1)
            new_vel_y = np.random.randint(vel_y-1e1,vel_y+1e1)
            params = [new_pos_x,new_pos_y,new_vel_x,new_vel_y,mass]
            for ii in range(len(params)):
                if params[ii] < 0.0:
                    f.write(str(params[ii])+' ')
                else:
                    f.write(' '+str(params[ii])+' ')
            f.write('\n')

        f.close()

        universe = u.Universe("temp_data.txt")

        for j in range(100):
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
            database.append(img.flatten().tolist())
            #labels.append(label.flatten().tolist())
    database_file = open(str(n)+"bodies_database.txt","w")
    labels_file = open(str(n)+"bodies_labels.txt","w")
    database_file.write(str(database))
    #labels_file.write(str(labels))

