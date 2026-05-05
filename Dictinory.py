# Example of Dictionary
from os import process_cpu_count
chai_type = {"Masala" : "Spicy" , "Ginger": "Zesty", "Green": "Mint"}

# print(chai_type.get("Ginger"))
chai_type["Green"] = 'Fresh Chai'
print(chai_type)

for chai in chai_type:
    print(chai, chai_type[chai])



    if "masala" in chai_type:
        print("I have Masala chai")
    else:
        print("Not a masalal chai")