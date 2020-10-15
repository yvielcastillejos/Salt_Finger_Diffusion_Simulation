#----------------------------------------------------------------------------

# This part converts Var1 that is of shape (Nx*Ny*Nz,lz,ly,lx)

# as resulting from exadata.py to Var2 that is of shape (Nx*lx,Ny*ly,Nz*lz)

#----------------------------------------------------------------------------

import numpy as np

def reshapenek(Var1,lr1):
    Nx = 128
    Ny = 128
    Var2 = np.zeros(shape=(Nx*lr1[1],Ny*lr1[0]))
    for iy in range(Ny):
        for ix in range(Nx):
           # print(iy)
            #print(Var2[iy*lr1[0]:(iy+1)*lr1[0],ix*lr1[1]:(ix+1)*lr1[1]].shape)
            x2 = np.transpose(Var1[ix+iy*Nx,:,:][0],(0,1))
            #print(iy )
            #print(Var2[iy*lr1[0]:(iy+1)*lr1[0],ix*lr1[1]:(ix+1)*lr1[1]].shape)
            Var2[iy*lr1[0]:(iy+1)*lr1[0],ix*lr1[1]:(ix+1)*lr1[1]] = x2
    return Var2