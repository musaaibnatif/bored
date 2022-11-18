array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in array:
    if(i%5 == 0 and i%3 == 0):
        print("FizzBuzz")
    elif (i%5 == 0):
        print("Buzz")
    elif(i%3 == 0):
        print("Fizz")