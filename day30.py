#smallest multiple 
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #list of multiples

multiple = []

for num in range(20, 999999999):  #testing all the number from 20 to 999999999
    for i in num_list:  # loop through the list of multiples
        if num % i == 0:  # if num is divisible to each number in the list 
            multiple.append(num)  #add the number to the list "multiple"
print(min(multiple))  # print the smallest valuee in the list 
