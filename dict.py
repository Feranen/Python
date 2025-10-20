lista = []

dict = {
    "name" : "TEst",
    "city" : "Warsaw"
}

print(dict["name"])
dict["name"] = "Ola"
print(dict["name"])
dict["street"] = "Strach"
print(dict)
list = {0: "zero", 1 : "Jeden", 2 : [1,2,3],}
print(list[2][2])
del list[2]
print(list)

zagniezdzone = {
    "1" : {0: [1,2,3,4], "1" : [1,2,2,3]},
    "2" : {1: [1212,1], 2 : [2,3,4]}
}

print(zagniezdzone["1"]["1"][1])