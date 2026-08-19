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
