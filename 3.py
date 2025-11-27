def divisor_sum(n):
    addition = 0
    i = 0
    while i<=n:
        i+=1
        if n % i == 0:
            addition += i
    return addition

#testing
for i in [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 25, 28, 30, 100, 101]:
    print(f'input: {i}, output: {divisor_sum(i)}')

#time
n = int(input('enter number: '))
import timeit
runtime=timeit.timeit('divisor_sum(n)', globals=globals(), number=1000)
print(f'Execution time: {runtime/1000} seconds')

#steps counter
steps=0

addition = 0
steps+=1

i = 0
steps+=1

steps+=1
while i<=n:
    steps+=2

    i+=1
    steps+=2

    steps+=2
    if n % i == 0:
        steps+=1

        addition += i
        steps+=1

steps+=1
output = addition

print('Steps:', steps)