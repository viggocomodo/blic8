cars = ["volvo", "bmw", "toyota"]

#add item to array 
cars.append("ferrari")
print(cars)
#remove item from an array
cars.remove("ferrari")
print(cars)

#loop over valus in array
for car in cars:    
    print(car)
    if car == "volvo":
        print("i like volvo")
    elif car == "bmw":
        print("bmws are expensive")

appleColor = "green"
mangoColor = "yellow"
fruitColor = [appleColor, mangoColor, "pineapple"]

    