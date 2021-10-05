def Main()
count=5
for i in range(0,count):
    for j in range(i,n+1):
        for k in range(j,n+1):
            print(count)


"""
count=5, 1 unit, 1 time
i = 0,1,2,3,4,   5 times

1] j=0,1,2,3,4,  5 times
2] j=1,2,3,4     4 times
...
5] j=4,          1 time

for j loop= n*(n-1) times

1] k=0,1,2,3,4,  5 times
2] k=1,2,3,4     4 times
...
   for k loop= n*(n-i-j)times

   T(n) = n*n+  n*n*n + n + c
   T(n)=O(n^2+n^3+n)+c
   T(n)=O(n^3)
"""