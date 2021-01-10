def lpf(n): #Largest Prime Factor
    i = 2

    while i <= n / i: # while i is less than or equal to n divided by i
        if n % i == 0:  # if n is divisible by i
            n /= i  # n is equal to n/i
        else:
            i += 1  i+1 until n is divisble by i
            
    return n
  
print (lpf(600851475143))
