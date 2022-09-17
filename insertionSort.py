def insertionsort(arr):
  l = len(arr)
  s=arr[0]

  for i in range(1,l):

    if arr[i] < s:
      x = arr.pop(i)
      for j in range(0,i):
        if arr[j] > x:
          arr.insert(j,x)
          break
    s = arr[i]
    
  return arr

arr = [6,5,3,1,8,7,2,4]
print(insertionsort(arr))
