n = int(input("enter the value :- "))
for i in range(1,n+1):
    # print(i)
    # print('#'*i)
    print(" "*(n-i)+"#"*(2*i-1))
# for row in range(1,n+1):
#     for col in range(1, n*2):
#         if (col>=n-row+1)and (col<=n+row-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()