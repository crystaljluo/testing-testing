i = int(input("Enter a number: "))
for n in range(1,i+1):
    if n%3 == 0 and n%5 == 0:
        print("FizzBuzz")
        continue
    elif n%3 == 0:
        print("Buzz")
        continue
    elif n%5 == 0:
        print("Fizz")
        continue
    print(n)

        

           
