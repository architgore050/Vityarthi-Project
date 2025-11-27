def digital_root(n):
    n=str(abs(n))
    if len(n)==1:
        return int(n)
    else:
        sum=0
        for digit in n:
            sum+=int(digit)
        return digital_root(sum)

#testing
for n in [0, 5, 12, 123, 9875, 493193, 9999, 1000, -9875, 1234567890]:
    print(f'digital root of {n} is {digital_root(n)}')

#calculating runtime
import timeit
n=int(input('enter number: '))
runtime=timeit.timeit('digital_root(n)', globals=globals(), number=1000000)
print(f'average runtime: {runtime/1000000}')