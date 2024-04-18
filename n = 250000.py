n = 250000
count = 0
b = 1250
while n> 0:
    n = n*1.0025-b
    b = b*0.9925
    count += 1
    if count % 1000 == 0:
        print("n", n)
        print("b", b)

print("count", count)