def is_prime_miller_rabin(n, k):
    #some base cases
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    #n-1 = d*2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    #actual process
    a = 2
    tests_done = 0
    while tests_done < k and a < n - 1:
        x = pow(a, d, n)
        if x != 1 and x != n - 1:
            r = 1
            composite = True
            while r < s:
                x = pow(x, 2, n)
                if x == n - 1:
                    composite = False
                    break
                if x == 1:
                    return False
                r += 1
            if composite:
                return False
        a += 1
        tests_done += 1
    return True

#testing
for i in [(2, 3), (5, 1), (97, 3), (9, 3), (1001, 3), (100000, 3), (341, 2), (2047, 3), (561, 5)]:
    print(f"is_prime_miller_rabin{i} =", is_prime_miller_rabin(i[0], i[1]))

#runtime
n = int(input("Enter number (n): "))
k = int(input("Enter number (k): "))
print("Result =", is_prime_miller_rabin(n, k))
import timeit
runtime = timeit.timeit("is_prime_miller_rabin(n, k)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
is_prime_miller_rabin(n, k)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def stepsCounter (n, k):
    steps=1
    if n < 2:

        steps+=1
        return steps
    
    steps+=2
    if n in (2, 3):

        steps+=1
        return steps
    
    steps+=2
    if n % 2 == 0:

        steps+=1
        return steps

    d = n - 1
    steps+=2

    s = 0
    steps+=2

    steps+=2
    while d % 2 == 0:
        steps+=2

        d //= 2
        steps+=3

        s += 1
        steps+=1

    a = 2
    steps+=1

    tests_done = 0
    steps+=1
    
    steps+=4
    while tests_done < k and a < n - 1:
        steps+=4

        x = pow(a, d, n)
        steps+=3

        steps+=4
        if x != 1 and x != n - 1:

            r = 1
            steps+=1

            composite = True
            steps+=1

            steps+=1
            while r < s:
                steps+=1

                x = pow(x, 2, n)
                steps+=3

                steps+=2
                if x == n - 1:

                    composite = False
                    steps+=1

                    steps+=1
                    break

                steps+=1
                if x == 1:

                    steps+=1
                    return steps
                
                r += 1
                steps+=2
            
            steps+=1
            if composite:

                steps+=1
                return steps
        
        a += 1
        steps+=2

        tests_done += 1
        steps+=1
    
    steps+=1
    return steps

print("Number of steps =", stepsCounter(n, k))