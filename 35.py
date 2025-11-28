def is_carmichael (n):
    if n<1: return None
    if n==1 or n==2 or n==3: return False
    a = 1
    while a < n:
        # is gcd(a, n) = 1
        if a>n: larger = a/2
        else: larger = n/2
        i = 2
        gcd_1 = True
        while i<larger:
            if a%i==0 and n%i==0:
                gcd_1 = False
                break
            i+=1
        if not gcd_1:
            a+=1
            continue
        
        if pow(a, n-1, n) != 1:
            return False

        a+=1
    return True

#testing
for i in [1, 2, 3 ,4, 6, 15, 561, 1105, 1729, 2465, 5610, 6601]:
    print(f"is_carmichael({i}) =", is_carmichael(i))

#runtime
n = int(input("Enter number (n): "))
print("Result =", is_carmichael(n))
import timeit
runtime = timeit.timeit("is_carmichael(n)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
is_carmichael(n)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def stepsCounter (n):
    steps=1
    if n<1:

        steps+=1
        return steps
    
    steps+=5
    if n==1 or n==2 or n==3:
        
        steps+=1
        return steps
    
    a = 1
    steps+=1

    steps+=1
    while a < n:
        steps+=1
        if a>n:
            steps+=1

            larger = a/2
            steps+=2

        else:
            larger = n/2
            steps+=1

        i = 2
        steps+=1

        gcd_1 = True
        steps+=1

        steps+=1
        while i<larger:
            steps+=1

            steps+=5
            if a%i==0 and n%i==0:

                gcd_1 = False
                steps+=1

                steps+=1
                break
            
            i+=1
            steps+=1
        steps+=1
        if not gcd_1:

            a+=1
            steps+=1

            steps+=1
            continue
        
        steps+=3
        if pow(a, n-1, n) != 1:

            steps+=1
            return steps

        a+=1
        steps+=2
    
    steps+=1
    return steps

print("Number of steps =", stepsCounter(n))