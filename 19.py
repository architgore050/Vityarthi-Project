def twin_primes (n):
    # finding primes under n
    p = []
    i=2
    while i<=n:
        k=2
        is_prime=True
        while k <= i/2:
            if i%k==0:
                is_prime=False
                break
            k+=1
        
        if is_prime:
            p.append(i)
        
        i+=1
    
    # finding twin prime pairs (pairs that differ by 2)
    l = 0
    for prime in p:
        l+=1
    
    prime_pairs=[]
    index = 0
    while index < l-1:
        if p[index]+2==p[index+1]:
            prime_pairs.append((p[index], p[index+1]))
        index+=1
    
    return prime_pairs

#testing
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100]:
    print(f"twin_primes({i}) =", twin_primes(i))

# runtime
n = int(input("Enter number: "))
print("Result =", twin_primes(n))
import timeit
runtime = timeit.timeit("twin_primes(n)", globals=globals(), number=1000000)
print("Runtime =", runtime/1000000)

#memory usage
import tracemalloc
tracemalloc.start()
twin_primes(n)
max_usage = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", max_usage, "Bytes")

#steps counting
p = []
steps=1

i=2
steps+=1

steps+=1
while i<=n:
    steps+=1

    k=2
    steps+=1

    is_prime=True
    steps+=1

    steps+=2
    while k <= i/2:
        steps+=1

        steps+=1
        if i%k==0:
            steps+=1

            is_prime=False
            steps+=1

            steps+=1
            break
        
        k+=1
        steps+=1
    
    steps+=1
    if is_prime:
        steps+=1

        p.append(i)
        steps+=1
    
    i+=1
    steps+=1

l = 0
steps+=1

for prime in p:
    steps+=1

    l+=1
    steps+=1

prime_pairs=[]
steps+=1

index = 0
steps+=1

steps+=2
while index < l-1:
    steps+=2

    steps+=5
    if p[index]+2==p[index+1]:
        steps+=1

        prime_pairs.append((p[index], p[index+1]))
        steps+=5

    index+=1
    steps+=1

output = prime_pairs
steps+=1

print("Steps count =", steps)