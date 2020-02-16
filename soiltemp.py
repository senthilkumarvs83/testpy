x = [10,21,11,32,9,17,22,14]
y = [6,11,7,12,29,16,9,31]
soil_temp = [8,12,7,8,6,9,11,7]
coords = list(zip(x,y))
soil_dict = dict(zip(coords,soil_temp))
print(soil_dict)
for temp in soil_dict:
    print(temp)