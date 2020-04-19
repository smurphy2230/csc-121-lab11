while True:
    try:
        num = int(input("Enter an integer between 1 and 100: "))
        if num < 1 or num > 100:
          raise()
    except:
        print("Invalid input")
    else:
        print(num)

