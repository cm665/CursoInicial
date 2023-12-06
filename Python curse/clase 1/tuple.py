student = ("bro",21,"male")

print(student.count("bro"))
print(student.index("male"))

for x in student:
    print(x)

if "bro" in student:
    print("bro is here!")


utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()
dishes.update(utensils)
dinner_table = utensils.union(dishes)



for a in utensils:
    print(a)
print(dishes.difference(utensils))


