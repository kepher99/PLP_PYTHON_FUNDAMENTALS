supplies = ["tent","sleeping bags","water","raspberry pi", "coffee", "knife","ethernet cable", "flash drive","beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 95.5,False]

#supplies.append("toilet paper")

#supplies.append("bidet")

#supplies.extend(["toilet paper","bidet"])

#supplies = supplies + ["toilet paper","bidet"]

supplies.insert(0, "bidet")

supplies.insert(-1, "toilet paper")

supplies.pop(0)

print("This item was just deleted: " + supplies.pop(0))

print(supplies)