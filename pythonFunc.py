# taken from
# https://js-algorithms.tutorialhorizon.com/2015/10/19/find-consecutive-segments-in-an-sorted-array/
# by Kavit

def checkEvenlySpaced(arr):
    diff = arr[1] - arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] != diff:
            return False
    return diff

def compressArr(arr):
    start = arr[0]
    stop = start
    arrLength = len(arr)
    result = []

    for i in range(1, arrLength):
        if arr[i] == stop+1:
            stop = arr[i]
        else:

            if (start == stop):
                result += [start]
            else:
                result += [(start, stop)]
            start = arr[i]
            stop = start

    if (start == stop):
        result += [start]
    else:
        result += [(start, stop)]

    return result


arr = [1, 2, 3, 10, 25, 26, 30, 31, 32, 33]

compressArr(arr)
