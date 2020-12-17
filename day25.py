# Find the sum of all the multiples of 3 or 5 below 1000.

total_sum = 0

for i in range (0, 1000): # for every number from 0 to 999
    if i % 3 == 0 or i % 5 == 0:    # if that number is a multiple of 3 or five
        total_sum = total_sum + i       # total sum would add that number 
print(total_sum)

