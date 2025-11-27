def mobius(n):
    #number of divisible primes found
    count=0
    
    #looping over all numbers up to n ignoring 1 as it is not considered a prime
    i=1
    while i<=n:
        i+=1
        
        #checking divisibility
        if n%i==0:

            #checking if divisible number found is a perfect square or not
            root=i**(1/2)
            if root==int(root):
                return 0

            #checking if number is prime or not (we can not use dynamic programming and store primes found as we are only calculating those primes that devide n, not all primes. This will result in incorrect classification)
            isprime=True
            k=1
            while k<i:
                k+=1
                if i%k==0:
                    isprime=False
                    break
            
            if isprime:
                count+=1

    #checking if number of primes found is even or odd
    if count%2==0:
        return 1
    else:
        return -1            


#testing
for i in [1, 2, 3, 4, 5, 6, 8, 10, 12, 30, 60, 210, 2310, 900, 997]:
    print(f'input: {i}, output: {mobius(i)}')

#runtime calculation
n = int(input('enter number: '))
import timeit
runtime=timeit.timeit('mobius(n)', globals=globals(), number=1000000)
print('average runtime:', runtime/1000000)



#counting steps
steps = 0
def mobius(n):
    global steps

    count=0
    steps+=1
    
    i=1
    steps+=1

    while i<=n:
        steps+=2

        i+=1
        steps+=2

        steps+=2
        if n%i==0:
            steps+=1

            root=i**(1/2)
            steps+=2

            steps+=1
            if root==int(root):
                steps+=1

                steps+=1
                return 0
            
            isprime=True
            steps+=1

            k=1
            steps+=1

            while k<i:
                steps+=2

                k+=1
                steps+=2

                steps+=1
                if i%k==0:
                    steps+=1

                    isprime=False
                    steps+=1

                    steps+=1
                    break
            
            if isprime:
                steps+=1

                count+=1
                steps+=1
    steps+=2
    if count%2==0:
        steps+=1

        steps+=1
        return 1
    else:

        steps+=1
        return -1

mobius(n)
print('Steps:', steps)