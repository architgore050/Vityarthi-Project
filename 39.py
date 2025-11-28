def partition_function (n, slots=-1, maximum=-1):
    if slots==-1:
        slots=n
    if maximum==-1:
        maximum=n
    
    if n==0:
        return 1
    if slots==0:
        return 0
    
    ans=0
    i=0
    if n<maximum: smaller = n
    else: smaller = maximum
    while i<=smaller:
        ans+=partition_function(n-i, slots=slots-1, maximum=i)
        i+=1
    
    return ans


#testing
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50]:
    print(f"partition_function({i}) =", partition_function(i))

#runtime
n = int(input("Enter number (n): "))
print("Result =", partition_function(n))
import timeit
runtime = timeit.timeit("partition_function(n)", globals=globals(), number = 10000)
print("Average runtime =", runtime/10000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
partition_function(n)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def stepsCounter (n, slots=-1, maximum=-1):
    steps=1
    if slots==-1:

        slots=n
        steps+=1
    
    steps+=1
    if maximum==-1:

        maximum=n
        steps+=1
    
    steps+=1
    if n==0:
        
        steps+=1
        return (1, steps)
    
    steps+=1
    if slots==0:

        steps+=1
        return (0, steps)
    
    ans=0
    steps+=1

    i=0
    steps+=1

    steps+=1
    if n<maximum:
        steps+=1

        smaller = n
        steps+=1

    else: 
        smaller = maximum
        steps+=1
    steps+=1
    while i<=smaller:
        steps+=1

        response = stepsCounter(n-i, slots=slots-1, maximum=i)
        ans+=response[0]
        steps+=4
        steps+=response[1]

        i+=1
        steps+=2
    
    steps+=1
    return (ans, steps)

print("Number of steps =", stepsCounter(n)[1])