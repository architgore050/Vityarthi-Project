def aliquot_sum (n):
    divisors = [1]
    
    i=2
    while i < n**0.5:
        if n%i == 0:
            divisors+=[i, n/i]
        i+=1
    if n % n**0.5 == 0 and n != 1:                      #special case
        divisors.append(n**0.5)
    
    s = 0 #sum
    for divisor in divisors:
        s+=divisor
    
    return s

#testing
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 49, 50, 100, 200, 500, 1000]:
    print(f"aliquot_sum({i}) =", aliquot_sum(i))

#runtime
n = int(input("Enter number: "))
import timeit
runtime = timeit.timeit("aliquot_sum(n)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
aliquot_sum(n)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
divisors = [1]
steps=1

i=2
steps+=1

steps+=2
while i < n**0.5:
    steps+=1

    steps+=1
    if n%i == 0:
        divisors+=[i, n/i]
        steps+=3

    i+=1
    steps+=2

steps+=5
if n % n**0.5 == 0 and n != 1:                      #special case
    
    divisors.append(n**0.5)
    steps+=2

s = 0 #sum
steps+=1

for divisor in divisors:
    steps+=1

    s+=divisor
    steps+=2

output = s
steps+=1

print("Number of steps =", steps)