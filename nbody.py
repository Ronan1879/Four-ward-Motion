import numpy as np
import time
import matpltlib.pyplot as plt


class bods:
    def __init__(self,m=1.0,npar=5,thres=0.01,G=1.0,dt=0.1,num_enc=np.zeros(self.pars['npars'])):
        self.pars={}
        self.pars['npar']=npar
        self.pars['thresh']=thresh
        self.pars['G']=G
        self.pars['dt']=dt
        self.num_enc=np.zeros(self.pars['npars'])
        
        self.x=np.random.rand(self.pars['npar'])
        self.y=np.random.rand(self.pars['npar'])
        self.m=np.random.randn(self.pars['npars'])*m
        self.vx=0*self.x
        self.vy=0*self.x
        self.clos_enc=np.zeros(self.pars['npars'])
        
    def get_forces(self):
        self.for_x=np.zeros(self.pars['npar'])
        self.for_y=np.zeros(self.pars['npar'])
        for i in range(self.pars['npar']):
            dx=self.x[i]-self.x
            dy=self.y[i]-self.y
            r_sq=dx**2+dy**2
            thresh=self.pars['thresh']**2
            
            
            if not(np.all(r_sq > thresh)): #if we have to care about things being close
                #array with a 1 at each index/particle currently closer than threshold
                close_ps = ((r_sq<thresh) + np.zeros(len(r_sq)))
                if num_enc == np.zeros(len(self.pars['npar'])): #if this is the first time we have to worry about particles being close...
                    num_enc = indicies #then simply updatae the close log
                elif num_enc != indicies: #if the particles we knew were close in the previous timestep aren't the same as the ones that are now
                    delta_close = num_enc - indicies #if particle status is same (close or far), then there will be a zero at its index
                                                     #if a particle has recently become close, then there will be a -1 at it's index
                                                     #if a particle just left the vicinity, then 1-0 = 1 at it's index
                    n_close_encounter = np.sum(delta_close>0)
            else:
                indicies = ((r_sq<thresh) + np.zeros(len(r_sq)))
                if self.num_enc[i]==1:
                    self.clos_enc[i]+=1
                    self.num_enc[i]=0
                    
            r_sq=r_sq+self.pars['thresh']**2
            r=numpy.sqrt(rsqr)
            r3=1.0/(r*rsqr)
            self.fx[i]=-numpy.sum(self.m*dx*r3)*self.pars['G']
            self.fy[i]=-numpy.sum(self.m*dy*r3)*self.pars['G']
            pot+=self.pars['G']*numpy.sum(self.m/r)*self.m[i]
            return -0.5*pot, self.num_enc
        
        
        def evolve(self):
            self.x+=self.vx*self.pars['dt']
            self.y+=self.vy*self.pars['dt']
            pot, num_enc=self.get_forces()
            self.vx+=self.fx*self.pars['dt']
            self.vy+=self.fy*self.pars['dt']
            kinetic=0.5*numpy.sum(self.m*(self.vx**2+self.vy**2))
            return pot+kinetic, num_enc
        
if __name__=='__main__':
    plt.ion()
    n=5
    oversamp=5
    part=particles(m=1.0/n,npart=n,dt=0.1/oversamp)
    plt.plot(part.x,part.y,'*')
    plt.show()
    


    #fig = plt.figure()
    #ax = fig.add_subplot(111, autoscale_on=False, xlim=(-5, 5), ylim=(-5, 5))
    #line, = ax.plot([], [], '*', lw=2)

    for i in range(0,10000):
        for ii in range(oversamp):
            energy, num_enc=part.evolve()
            part=particles(m=1.0/n,npart=n,dt=0.1/oversamp, num_enc)
        print(energy)
        plt.clf()
        plt.plot(part.x,part.y,'*')
        plt.pause(1e-3)
