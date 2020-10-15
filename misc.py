    PATH13 = "/Users/yvielcastillejos/Desktop/Osc_Oxy/Rp = 1.05/output/13"
    PATH14 = "/Users/yvielcastillejos/Desktop/Osc_Oxy/Rp = 1.05/output/14"
    PATH15 = "/Users/yvielcastillejos/Desktop/Osc_Oxy/Rp = 1.05/output/15"
    PATH16 = "/Users/yvielcastillejos/Desktop/Osc_Oxy/Rp = 1.05/output/16"
    PATH17 = "/Users/yvielcastillejos/Desktop/Osc_Oxy/Rp = 1.05/output/17"
    PATH18 = "/Users/yvielcastillejos/Desktop/Osc_Oxy/Rp = 1.05/output/18"


      # 7
    data7 = neksuite.readnek(f"{PATH7}")
    lr7 = data7.lr1
    Uy7 = extract_data2D.reshapenek(data7.elems.vel[1],lr7)
    temp7 =  extract_data2D.reshapenek(data7.elems.temp[0],lr7) 
    saln7 = extract_data2D.reshapenek(data7.elems.scal[0],lr7)
    oxyg7 = extract_data2D.reshapenek(data7.elems.scal2[0],lr7)
    time7 = data7.time
    
    # 8
    data8 = neksuite.readnek(f"{PATH8}")
    lr8 = data8.lr1
    Uy8 = extract_data2D.reshapenek(data8.elems.vel[1],lr8)
    temp8 =  extract_data2D.reshapenek(data8.elems.temp[0],lr8) 
    saln8 = extract_data2D.reshapenek(data8.elems.scal[0],lr8)
    oxyg8 = extract_data2D.reshapenek(data8.elems.scal2[0],lr8)
    time8 = data8.time 

      # 9
    data9 = neksuite.readnek(f"{PATH9}")
    lr9 = data9.lr1
    Uy9 = extract_data2D.reshapenek(data9.elems.vel[1],lr9)
    temp9 =  extract_data2D.reshapenek(data9.elems.temp[0],lr9) 
    saln9 = extract_data2D.reshapenek(data9.elems.scal[0],lr9)
    oxyg9 = extract_data2D.reshapenek(data9.elems.scal2[0],lr9)
    time9 = data9.time 
   
      # 10
    data10 = neksuite.readnek(f"{PATH10}")
    lr10 = data10.lr1
    Uy10 = extract_data2D.reshapenek(data10.elems.vel[1],lr10)
    temp10 =  extract_data2D.reshapenek(data10.elems.temp[0],lr10) 
    saln10 = extract_data2D.reshapenek(data10.elems.scal[0],lr10)
    oxyg10 = extract_data2D.reshapenek(data10.elems.scal2[0],lr10)
    time10 = data10.time
     
   
    # 12
    data12 = neksuite.readnek(f"{PATH12}")
    lr12 = data12.lr1
    Uy12 = extract_data2D.reshapenek(data12.elems.vel[1],lr12)
    temp12 =  extract_data2D.reshapenek(data12.elems.temp[0],lr12) 
    #saln12 = extract_data2D.reshapenek(data12.elems.scal[0],lr12)
    oxyg12 = extract_data2D.reshapenek(data12.elems.scal2[0],lr12)
    time12 = data12.time

    # 13
    data13 = neksuite.readnek(f"{PATH13}")
    lr13 = data13.lr1
    Uy13 = extract_data2D.reshapenek(data13.elems.vel[1],lr13)
    temp13 =  extract_data2D.reshapenek(data13.elems.temp[0],lr13) 
    #saln13 = extract_data2D.reshapenek(data13.elems.scal[0],lr13)
    oxyg13 = extract_data2D.reshapenek(data13.elems.scal2[0],lr13)
    time13 = data13.time

        # 14
    data14 = neksuite.readnek(f"{PATH14}")
    lr14 = data14.lr1
    Uy14 = extract_data2D.reshapenek(data14.elems.vel[1],lr14)
    temp14 =  extract_data2D.reshapenek(data14.elems.temp[0],lr14) 
    #saln14 = extract_data2D.reshapenek(data14.elems.scal[0],lr14)
    oxyg14 = extract_data2D.reshapenek(data14.elems.scal2[0],lr14)
    time14 = data14.time

        # 15
    data15 = neksuite.readnek(f"{PATH15}")
    lr15 = data15.lr1
    Uy15 = extract_data2D.reshapenek(data15.elems.vel[1],lr15)
    temp15 =  extract_data2D.reshapenek(data15.elems.temp[0],lr15) 
    #saln15 = extract_data2D.reshapenek(data15.elems.scal[0],lr15)
    oxyg15 = extract_data2D.reshapenek(data15.elems.scal2[0],lr15)
    time15 = data15.time

        # 16
    data16 = neksuite.readnek(f"{PATH16}")
    lr16 = data16.lr1
    Uy16 = extract_data2D.reshapenek(data16.elems.vel[1],lr16)
    temp16 =  extract_data2D.reshapenek(data16.elems.temp[0],lr16) 
    #saln16 = extract_data2D.reshapenek(data16.elems.scal[0],lr16)
    oxyg16 = extract_data2D.reshapenek(data16.elems.scal2[0],lr16)
    time16 = data16.time

        # 17
    data17 = neksuite.readnek(f"{PATH1}")
    lr17 = data17.lr1
    Uy17 = extract_data2D.reshapenek(data17.elems.vel[1],lr17)
    temp17 =  extract_data2D.reshapenek(data17.elems.temp[0],lr17) 
    #saln17 = extract_data2D.reshapenek(data17.elems.scal[0],lr17)
    oxyg17 = extract_data2D.reshapenek(data17.elems.scal2[0],lr17)
    time17 = data17.time

        # 18
    data18 = neksuite.readnek(f"{PATH18}")
    lr18 = data18.lr1
    Uy18 = extract_data2D.reshapenek(data18.elems.vel[1],lr18)
    temp18 =  extract_data2D.reshapenek(data18.elems.temp[0],lr18) 
    #saln18= extract_data2D.reshapenek(data18.elems.scal[0],lr18)
    oxyg18 = extract_data2D.reshapenek(data18.elems.scal2[0],lr18)
    time18 = data18.time










    tempmean12 = np.mean(temp12,axis =1)
    oxygmean12 = np.mean(oxyg12,axis =1)

    tempmean13 = np.mean(temp13,axis =1)
    oxygmean13 = np.mean(oxyg13,axis =1)

    tempmean14 = np.mean(temp14,axis =1)
    oxygmean14 = np.mean(oxyg14,axis =1)

    tempmean15 = np.mean(temp15,axis =1)
    oxygmean15 = np.mean(oxyg15,axis =1)

    tempmean16 = np.mean(temp16,axis =1)
    oxygmean16 = np.mean(oxyg16,axis =1)

    tempmean17 = np.mean(temp17,axis =1)
    oxygmean17 = np.mean(oxyg17,axis =1)

    tempmean18 = np.mean(temp18,axis =1)
    oxygmean18 = np.mean(oxyg18,axis =1)





    fig2, ax = plt.subplots()
    plt.plot(oxygmean1,y, c ="b", label= "t=7")
    plt.plot(oxygmean2,y, c ="g", label="t=70" )
    plt.plot(oxygmean3,y, c ="r", label= "t=100")
    plt.plot(oxygmean4,y, c ="c", label= "t=150")
    plt.plot(oxygmean5,y, c ="m", label= "t=250")
    plt.plot(oxygmean6,y, "--", label= "t=700")
   # plt.plot(oxygmean7,y, c ="k", label= "t=800")
   # plt.plot(oxygmean8,y, c ="y", label= "t=1000")
    #plt.plot(oxygmean9,y,"--", c = "g", label= "t=70000")
    plt.legend(loc="upper left")
    plt.title('Mean Oxygen Values at Rp = 2.0')
    plt.ylabel('Depth')
    plt.xlabel('Oxygen Value')
    plt.show()



    plt.plot(oxygmean12,y)
    plt.plot(oxygmean13,y)
    plt.plot(oxygmean14,y)
    plt.plot(oxygmean15,y)
    plt.plot(oxygmean16,y)
    plt.plot(oxygmean17,y)
    plt.plot(oxygmean18,y)