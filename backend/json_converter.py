import json
from collections import defaultdict
import numpy as np

# convert temperatures!

def parse_temp_list_into_jsondict(l):
    j = defaultdict(list)
    for (t, lat, lng, val) in l:
        #print(type(val))
        #print(val)
        #print(type(t))
        #print(t)
        #print(type(lat))
        #print(lat)
        #print(type(lng))
        #print(lng)
        val = val.item()
        lat = np.ndarray.item(lat.data)
        lng = np.ndarray.item(lng.data)
        t = np.ndarray.item(t.data)
        j[t].append({"lat": lat, "lng": lng, "val": val})
    return j

def save_temp_to_json(j, sname):
    with open(sname + ".json", "w+") as f:
        json.dump(j,f)
    
with open("temperature_data/pdf_annual/indices_26", "rb") as f:
    l = pickle.load(f)
    j = parse_temp_list_into_jsondict(l)
    print(j.keys())
    save_to_json(j, "json_pdf_26_data.json")
    
with open("temperature_data/pdf_annual/indices_45", "rb") as f:
    l = pickle.load(f)
    j = parse_temp_list_into_jsondict(l)
    print(j)
    save_to_json(j, "json_pdf_45_data.json")
    
with open("temperature_data/pdf_annual/indices_85", "rb") as f:
    l = pickle.load(f)
    j = parse_temp_list_into_jsondict(l)
    print(j.keys())
    save_to_json(j, "json_pdf_85_data.json")


# convert sea levels

def preinitialize_jsondict():
    Jsondict = {"5th": defaultdict(list), "50th": defauldict(list), "99th": defaultdict(list)}
    for k in Jsondict.keys():
        for i in range(111):
            Jsondict[k][str(i)] = []

    return Jsondict

def parse_sea_level_list_into_jsondict(l):
    j = {"5th": defaultdict(list), "50th": defaultdict(list), "95th": defaultdict(list)}
    for (t, lat, lng, percs, val) in l:
        lat = np.ndarray.item(lat.data)
        lng = np.ndarray.item(lng.data)
        val = np.ndarray.item(val.data)
        if percs == 5:
            j["5th"][t].append({"lat": lat,"lng": lng,"val":val})
        if percs == 50:
            j["50th"][t].append({"lat": lat,"lng": lng,"val":val})
        if percs == 95:
            j["95th"][t].append({"lat": lat,"lng": lng,"val":val})
    return j

def save_sea_level_to_json(j, sname):
    with open(sname + ".json", "w+") as f:
        json.dump(j,f)
    
    midperc = j["50th"]
    with open(sname + "_50th.json", "w+") as f:
        json.dump(midperc,f)

j = parse_sea_level_list_into_jsondict(l)
print("parsed!")
save_to_json(j, "sea_level_indices_data/sea_level_26_json")
#print(j)
print("done!")


with open("sea_level_indices_data/sea_level_results_45", "rb") as f:
    l = pickle.load(f)
print("loaded")
j = parse_sea_level_list_into_jsondict(l)
print("parsed!")
save_to_json(j, "sea_level_indices_data/sea_level_45_json")
#print(j)
print("done! 1")
with open("sea_level_indices_data/sea_level_results_85", "rb") as f:
    l = pickle.load(f)
print("loaded")
j = parse_sea_level_list_into_jsondict(l)
print("parsed!")
save_to_json(j, "sea_level_indices_data/sea_level_85_json")
#print(j)
print("done! 2")