def area(length,width):
    rectangle= (length*width)
    print("The area of rectangle is",rectangle)
    area(length=int(input("Enter the length:")))
    area(width=int(input("Enter the radius:")))

