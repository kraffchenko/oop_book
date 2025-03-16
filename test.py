ean = str(input("Write your code: "))
sum = 0
counter = 1
for num in range(0, len(ean)-1):
    print(ean[num])
    if counter % 2 != 0:
        print('1')
        print('\n\n')
        sum += int(ean[num]) * 1
    else:
        sum += int(ean[num]) * 3
        print('2')
        print('\n\n')
    counter +=1
sum = sum % 10
sum = 10 - sum
print(sum)
if str(sum) == ean[12]:
    print("True")
else:
    print("False")
