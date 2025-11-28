def are_amicable (a, b):
    # sum of divosors of a
    divisors_a = [1]
    i=2
    while i < a**0.5:
        if a%i == 0:
            divisors_a+=[i, a/i]
        i+=1
    if a % a**0.5 == 0 and a != 1:                      #special case
        divisors_a.append(a**0.5)
    s_a = 0 #sum
    for divisor in divisors_a:
        s_a+=divisor
    
    # sum of divosors of b
    divisors_b = [1]
    i=2
    while i < b**0.5:
        if b%i == 0:
            divisors_b+=[i, b/i]
        i+=1
    if b % b**0.5 == 0 and b != 1:                      #special case
        divisors_b.append(b**0.5)
    s_b = 0 #sum
    for divisor in divisors_b:
        s_b+=divisor
    
    # checking amicability
    return s_a == s_b

#testing
l=[1, 2, 3, 4]
for i1 in l:
    for i2 in l:
        print(f"are_amicable({i1}, {i2}) =", are_amicable(i1, i2))

#runtime
a = int(input("Enter number (a): "))
b = int(input("Enter number (b): "))
import timeit
runtime = timeit.timeit("are_amicable(a, b)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
are_amicable(a, b)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
divisors_a = [1]
steps=1

i=2
steps+=1

steps+=2
while i < a**0.5:
    steps+=1

    steps+=1
    if a%i == 0:
        divisors_a+=[i, a/i]
        steps+=3

    i+=1
    steps+=2

steps+=5
if a % a**0.5 == 0 and a != 1:                      #special case
    
    divisors_a.append(a**0.5)
    steps+=2

s_a = 0 #sum
steps+=1

for divisor in divisors_a:
    steps+=1

    s_a+=divisor
    steps+=2

divisors_b = [1]
steps+=1

i=2
steps+=1

steps+=2
while i < b**0.5:
    steps+=1

    steps+=1
    if b%i == 0:
        divisors_b+=[i, b/i]
        steps+=3

    i+=1
    steps+=2

steps+=5
if b % b**0.5 == 0 and b != 1:                      #special case
    
    divisors_b.append(b**0.5)
    steps+=2

s_b = 0 #sum
steps+=1

for divisor in divisors_b:
    steps+=1

    s_b+=divisor
    steps+=2

output = s_a == s_b
steps+=2

print("Number of steps =", steps)