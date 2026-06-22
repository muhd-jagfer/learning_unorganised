x = int(input("enter a valur for x : "))
y = int(input("enter a value for y : "))

if x > y:
    print(x, "is greater than ", y)
elif x < y:
    print(f"{y} is greater than {x}")
else:
    print(f"{x} and {y} are equal")