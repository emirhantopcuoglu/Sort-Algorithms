liste = [5,2,4,6,1,3]
def merge(arr):
    if len(arr) > 1:
        print("Parçalanan değerler " + str(arr))
        orta = len(arr) // 2
        leftArr = arr[:orta]
        rightArr = arr[orta:]
        merge(leftArr)
        merge(rightArr)
        mergeSort(arr,leftArr,rightArr)

def mergeSort(arr,leftArr,rightArr):
    i,j,k = 0,0,0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1
    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1
    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1
        print("Birleştirilmiş hali " + str(arr))

merge(liste)