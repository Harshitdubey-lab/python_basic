# # mainly there are 4 type of data structure 
# # 1. list ->> array [str, int, float, boolean]
# # 2. tuples -->  (1, 2, 3, 4)
# # 3. set --> {1,2,3}
# # 4. dictonary --> collection of {key: value} e.g {"name": "payal"}


# # list :--
# # 1. mutable --> creation yaha pr changes kiya j sak the h 
# # 2. duplication --> allow duplicate value 
# # 3. ordered --> [1,4,6,3]
# # fruits = ["mango", "banana", "chiku", 5]
# # print(type(fruits))
# # print(fruits[2])


# # number = [1,2,3,4,5,6,7,8,9,5]
# # print(number)
# # append() --> is use for adding the number in list but it can add at the last 
# # number.append(10)
# # print(number)
# # # insert(index,value) using index and value we can instert the number in the list
# # number.insert(2,5)
# # print(number)
# # # if we want to insert the multiple value so we use extend
# # number.extend([12,13,45,89])
# # print(number)
# #  Remove 
# # number.remove(8) # remove first occurance 
# # print(number)
# # # index 
# # value = number.index(4)
# # print(value)
# # # count --> 
# # val = number.count(1)
# # print(val)

# # n = [6,4,8,2,0,8] 
# # n.sort()
# # print(n)
# # n.reverse()
# # print(n)
# # print(n)
# # vale = n.copy()
# # print(vale)

# # # clear()
# # n.clear()
# # print(n)
# # print positive or negative elements of an list 
# # list = [10,-5,0,7,-3,8,-1]
# # print("positive number")
# # for i in list:
# #     if i > 0:
# #         print(i)
# # print("negative number ")
# # for i in list:
# #     if i < 0 :
# #         print(i)

# # # mean of list 
# # mean = sum(list)/len(list)
# # print("your mean is ", mean)

# # find the greatest element and there index vgalue 
# lst = [10,5, 6, 9, 1, 11]
# # max_val= max(lst)
# # # print(max_val)
# # index = lst.index(max_val)
# # print("Greatest number is ", max_val)
# # print("the index of max value is :",index)
# # max_vale=lst[0]
# # index = 0
# # for i in range(len(lst)):
# #     if lst[i]> max_vale:
# #         max_vale= lst[i]
# #         index = i
# # print("Greatest number is ", max_vale)
# # print("the index of max value is :",index)

# lst=[10,45,7,89,100] #[7,10,45,89,100]
# print("secound greast no. ",sorted(lst)[-2])



# tuples
# immutable :- you cant change the values of tuples
# dupication :- you can have duplicate Value
# ordered :- set ka form 
# heterogenous :-mixture of datatype int, str, bool, flooat

# tuples h vo string formt m hota h 
# t = (5,6,2,4,3,5)
# print(type(t))
# a=list(t)
# print(type(a))

# a = t.index(2)
# count_a= t.count(2)
# print(a)
# print(count_a)

# # mainly there are 4 type of data structure 
# # 1. list ->> array [str, int, float, boolean]
# # 2. tuples -->  (1, 2, 3, 4)
# # 3. set --> {1,2,3}
# # 4. dictonary --> collection of {key: value} e.g {"name": "payal"}


# # list :--
# # 1. mutable --> creation yaha pr changes kiya j sak the h 
# # 2. duplication --> allow duplicate value 
# # 3. ordered --> [1,4,6,3,4]
# fruits = ["mango", "banana", "chiku", 5]
# print(type(fruits))
# print(fruits[2])


# number = [1,2,3,4,5,6,7,8,9,5]
# print(number)
# append() --> is use for adding the number in list but it can add at the last 
# number.append(10)
# print(number)
# # # insert(index,value) using index and value we can instert the number in the list
# number.insert(2,5)
# print(number)
# # # if we want to insert the multiple value so we use extend
# number.extend([12,13,45,89])
# print(number)
# #  Remove 
# number.remove(1) # remove first occurance 
# print(number)
# # # index 
# value = number.index(4)
# print(value)
# # # count --> 
# val = number.count(5)
# print(val)

# n = [6,4,8,2,0,8] 
# n.sort()
# print(n)
# n.reverse()
# print(n)
# print(n)
# vale = n.copy()
# print(vale)

# clear()
# n.clear()
# print(n)
# # print positive or negative elements of an list 
# list = [10,-5,0,7,-3,8,-1]
# print("positive number")
# for i in list:
#     if i > 0:
#         print(i)
# print("negative number ")
# for i in list:
#     if i < 0 :
#         print(i)

# mean of list 
# mean = sum(list)/len(list)
# print("your mean is ", mean)

# find the greatest element and there index vgalue 
# lst = [10,5, 6, 9, 1, 11]
# max_val= max(lst)
# # print(max_val)
# index = lst.index(max_val)
# print("Greatest number is ", max_val)
# print("the index of max value is :",index)
# max_vale=lst[0]
# index = 0
# for i in range(len(lst)):
#     if lst[i]> max_vale:
#         max_vale= lst[i]
#         index = i
# print("Greatest number is ", max_vale)
# print("the index of max value is :",index)

# lst=[10,45,7,89,100] #[7,10,45,89,100]
# print("secound greast no. ",sorted(lst)[-2])



# tuples
# immutable :- you cant change the values of tuples
# dupication :- you can have duplicate Value
# ordered :- set ka form 
# heterogenous :-mixture of datatype int, str, bool, flooat

# # tuples h vo string formt m hota h 
# t = (5,6,2,4,3,5) # list diiff[]
# print(type(t)) # tuple
# a=list(t)
# print(type(a)) # list

# a = t.index(4)
# count_a= t.count(5)
# print(a)
# print(count_a)


# set is the collection same data 

# mutable :- chances kiya j sak the h 
# duplicate :- no duplicate 
# unordered :- 
# heterogenous :- 
# hash() 
# set dont have there index 
# s ={1,2,3}
# s.add(4)
# s.remove(2)
# s.clear()
# print(s)

# A= {1,2,3}
# B = {3,4,5}
# union_set =A.union(B)
# print(union_set)
# intrestion_set=A.intersection(B)
# print(intrestion_set)
# differnce_set = A.difference(B)
# print(differnce_set)
# symm = A.symmetric_difference(B)
# print(symm)


# dictionary :- it is a collection key(unique) and value (value can be repeat)
# mutable : - 
# dupication :-
# order :- index is not required unique value can be access 
# heterogeous :-

# Systax 
# student = {"Name": "aditiya", "age":12}
# # print(type(student))
# print(student["Name"])


# number = {"A": "aditya","B": "Ayush","C":"harsh"}
# for i in number:
#     print(i,":",number[i])
