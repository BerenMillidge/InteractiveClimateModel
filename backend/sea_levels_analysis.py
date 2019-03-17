from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import pickle

sea_levels_26 = Dataset(str("sea_level_indices_data/seaLevelAnom_marine-sim_rcp26_ann_2007-2100.nc"),"r", format="NETCDF4")
sea_levels_45 = Dataset("sea_level_indices_data/seaLevelAnom_marine-sim_rcp45_ann_2007-2100.nc","r", format="NETCDF4")
sea_levels_85 = Dataset("sea_level_indices_data/seaLevelAnom_marine-sim_rcp85_ann_2007-2100.nc","r", format="NETCDF4")
print(type(sea_levels_26))
print(type(sea_levels_45))
print(type(sea_levels_85))
print(sea_levels_26.variables.keys())
print(sea_levels_45.variables.keys())
print(sea_levels_85.variables.keys())
print(sea_levels_26.variables['seaLevelAnom'])
print(sea_levels_45.variables['seaLevelAnom'])
print(sea_levels_85.variables['seaLevelAnom'])

indices = []
for i in range(94):
    for j in range(135):
        for k in range(150):
            for l in range(3):
                if slevel[i,j,k,l] != '--':
                    #print(slevel[i,j,k,l])
                    indices.append((i,j,k,l, slevel[i,j,k,l]))
                    
print(len(indices))

#let's plot as images..
img1 = np.zeros([135,150])
img2 = np.zeros([135,150])
img3 = np.zeros([135,150])
cur_t = 0
for (t, lat, lng, perc, val) in indices:
    if t > cur_t:
        plt.imshow(img1)
        plt.show()
        plt.imshow(img2)
        plt.show()
        plt.imshow(img3)
        plt.show()
        cur_t = t
        img1 = np.zeros([135,150])
        img2 = np.zeros([135,150])
        img3 = np.zeros([135,150])
        print("Now at t: ", t)
        
    if perc == 0:
        img1[lat, lng] = val
    elif perc == 1:
        img2[lat, lng] = val 
    elif perc == 2:
        img3[lat, lng] = val

print("starting...")
for (dataset,val) in zip([sea_levels_26, sea_levels_45, sea_levels_85],[26,45,85]):
    print("Another dataset!", val)
    data = dataset.variables['seaLevelAnom']
    lats = dataset.variables['latitude']
    longs = dataset.variables['longitude']
    percs = dataset.variables['percentile']
    
    indices = []
    for i in range(94):
        for j in range(135):
            for k in range(150):
                for l in range(3):
                    if data[i,j,k,l] != '--':
                        #print(slevel[i,j,k,l])
                        indices.append((i,lats[j],longs[k],percs[l], data[i,j,k,l]))

    print(len(indices))
    with open("sea_level_indices_data/sea_level_results_"+ str(val), "wb") as f:
        pickle.dump(indices, f)
print("done")
