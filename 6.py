def factorial(n):
    assert n>=0 and n==int(n), 'n must be a positive integer'
    soln = 1
    i=1
    while i<n:
        i+=1
        soln*=i
    return soln

#testing
for n in [0, 1, 2, 3, 4, 5, 7, 10, 50]:
    print(f"The factorial of {n} is {factorial(n)}")

#calculating runtime
import timeit
n=int(input('enter number: '))
runtime = timeit.timeit('factorial(n)', globals=globals(), number=10**6)
print(f'average runtime for n={n}: {runtime/10**6} seconds')

#counting steps
steps=0

assert n>=0 and n==int(n), 'n must be a positive integer'
steps+=2

soln = 1
steps+=1

i=1
steps+=1

while i<n:
    steps+=1

    i+=1
    steps+=1

    soln*=i
    steps+=2

output = soln
steps+=1

print(f'number of steps run for n={n}: {steps}')