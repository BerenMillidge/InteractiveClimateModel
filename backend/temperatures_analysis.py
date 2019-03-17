from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import pickle


temps_26 = Dataset("temperature_data/tasAnom_rcp26_land-prob_uk_25km_sample_b8110_30y_ann_20091201-20991130.nc","r", format="NETCDF4")
temps_45 = Dataset("temperature_data/tasAnom_rcp45_land-prob_uk_25km_sample_b8110_30y_ann_20091201-20991130.nc","r", format="NETCDF4")
temps_85 = Dataset("temperature_data/tasAnom_rcp85_land-prob_uk_25km_sample_b8110_30y_ann_20091201-20991130.nc","r", format="NETCDF4")
print(type(temps_26))
print(type(temps_45))
print(type(temps_85))
print(temps_26.variables.keys())
print(temps_45.variables.keys())
print(temps_85.variables.keys())
print(temps_26.variables['tasAnom'])
print(temps_45.variables['tasAnom'])
print(temps_85.variables['tasAnom'])


vs = temps_26.variables
print(vs.keys())
time = vs['time']
year = vs['year']
print(year)
print(year[0:8])
samp = vs['sample']
print(samp)
lat = vs['latitude']
lng = vs['longitude']
print(lat)
print(lng)
print(lat[0,:])
print(lat[:,0])
print(lng[0,:])
print(lng[:,0])
print(np.mean(lat))
print(np.mean(lng))

print(vs['tasAnom'])
coords = vs['tasAnom'][5,42,20,1]
print(coords.shape)
#for el in coords:
# print(el)

print(vs['transverse_mercator'])
print(vs['projection_x_coordinate'][0:10])

for (dataset, val) in zip([temps_26, temps_45, temps_85], [26,45,85]):
    vs = dataset.variables
    print("beginning dataset: " + str(val))
    temps = vs['tasAnom'][:,:,:,52]
    lats = vs['latitude']
    longs = vs['longitude']
    indices = []
    for (t,year) in enumerate(vs['year']):
        for (y_index, y_coord) in enumerate(vs['projection_y_coordinate']):
            for (x_index, x_coord) in enumerate(vs['projection_x_coordinate']):
                if temps[t,y_index, x_index] != "--":
                    indices.append([year, lats[y_index, x_index], longs[y_index, x_index], temps[t,y_index,x_index]])
                    
    with open("temperature_data/pdf_annual/indices_" + str(val), "wb") as f:
        pickle.dump(indices, f)

print("done!")
                   