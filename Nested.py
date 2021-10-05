def Main()
count=5                     
for i in range(0,count)     
    for j in range(i,n+1)   
    print(count)


##
##count=5, 1unit 1 time
##i=0,1,2,3,4,   5 times
##j=1,2,3,4,     4 times
##j=2,3,4,       3 times 
...              ...
##j=4,           1 time
##loop of j (n-1)* n times

##Time(n) = n*(n-1)+n+c
##Time(n) = n^2+n+c
##Time(n)=O(n^2)