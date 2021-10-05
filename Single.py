##Single FOR loop
Sum(A,n) 
{
    total =0               ## 1 unit,  no of times=1
    for i in range(0,n)    ## 2 units,  no of times=n+1 
        sum = sum + A[i]   ##  2 untis  no of times=n 
    return sum             ## 1 unit  no of times=1
} 

##T(Sum)=1 + 2 * (n+1) + 2 * n + 1 
##T(Sum)=4n + 4 =C1 * n + C2 = O(n)

