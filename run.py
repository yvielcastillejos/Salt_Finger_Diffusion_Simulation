import exadata
import extract_data2D
import neksuite
import numpy as np
import matplotlib.pyplot as plt
import os

kappa_o = 0.0125
Nus = []
times = []
turbratio = []
for i in range(1,4,1):
    #PATH = '/Volumes/LaCie/Nek5000/dddd'
    PATH = f"/home/casti136/scratch/Osc_Oxy/output_part{i}"
    files = sorted(os.listdir(PATH))
    # print(files)
    #fifle= "/home/casti136/scratch/try/output_part6/dd0.f00001"
   # Nus = []
   # times = []
   # turbratio = []
    files1 = []
    for file in files:
       if file[0:3]=='dd0':
            files1.append(file)
       else:
            continue
    for file in files1:
        data = neksuite.readnek(f"{PATH}/{file}")
        lr1 = data.lr1
        Uy = extract_data2D.reshapenek(data.elems.vel[1],lr1)
     #   temp =  extract_data2D.reshapenek(data.elems.temp[0],lr1) 
     #   saln = extract_data2D.reshapenek(data.elems.scal[0],lr1)
        oxyg = extract_data2D.reshapenek(data.elems.scal2[0],lr1)
        time = data.time
        dO_dz = np.gradient(oxyg, axis = 0 ) 
        
        horz = k_o*np.mean(dO_dz, axis=1) 
        diff  =np.mean(horz) 
     #   Nu = 1 - FT
        #turbratio.append(F_T/F_S)
        Nus.append(Nu)
        times.append(time)
        print(f"{file}" + " done")
        #print(times)
        #print(Nus)

    # x,y coordinates
    #data = neksuite.readnek(fifle)
    #lr1 = data.lr1
    #temp =extract_data2D.reshapenek(data.elems.scal2[0],lr1)
    #print((temp.shape))
    #time = data.time 
    # U = np.sqrt(np.square(Ux) + np.square(Uy))
    x = np.linspace(0, 300, 896)
    y = np.linspace(0, 500, 896)


    # calculate mean
    tempmean = np.mean(temp,axis =1)

    # plot

    #fig, ax = plt.subplots()
    #
    #cmap = ax.pcolormesh(x, y, temp)
    #ax.set_aspect("equal")
    #fig.colorbar(cmap)
    #plt.title(f"Temp-end-osc-{time}")
    #plt.show()
    #
    #plt.savefig('books_read.png')


fig2, ax = plt.subplots()
plt.plot(times,Nus)

    #plt.title(f't ={time} (Nu = {Nu})')
plt.title('Diff_O')

    #plt.title(f"Temp-end-osc-{")
plt.ylabel('Flux')
plt.xlabel('time')

plt.savefig(f"Diff_Flux")
    #ax.set_aspect("equal")
    #plt.show()

