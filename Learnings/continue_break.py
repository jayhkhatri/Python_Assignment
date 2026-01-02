# continue

# break
count =0
for num in range(10):
    if num % 3 == 0:
        continue
    if  count == 5:
        break
    count += 1

    print(num,count)
