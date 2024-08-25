age = 19
isBirthday = False

if age >= 21:
    print("YOU CAN DRINK!!")
    if isBirthday:
        print("HAPPY B-DAY, HERE IS A FREE MARTINI!!!")
elif age >= 18:
    print("YOU CAN COME IN BUT NO DRINKING!")
    if isBirthday:
        print("HAPPY B-DAY, HERE IS A FREE APPLE JUICY!!!")
else:
    print("SORRY GO HOME BUBS!!!")        