foreigners = ['Abigail', 'Hokusai', 'MHXX', 'Yang', 'Voyager', 'Gogh']
for f in foreigners:
    print(f, len(f))

for i in range(5):
    print(i)

print(sum(range(4)))

for n in range(2, 100):
    for i in range(2, n):
        if n % i == 0:
            print(n, '=', i, '*', n // i)
            break
    else:
        print(n, "is a prime number.")
