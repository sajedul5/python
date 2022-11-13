# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Shakil", 27, "Male")

print(student.count("27"))
print(student.index("Male"))

for x in student:
    print(x)

if "Shakil" in  student:
    print("Shakil is here!")