#https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
def dirReduc(arr):
    skip = False
    while True:
        unmodified = True
        arr.append('buffer')
        for i in range(0,len(arr)):
            if i == 0:
                skip = False
            if skip == False:
                if arr[i] == 'NORTH' and arr[(i+1)] == 'SOUTH':
                    arr[i] = 'remove'
                    arr[i+1] = 'remove'
                    skip = True
                    unmodified = False
                elif arr[i] == 'EAST' and arr[(i+1)] == 'WEST':
                    arr[i] = 'remove'
                    arr[i+1] = 'remove'
                    skip = True
                    unmodified = False
                elif arr[i] == 'SOUTH' and arr[(i+1)] == 'NORTH':
                    arr[i] = 'remove'
                    arr[i+1] = 'remove'
                    skip = True
                    unmodified = False
                elif arr[i] == 'WEST' and arr[(i+1)] == 'EAST':
                    arr[i] = 'remove'
                    arr[i+1] = 'remove'
                    skip = True
                    unmodified = False
            else:
                skip = False
        arr.remove('buffer')
        arr_read = arr.copy()
        for remove_find in arr_read:
            if remove_find == 'remove':
                arr.remove('remove')
        if unmodified == True:
            return arr
