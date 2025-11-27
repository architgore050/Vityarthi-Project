def gcd (a, b):
    if a<b:
        a,b=b,a
    r=a%b
    if r == 0:
        return b
    else:
        return gcd(b, r)

#print(gcd(14, 21))

def euler_phi(n):
    count = 0
    k = 0
    while k < n:
        k+=1
        if gcd(n, k) == 1:
            count += 1
    return count

#testing
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 30, 36, 40, 49, 100, 101]:
    print(f'input: {i}, output: {euler_phi(i)}')

#runtime
n = int(input('enter number: '))
import timeit
runtime = timeit.timeit('euler_phi(n)', globals=globals(), number = 1000)
print('average runtime:', runtime/1000)

#measuring steps
steps=0
def gcd (a, b):
    global steps
    steps+=1

    steps+=1
    if a<b:
        steps+=1

        a,b=b,a
        steps+=2

    r=a%b
    steps+=2

    steps+=1
    if r == 0:
        steps+=1

        steps+=1
        return b
    else:
        steps+=1

        steps+=1
        return gcd(b, r)

def euler_phi(n):
    global steps
    
    count = 0
    steps+=1

    k = 0
    steps+=1

    while k < n:
        steps+=2

        k+=1
        steps+=2

        steps+=1
        if gcd(n, k) == 1:
            steps+=1
            
            count += 1
            steps+=2
    
    steps+=1
    return count

euler_phi(n)
print('total steps:', steps)