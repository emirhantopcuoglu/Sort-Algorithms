arr = [5,2,4,6,1,3]
print("Sıralama öncesi:",arr)

for i in range(1,len(arr)):
  key = arr[i]
  j = i - 1
  while j >= 0 and arr[j] > key:
    arr[j+1] = arr[j]
    j -= 1
  arr[j+1] = key

print("Sıralama sonrası: ",arr)