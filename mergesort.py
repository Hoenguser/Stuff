
def mergesort(arr):
    if len(arr) > 1:
        middle = len(arr) //2
        sub_1 = arr[:middle]
        sub_2 = arr[middle:]
    
        mergesort(sub_1)
        mergesort(sub_2)
    
        i = j = k =0

        while i < len(sub_1) and j < len(sub_2):
            if sub_1[i] < sub_2[j]:
                arr[k] = sub_1[i]
                i += 1
            else:
                arr[k] = sub_2[j]
                j += 1
            k += 1

        while i < len(sub_1):
            arr[k] = sub_1[i]
            i += 1
            k += 1
        while j < len(sub_2):
            arr[k] = sub_2[j]
            j += 1
            k += 1


arr = [10, 9, 2, 6, 4, 13]
mergesort(arr)
print(arr)