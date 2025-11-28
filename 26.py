def mod_inverse (a, m):
    '''
    x=?
    a*x % m = 1
    (a*x - 1) % m = 0
    (a*x - 1) = k*m, k = anything
    x = (k*m + 1)/a
    I am assuming x is required as integer
    '''
    if a==m:
        return None                     #x can never be an integer
    if a==0:
        return None                     #condition will never be satisfied regardless of x and deviding by 0 will not work
    if m==0:
        return None                     #condition will never be satisfied regardless of x
    if a>m:
        s=m
    else:
        s=a
    i = 2
    while i <= s/2:
        if a%i == 0 and m%i == 0:
            return None                 #GCD of a and m has to be 1 otherwise x will never be an integer
        i+=1
    

    k=0
    while True:
        x = (k*m+1)/a
        if x==int(x):
            return x
        k+=1



#testing
l = [0, 1, 2, 3]
for a in l:
    for m in l:
        print(f"mod_inverse({a}, {m}) =", mod_inverse(a, m))

#runtime
a = int(input("Enter number (a): "))
m = int(input("Enter number (m): "))
print("Result =", mod_inverse(a, m))
import timeit
runtime = timeit.timeit("mod_inverse(a, m)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
mod_inverse(a, m)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def modInverse_stepsCounter (a, m):
    steps=1
    if a==m:

        steps+=1
        return steps
    
    steps+=1
    if a==0:

        steps+=1
        return steps
    
    steps+=1
    if m==0:

        steps+=1
        return steps
    
    steps+=1
    if a>m:
        steps+=1

        s=m
        steps+=1
    
    else:
        s=a
        steps+=1

    i = 2
    steps+=1

    steps+=2
    while i <= s/2:
        steps+=2

        steps+=5
        if a%i == 0 and m%i == 0:

            steps+=1
            return steps
        i+=1
        steps+=2

    k=0
    steps+=1

    while True:
        steps+=1

        x = (k*m+1)/a
        steps+=4

        steps+=2
        if x==int(x):

            steps+=1
            return steps
        
        k+=1
        steps+=2

print("Number of steps =", modInverse_stepsCounter(a, m))