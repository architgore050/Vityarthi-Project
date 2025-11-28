def crt (remainders, moduli):
    #makign sure gcd of all moduli is 1
    l = 0
    for m in moduli:
        l+=1
    if l>1:
        lowest_m = moduli[0]
        for m in moduli[1:]:
            if m<lowest_m:
                lowest_m=m
        i=2
        while i<=lowest_m/2:
            for j in moduli:
                devides_all = True
                if j%i != 0:
                    devides_all = False
                    break
            if devides_all:
                return None
            i+=1
    
    #solving
    capital_M = 1
    for m in moduli:
        capital_M*=m
    
    m_s = []
    for m in moduli:
        m_s.append(capital_M/m)
    
    m_inv_s = []
    l=0
    for i in remainders:
        l+=1
    i=0
    while i < l:
        a = m_s[i]
        m = moduli[i]
        if a==m:
            return None                     #x can never be an integer
        if a==0:
            return None                     #condition will never be satisfied regardless of x and deviding by 0 will not work
        if m==0:
            return None                     #condition will never be satisfied regardless of x
        if a>m:
            s=m
        else:
            s=a
        j = 2
        while j <= s/2:
            if a%j == 0 and m%j == 0:
                return None                 #GCD of a and m has to be 1 otherwise x will never be an integer
            j+=1
        k=0
        while True:
            x = (k*m+1)/a
            if x==int(x):
                m_inv_s.append(x)
                break
            k+=1
        i+=1
    
    total = 0
    i=0
    while i<l:
        total+=remainders[i]*m_s[i]*m_inv_s[i]
        i+=1   
    return total%capital_M

#testing
test_cases = [([1, 2], [3, 5]), ([2, 3], [3, 4]), ([5, 7], [11, 13]), ([1, 4, 6], [5, 7, 8]), ([2, 3], [4, 6]), ([7], [12]), ([0, 3], [4, 5]), ([123456, 987654], [1000003, 1000033])]
for test_case in test_cases:
    print(f"crt{test_case} =", crt(test_case[0], test_case[1]))

#runtime
a = eval(input("Enter remainders (list form): "))
m = eval(input("Enter moduli (list form): "))
print("Result =", crt(a, m))
import timeit
runtime = timeit.timeit("crt(a, m)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
crt(a, m)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
def crt_stepsCounter (remainders, moduli):
    l = 0
    steps=1
    for m in moduli:
        steps+=1

        l+=1
        steps+=2

    steps+=1
    if l>1:

        lowest_m = moduli[0]
        steps+=2

        steps+=1
        for m in moduli[1:]:
            steps+=1

            steps+=1
            if m<lowest_m:

                lowest_m=m
                steps+=1

        i=2
        steps+=1

        steps+=2
        while i<=lowest_m/2:
            steps+=2

            for j in moduli:
                steps+=1

                devides_all = True
                steps+=1

                steps+=2
                if j%i != 0:
                    steps+=2

                    devides_all = False
                    steps+=1

                    steps+=1
                    break
            
            steps+=1    
            if devides_all:

                steps+=1
                return steps
            
            i+=1
            steps+=2
    
    #solving
    capital_M = 1
    steps+=1

    for m in moduli:
        steps+=1

        capital_M*=m
        steps+=2
    
    m_s = []
    steps+=1

    for m in moduli:
        steps+=1

        m_s.append(capital_M/m)
        steps+=2
    
    m_inv_s = []
    steps+=1

    l=0
    steps+=1

    for i in remainders:
        steps+=1

        l+=1
        steps+=2
    
    i=0
    steps+=1

    steps+=1
    while i < l:
        steps+=1

        a = m_s[i]
        steps+=1

        m = moduli[i]
        steps+=1

        steps+=1
        if a==m:

            steps+=1
            return steps                     #x can never be an integer
        
        steps+=1
        if a==0:

            steps+=1
            return steps                     #condition will never be satisfied regardless of x and deviding by 0 will not work
        
        steps+=1
        if m==0:

            steps+=1
            return steps                     #condition will never be satisfied regardless of x
        
        steps+=1
        if a>m:

            s=m
            steps+=1

        else:
            steps+=1

            s=a
            steps+=1

        j = 2
        steps+=1

        steps+=2
        while j <= s/2:
            steps+=1

            steps+=5
            if a%j == 0 and m%j == 0:
                steps+=1

                steps+=1
                return steps                 #GCD of a and m has to be 1 otherwise x will never be an integer
            
            j+=1
            steps+=2

        k=0
        steps+=1

        while True:
            steps+=1

            x = (k*m+1)/a
            steps+=4

            steps+=2
            if x==int(x):
                steps+=1

                m_inv_s.append(x)
                steps+=1

                steps+=1
                break
            
            k+=1
            steps+=1

        i+=1
        steps+=1
    
    total = 0
    steps+=1

    i=0
    steps+=1

    steps+=1
    while i<l:
        steps+=1

        total+=remainders[i]*m_s[i]*m_inv_s[i]
        steps+=6

        i+=1
        steps+=2

    steps+=2
    return steps

print("Number ofr steps =", crt_stepsCounter(a, m))