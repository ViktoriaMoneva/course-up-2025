if __name__ == '__main__':
    list_of_sides = []
    while True:
        sides = input("X, Y")
        if sides == "":
            break
        sides2 = sides.split(',')
        list_of_sides.append((float(sides2[0]), float(sides2[1])))

    print (list_of_sides)

    for p in list_of_sides:

