def legendre_symbol(a, p):
    if (a**((p-1)/2)) % p == 1:
        return 1
    else:
        return -1

#test
for i in [(1, 3), (2, 3), (2, 5), (3, 5), (4, 5), (2, 7), (3, 7), (5, 7), (6, 7), (-1, 7), (2, 11), (3, 11), (6, 13), (7, 13), (9, 13)]:
    print(f'input (a): {i[0]}, input (p), {i[1]}, outut: {legendre_symbol(i[0], i[1])}')

# runtime calculation
a=int(input('enter a: '))
p=int(input('enter p: '))
import timeit
runtime = timeit.timeit('legendre_symbol(a, p)', globals=globals(), number = 1000000)
print('average runtime:', runtime/1000000)

#step count
steps = 0

steps+=5
if (a**((p-1)/2)) % p == 1:
    steps+=1

    output = 1
    steps+=1

else:
    steps+=1

    output = -1
    steps+=1

print('total steps:', steps)