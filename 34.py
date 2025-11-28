def polygonal_number (s, n):
    if s<3: return None
    if n<0: return None
    return (s-2)*n*(n+1)//2 - (s-3)*n

#testing
for i in [(3, 1), (3, 7), (4, 5), (5, 3), (6, 4), (4, 10000), (1000, 5), (5, 1), (3, 10), (2, 5), (6, 0), (4, -3)]:
    print(f"polygonal_number{i} =", polygonal_number(i[0], i[1]))

#runtime
s = int(input("Enter number (s): "))
n = int(input("Enter number (n): "))
print("Result =", polygonal_number(s, n))
import timeit
runtime = timeit.timeit("polygonal_number(s, n)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
polygonal_number(s, n)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def polygonalNumber_steosCounter (s, n):
    steps=1
    if s<3:

        steps+=1
        return steps
    
    steps+=1
    if n<0:

        steps+=1
        return steps
    
    output = (s-2)*n*(n+1)//2 - (s-3)*n
    steps+=8

    steps+=1
    return steps

print("Number of steps =", polygonalNumber_steosCounter(s, n))