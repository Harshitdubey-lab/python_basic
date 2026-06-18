# loop :- loops in py allow us to execute the block of code multiple time without rewritting it.
# ek kaam bar bar kar the ha conditional ka through uski place 
# loop 
# python 2 
# for  range(start,stop,step) stop -> n-1
# for i in range(2,21,3):
#     print(i) 

# a = "elephant"
# # for i in range(len(a)):
# #     print(a[i]) # length
# #     print(i) # indexing
# #     #index 0 to end
# for s in a:
#     print(s)

# for i in range() 

# Accept an integer and print hello world n time 
# a = int(input("enter the value :- ")) # 5
# for i in range(a):
#     print("hello world")

# for i in range(start,stop,steps):
# reverse for loop n to 1
# n = int(input("enter the value : "))
# for i in range(n,0,-1):
#     print(i)
# table 
# for i in range(1,11):
#     print(n, "x", i, "=",n*i)

# s = input("Enter the value") # user input
# rev = "" # reverse ko store kiya 
# for i in s: # 121 == 121
#     rev = i + rev # 2+1
# if s == rev: 
#     print("palindrome")
# else:
#     print("not palindrome ")
# while 
# when you dont know where to start and stop bas ap ka pass kya ho ek condition aagr ye condition par true ha jo andar jo bhe code likha ha vo kya run ho jae 
# systex 
# while (true):
# question
# seprate each digit of number and print it all the new line 
# n = int(input("enter the value :- "))
# while n > 0: # n >0 
#     print(n % 10) #123 % 10==
    
# gusessing game 
import random 
original = random.randint(1,10)
# print(original)
tries = 0
while True:
    tries +=1
    print(f"try---{tries}")
    guess = int(input("guess the number "))
    if original == guess :
        print("you won ")
        break
    elif (guess < original):
        print("go bit higher")
    elif (guess > original):
        print("go bit lower")




