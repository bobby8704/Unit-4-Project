a, b = 1, 1 # set value for the sequence
total = 0 # total will calculate the sum of the sequence
while a <= 4000000: # while all the value is less than or equal to 4 million
    if a % 2 == 0:  # if the number in the number in the sequence is an even number
        total += a  # total will add that number
    a, b = b, a+b  # formula for Fibonacci 
print (total)
