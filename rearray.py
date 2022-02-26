from turtle import right


n = int(input())
array = list(map(int,input().split())) 
length = len(array) #8
left = 0
right = length-1

for i in range(length):
    while left<=right:
        mid = (left+right)//1
        if array[mid] == array[i]:
            print(mid+1)
            break
        elif array[mid]>array[i]:
            right = mid-1
        else :
            left = mid+1








2 4 5 1 7 6 3 8
0 1 0 2 2 1 2 0
#자신 숫자보다 작은 숫자의 개수를 출력하는것
