square_side = int(input("Enter the size of the pattern: "))
square = 0
while square < square_side:
    for row in range(square_side):
        print("*", end="")
    print()
    square +=1

