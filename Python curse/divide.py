try:
    numerator = int(input("enter a number to divide: "))
    denominator = int(input("enter a number to divide by: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("nononononnoon")
except ValueError as e:
    print(e)
    print("enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("this will always execute")


