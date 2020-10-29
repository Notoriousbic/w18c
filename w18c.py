numbers = [30, 55, 45, 36, 80, 95, 105, 120, 225, 220, 333, 33, 125, 500, 250]        


def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    print(x)
for number in numbers:
    fizzbuzz(number)