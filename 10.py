def is_abundant(n):
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum+=i
        i+=1
    if sum>n:
        return True
    else:
        return False

#testing
for i in [1, 2, 3, 4, 12, 18, 15, 28, 945, 97]:
    print(f'Input: {i}, Ouput:{is_abundant(i)}')

#runtime calculation
import timeit
n=int(input('enter number: '))
runtime=timeit.timeit('is_abundant(n)', globals=globals(), number=10**6)
print(f'average runtime for n={n}: {runtime/10**6} seconds')