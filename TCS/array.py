#Find the maximum element in an array:
arr=[10,20,30,40,50]
def find_max(arr):
    max_val=arr[0]
    for num in arr:
        if num>max_val:
            max_val=num

    return max_val
print(find_max(arr))

#find the minimum element in an array:
arr=[10,20,30,40,50]
def find_min(arr):
    min_val=arr[0]
    for num in arr:
        if num<min_val:
            min_val=num

    return min_val
print(find_min(arr))

#find the sum of elemets in an array:
arr=[20,30,40,56]
def find_sum(arr):
    total=0
    for num in arr:
        total=total+num    #total+=num
    return total
print(find_sum(arr))    

#check prime number:
#using for loop:
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("enter the number:"))
if is_prime(n):
    print("prime number")
else:
    print("not a prime number")

#using fro loop with different method
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input("enter the number:"))
if is_prime(n):
    print("prime number")
else:
    print("not a prime number")

#using while loop:
def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True    
n=int(input("enter the number:"))
if is_prime(n):
    print("prime number")
else:
    print("not a prime number")

#check if array is sorted :
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True    
arr=[1,2,3,4]
print(is_sorted(arr))

#Find missing number 1to N
def missing_number(arr, N):
    expected = N * (N + 1) // 2
    return expected - sum(arr)

arr = [1, 2, 3, 5]
N = 5
print("missing_number:", missing_number(arr,N))

#find the element appearing once(XOR):
def single_number(arr):
    ans = 0
    for num in arr:
        ans ^= num
    return ans

arr = [2, 3, 2, 4, 4]
print(single_number(arr))
