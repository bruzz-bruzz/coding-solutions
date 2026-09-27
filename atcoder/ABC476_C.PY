import heapq
n = int(input())
arr = [int(x) for x in str(input()).split(" ")]
h = arr[:3]
heapq.heapify(h)
print(h[0])
for x in arr[3:]:
    heapq.heappush(h,x)
    heapq.heappop(h)
    print(h[0])