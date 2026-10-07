result = str(bin(int(input())))   
count = 0
for i in result:
    if i == '1': count += 1
print(count)