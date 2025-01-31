# a=2
# b=4
# c=6
# print(max(a,b,c))

# if (a>b) and (a>c):
#     larest=a
# elif (b>c) and (b>a):
#     larest=b
# else:
#     larest=c
# print(larest)

# l=[1,3,4,5,99]
# k=0
# for i in l:
#     if i>k:
#         k=i
# print(k)
# print(type(2+3j))


# #sum of the digits
# test=list(input("enter a numbers"))
# b=0
# for i in test:
#     b+=int(i)
# print(b)


#reverse 
# r=list(str(721))
# b=r.reverse()
# print(b)

#factoral

# n=int(input("enter a number"))
# a=1
# for i in range(1,n+1):
#     a *=i
# print(a)

#middle character
# middle='Wonder'
# middle1=len(middle)
# b=middle1//2
# if middle1 % 2 == 0:
#     jk=middle[b+1 : b-1]
# else:
#     jk=middle[b]

# print(jk)

#first and middle number
# n=input("enter a number")
# g=''
# num=list(n)
# for i in num[1:-1]:
#     if (num[0]>i) and (num[-1]>i):
#         g='true'
#     else:
#         g='false'
# print(g)
units=40
bill=0
if units<=50:
    bill+=0
elif(units<=100):
    bill+=units*50
elif units<=150:
    bill+=units*100
elif units<=201:
    bill+=units*150
print(bill)
print('something')

    