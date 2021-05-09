counties =["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print  (counties[1])


for i in range(len(counties)):
    print (counties[i])

#looping through dictionary 
counties_dict = {"Arapahoe":422829, "Denver":463353,"Jefferson":432438}


print("......printing keys......")
for x in counties_dict.keys():
    print(x)

print("........Printing Values..........")
for x in counties_dict:
    print(counties_dict[x])

for x in counties_dict.values():
    print(x) 

print("printing both key and value")
for key, value in counties_dict.items():
    print (key + ""+ "county has"+ ""+str(value) +""+ "registered voters")