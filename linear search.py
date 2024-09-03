def linearsearch(a,key):
    n=len(a)
    for i in range(n):
        if a[i]==key:
            return i;
    return-1
a=[13,24,45,21,43,65,56,81,80]
print("The array elements are:",a)
k=int(input("Enter the key element to search:"))
i=linearsearch(a,k)
if i==-1:
      print("search unsuccessful")
else:
    print("search successful key found at location:",i+1)



