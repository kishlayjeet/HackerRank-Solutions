import numpy

N, M = map(int, input().split())
lst = []
for i in range(N):
    lst += list(map(int, input().split()))
arr = numpy.reshape(lst, (N, M))
print(numpy.max(numpy.min(arr, axis=1)))