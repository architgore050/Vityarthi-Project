def prime_pi(n):
    p = [False] + [True]*(n-1)
    i = 1
    nHalf = n/2
    while i < nHalf:
        i+=1
        m = 2
        while True:
            im = i*m
            if im > n:
                break
            p[im-1] = False
            m+=1

    count = 0
    for i in p:
        if i:
            count+=1
    return count

#testing
for i in [0, 1, 2, 3, 5, 10, 11, 20, 30, 50, 100, 101, 1000, 10000, 1000000]:
    print(f'input: {i}, output: {prime_pi(i)}')

#speed
n=int(input('enter number: '))
import timeit
runtime = timeit.timeit('prime_pi(n)', globals=globals(), number=1000)
print('mean runtime:', runtime/1000)

#steps
steps=0

p = [True]*n
steps+=1

i = 1
steps+=n+2

nHalf = n/2
steps+=1

steps+=1
while i < nHalf:
    steps+=1

    i+=1
    steps+=2

    m = 2
    steps+=1

    while True:
        steps+=1

        im = i*m
        steps+=2

        steps+=1
        if im > n:
            steps+=1

            steps+=1
            break

        p[im-1] = False
        steps+=2

        m+=1
        steps+=2

count = 0
steps+=1

for i in p:
    steps+=1

    steps+=1
    if i:
        steps+=1

        count+=1
        steps+=1
    
output = count
steps+=1

print('total steps:', steps)