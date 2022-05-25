# метод сортировки блоками (недоделан)

import os
os.system('cls')

arr = [79,5,3,4,9,7,5,3,6,70]
print(arr)
middle = int(len(arr)/2)
max = int(len(arr))

indmin = 0
indmax = len(arr)-1
l = arr[indmin]
r = arr[indmax]

s = arr[middle]
print (l,s,r)


if l > r:
    temp = l 
    print (temp)
    arr[indmin] = r
    arr[indmax] = temp   
print(arr)

indmin+=1
indmax+=1