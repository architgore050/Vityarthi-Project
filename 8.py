def mean_of_digits(n):
    if n>=0:
        digits=[int(digit) for digit in str(n)]
    else:
        digits=[int(digit) for digit in str(-n)]
    
    #sum(digits)
    sum=0
    for digit in digits:
        sum+=digit
    
    #len(digits)
    length=0
    for digit in digits:
        length+=1
    
    return sum/length

#testing
for i in [0, 5, 12, 123, 1111, 9876, 9, 1234567890, -123]:
    print(f'mean of digits of {i} is {mean_of_digits(i)}')

#runtime claculation
import timeit
n=int(input('enter number: '))
runtime = timeit.timeit('mean_of_digits(n)', globals=globals(), number=10**6)
print(f'average runtime for n={n}: {runtime/10**6} seconds')

#counting steps
steps=0

steps+=1
if n>=0:
    steps+=1

    digits=[int(digit) for digit in str(n)]
    steps+=len(digits)*3+1
else:
    digits=[int(digit) for digit in str(-n)]
    steps+=len(digits)*3+1

#sum(digits)
sum=0
steps+=1

for digit in digits:
    steps+=1

    sum+=digit
    steps+=2

#len(digits)
lenght=0
steps+=1

for digit in digits:
    steps+=1

    lenght+=1
    steps+=1

output = sum/lenght
steps+=1

print(f'number of steps performed for n={n}: {steps}')