#Sum square difference
sum_squares = 0 
for i in range (0,101): # for each number from 0 to 100
    i = i*i # i equal to the i time itself (square 2) 
    sum_squares += i  # for each number will be add to the total 

square_sum = 0  
for i in range (0,101): #for each number from 0 to 100
    square_sum += i # add that number to the total 

difference = sum_squares - square_sum*square_sum  # sum of the squares minus the square of the sum
print(difference) # print the result 
