def prime_factors (n):
    l = []      # list of prime factors

    i=2
    while i<=n:

        if n%i==0:
            
            isPrime = True
            k = 2
            while k<i:
                if i%k==0:
                    isPrime = False
                k+=1
            
            if isPrime == True:
                l.append(i)
        i+=1
    return l

#testing
for i in [0, 1, 2, 3, 4, 5, 6, 10, 11, 15, 17, 20, 21, 50, 100, 200, 1000]:
    print(f"prime_factors({i}) =", prime_factors(i))

#runtime calculation
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("prime_factors(n)", globals=globals(), number = 1000000)
print("runtime = ", runtime/1000000, "s", sep="")

#steps claculation
l = []      # list of prime factors
steps=1

i=2
steps+=1

steps+=1
while i<=n:
    steps+=1

    steps+=2
    if n%i==0:
        steps+=1
        
        isPrime = True
        steps+=1

        k = 2
        steps+=1

        steps+=1
        while k<i:
            steps+=1

            steps+=1
            if i%k==0:
                steps+=1

                isPrime = False
                steps+=1
            
            k+=1
            steps+=1
        
        steps+=1
        if isPrime == True:
            steps+=1

            l.append(i)
            steps+=2
    
    i+=1
    steps+=2

output = l
steps+=1

print("step count =", steps)