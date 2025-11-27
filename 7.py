def is_pallindrome(n):
    n=str(n)
    if n==n[::-1]:
        return True
    else:
        return False

#testing
for n in [0, 5, 11, 12, 121, 123, 12321, 1221, 12345, -121, 1234567890987654321]:
    print(f'Input: {n}, Output: {is_pallindrome(n)}')

#runtime calculation
n=int(input('enter number: '))
import timeit
runtime=timeit.timeit('is_pallindrome(n)', globals=globals(), number=10**6)
print(f'average runtime for n={n}: {runtime/10**6} seconds')

#steps calculation
steps=0

n=str(n)
steps+=1

steps+=1
if n==n[::-1]:
    steps+=2
    
    output = True
    steps+=1

else:
    steps+=1
    output = False

print(f'number of steps run for n={n}: {steps}')