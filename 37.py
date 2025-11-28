def pollard_rho(n, c = 1):
    #is n prime
    i=2
    is_prime=True
    while i<=n/2:
        if n%i == 0:
            is_prime=False
            # I should return the value of i here since technically we have found a multiple of n but the question specifically requires finding the factor through pollard's rho alogirthm
            break
        i+=1
    if is_prime:
        return 1
    
    #pollard's rho tends to fail for powers of 2
    if n%2==0:
        return 2

    #pollar's rho process
    x = 2
    y = 2
    i=0
    while True:
        x = (x**2 + c) % n
        y = (((y**2 + c) % n)**2 + c) % n

        #calculating gcd
        if x>y:
            diff = x-y
        else:
            diff = y-x
        if diff>n:
            smaller = n
        else:
            smaller = diff
        j = smaller//2
        gcd = 1
        while j>1:
            if diff%j==0 and n%j==0:
                gcd = j
                break
            j-=1
        
        i+=1
        if gcd == n:
            return pollard_rho(n, c=c+1)
        
        if gcd!=1:
            return gcd


#testing
for i in [50, 75, 80, 81, 93, 100, 101, 120, 150, 151, 209]:
    print(f"pollard_rho({i}) =", pollard_rho(i))

#runtime
n = int(input("Enter number (n): "))
print("Result =", pollard_rho(n))
import timeit
runtime = timeit.timeit("pollard_rho(n)", globals=globals(), number = 1000)
print("Average runtime =", runtime/1000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
pollard_rho(n)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def stepsCounter (n, c=1):
    i=2
    steps=1

    is_prime=True
    steps+=1

    steps+=2
    while i<=n/2:
        steps+=2

        steps+=2
        if n%i == 0:

            is_prime=False
            steps+=1

            steps+=1
            break
        
        i+=1
        steps+=2

    steps+=1
    if is_prime:

        steps+=1
        return steps
    
    steps+=2
    if n%2==0:

        steps+=1
        return steps

    x = 2
    steps+=1

    y = 2
    steps+=1

    i=0
    steps+=1

    while True:
        steps+=1

        x = (x**2 + c) % n
        steps+=3

        y = (((y**2 + c) % n)**2 + c) % n
        steps+=6

        steps+=1
        if x>y:
            steps+=1

            diff = x-y
            steps+=2

        else:
            diff = y-x
            steps+=1

        steps+=1
        if diff>n:
            steps+=1

            smaller = n
            steps+=1

        else:
            smaller = diff
            steps+=1

        j = smaller//2
        steps+=3

        gcd = 1
        steps+=1

        steps+=1
        while j>1:
            steps+=1

            steps+=5
            if diff%j==0 and n%j==0:

                gcd = j
                steps+=1

                steps+=1
                break

            j-=1
            steps+=1
        
        i+=1
        steps+=1

        steps+=1
        if gcd == n:

            steps+=1
            return stepsCounter(n, c=c+1)
        
        steps+=1
        if gcd!=1:

            steps+=1
            return steps

print("Number of steps =", stepsCounter(n))