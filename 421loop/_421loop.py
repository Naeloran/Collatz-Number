from ast import Return

victory = "We did it!"

print("Welcome. This program makes a Collatz Conjecture.")
print("Any number you give me will divided by two until it reaches one, or multiplied by three and then have one added to it.")
print("If you give me an odd number, it will be multiplied and added. It will be even after, and then divided.")
print("If you give me an even number, it will be divided until it reaches one, if possible. If it ends up odd, see previous.")
print("All positive numbers will enter the loop once they hit four. It goes four, two, one, forever.")

#The loop function
def collatz(number):
    if number % 2 == 0:
        print(number / 2)
        return(number / 2)
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return(result)

#Receive user input
x = int(input("Enter a starting number: "))
if int(x) < 1:
    print("Please enter a positive INTEGER!")

#Function to confirm if the number received is Odd or Even
def odd_or_even():
    if x % 2 == 0:
        print(x," is Even")
        pass
    else:
        print(x," is Odd")
        pass
#call odd_or_even function.
odd_or_even()

while x != 1:
    x = collatz(int(x))

#The end
print(x)
print(victory)        
        
#Goal here is even numbers get divided by two, odds get multiplied by three and one added to them.
