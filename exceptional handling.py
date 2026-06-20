# Exceptional handling 
# a = 10
# b =0
# print(a/b)

# try :- jaha error aa sakte hai 
# catch :- error handle karta hai
# finally :-hamesha chalega 
# else:- jab error nhi atha tab chalega 
# raise :- manually throw an exceptional

# e.g
# try:
#     num = int(input("enter  "))
#     print(10/num)
# except ValueError:
#     print("number sahi enter kari")
# except ZeroDivisionError:
#     print("Zero se divide nhi hota")

# def func():
#     print("hello") #no indentation

# print("start")  acche se cahle ga 
# print(10/0) errorzero
# print("End") end program



# file handling 
# r = read
# w = write
# a = append
# x = new file cfreate kar ne ka liya 

# read ki file
# f = open(".txt","r")
# print(f.read())
# f.close()

# write kar na ha 
# f = open(".txt","w")
# f.write("hello i am in the file ")
# f.close()

# # append 
# f = open(".txt","a")
# f.write("\n new line Add")
# f.close()


# try :
#     with open(".txt","r") as f :
#         print(f.read())
# except FileExistsError:
#     print("file nhi h ap ki ")


# project 
# file ko craete kar na 
# file ko open kar ka dekhn na 
# file ko del kar na 
# file ko rename kar na 
# file ka anadar pura del kar ka new chiz chal na 
# file ,a add kar na 