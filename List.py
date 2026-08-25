# 1 Print all elemnts of list
 num=[10,20,30,40,50]
 print(num[:])
 OR
for i in range(len(num)):
  print(num[i])

# 2 Even Or Odd numbers from given list 
 num=[10,20,30,40,50,7,9,13]
for i in range(len(num)):
    if num[i] %2==0:
       print("even no are:",num[i])
    else:
       print("no are odd",num[i])
      
# 3 Find sum of all elemnets
num=[10,20,30,40,50]
sum=0
for i in range(num[i]):
  sum=sum+num[i]
print(sum)

# search element 
num=[10,20,30,40,50]
target=30


# Search element in list 
num = [10, 20, 30, 40, 50]

target = 30
found = False
for i in range(len(num)):
    if num[i] == target:
        print("Element found at index", i)
        found = True
        break
if found == False:
    print("Element not found")

# Count even odd numbers 
num = [10, 20, 30, 40, 50, 7, 9, 13]

even = 0
odd = 0

for i in range(len(num)):
    if num[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers:", even)
print("Odd numbers:", odd)


## Find Missing Number in list
num = [1, 2, 3, 5]
n = 5
for i in range(1, n + 1):
    if i not in num:
        print("Missing number:", i)



## Find Duplicate Element from list
num = [10, 20, 10, 30, 20, 40]
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] == num[j]:
            print("Duplicate:", num[i])


## Remove Duplicate Elemnt from list
num = [10, 20, 10, 30, 20, 40]
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] == num[j]:
            num.remove(num[j])
print(num)




## Find SecondMax from list
num = [10, 20, 30, 40, 60, 40]
maxi = num[0]
for i in range(len(num)):
    if num[i] > maxi:
        maxi = num[i]
secondMax = num[0]
for i in range(len(num)):
    if num[i] != maxi and num[i] > secondMax:
        secondMax = num[i]

print("Maximum:", maxi)
print("Second Maximum:", secondMax)


## Find Two Sum in list
num = [10, 20, 38, 90]
target = 38
for i in range(len(num)):
    for j in range(len(num)):
        if num[i] + num[j] == target:
            print(num[i], num[j])



## Move All Zeros
num = [1, 0, 4, 5, 0, 8, 9]
for i in range(len(num)):
    if num[i] == 0:
        for j in range(i + 1, len(num)):
            if num[j] != 0:
                num[i] = num[j]
                num[j] = 0
                break
 print(num)



## Print Comman element from two list
num1=[10,20,30,40]
num2=[20,30,11,70]
for i in range(len(num1)):
    for j in range(len(num2)):
        if num1[i]== num2[j]:
            print("comman element from both list",num1[i])


## Merge two list
num1 = [10, 20, 30]
num2 = [40, 50, 60]
num3 = []
for i in range(len(num1)):
    num3.append(num1[i])
for j in range(len(num2)):
    num3.append(num2[j])
print(num3)

OR
num1 = [10, 20, 30]
num2 = [40, 50, 60]
num3 = num1 + num2
print(num3)




##Maximum subarray sum
num = [10, 20, -4, 5, -2, 8, 9]
max_sum = 0
for i in range(len(num)):
    current_sum = 0
    for j in range(i, len(num)):
        current_sum = current_sum + num[j]

        if current_sum > max_sum:
            max_sum = current_sum
print("Maximum subarray sum:", max_sum)




