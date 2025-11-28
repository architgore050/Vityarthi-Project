def is_highly_composite (n):
    num_div = 2
    i=2
    while i < n**0.5:
        if n%i == 0:
            num_div+=2
        i+=1
    if n % n**0.5 == 0 and n != 1:                      #special case
        num_div+=1
    target = num_div
    
    k = n
    while k > 0:
        num_div = 2
        i=2
        while i < k**0.5:
            if k%i == 0:
                num_div+=2
            i+=1
        if k % k**0.5 == 0 and k != 1:                      #special case
            num_div+=1
        
        if num_div > target:
            return False
        k-=1
        
    return True

#testing
for i in [1, 2, 3, 4, 5, 7, 9, 10, 11, 12, 13, 15, 20, 25, 49, 50, 97, 100, 101]:
        print(f"is_highly_composite({i}) =", is_highly_composite(i))

#runtime
n = int(input("Enter number: "))
import timeit
runtime = timeit.timeit("is_highly_composite(n)", globals=globals(), number = 10000)
print("Average runtime =", runtime/10000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
is_highly_composite(n)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def isHighlyComposite_stepsCounting (n):
    num_div = 2
    steps=1

    i=2
    steps+=1

    steps+=3
    while i < n**0.5:
        steps+=3

        steps+=2
        if n%i == 0:

            num_div+=2
            steps+=2

        i+=1
        steps+=2

    steps+=5
    if n % n**0.5 == 0 and n != 1:                      #special case
        
        num_div+=1
        steps+=2

    target = num_div
    steps+=1
    
    k = n
    steps+=1

    steps+=1
    while k > 0:
        steps+=1

        num_div = 2
        steps+=1

        i=2
        steps+=1

        steps+=2
        while i < k**0.5:
            steps+=2

            steps+=2
            if k%i == 0:

                num_div+=2
                steps+=2

            i+=1
            steps+=2
        
        steps+=5
        if k % k**0.5 == 0 and k != 1:                      #special case
            
            num_div+=1
            steps+=2
        
        steps+=1
        if num_div > target:

            steps+=1
            return steps
        
        k-=1
        steps+=2
    
    steps+=1
    return steps

print("Number of steps =", isHighlyComposite_stepsCounting(n))