try:
    width = float(input("Enter rectangle width: ").strip())
    length = float(input("Enter rectangle length: ").strip())

    if width==length :
        exit("That looks like a square.")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number  for the width and the length!")

