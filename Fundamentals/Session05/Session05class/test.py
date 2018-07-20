# minh_duc = ["Minh Duc", "Son La", 19, 2, 1, 10]

# dictionary/ object/ map

# luu theo cap    key : value 
person = {
    "name" : "Duc cop",
    "age" : 19,
    "ex" : 2,
    "iq" : 1, 

} 
person["hometown"] = "Son La" #create add/update new key value
person["ex"] = 3 
# goi value : person[key]

# for key in person.keys():
#     print(person[key],end="\t")

# print(person["name"])


# for value in person.values():
#     print(value)

# kiem tra key co trong dictionary ko 
key = "school"
if key in person:
    print(person(key))
else:
    print("Not Found")







