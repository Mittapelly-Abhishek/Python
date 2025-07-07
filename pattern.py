#  S(rev)


# r=int(input("enter a number:"))
# mid=(r//2)+1
# for i in range(1,r+1):
#     pat=""
#     for j in range(1,r+1):
#         if i<=mid:
#             if i==1 or j==r or i==mid:
#                 pat+="*"+" "
#             else:
#                 pat+=" "+" "
#         else:
#             if j==15 or i==r:
#              pat+="*"+" "
#         else:
#             pat+=" "+" "
        
#     print(pat)


# E (rev)
# r=int(input("enter a number:"))
# for i in range(1,r+1):
#     pat=""
#     for j in range(1,r+1):
#         if i==1 or i==r or j==r or i==(r//2+1):
#             pat+="*"+" "
#         else:
#             pat+=" "+" "
#     print(pat)

# Alphabet Triangle Code:in alphabets

# row=int(input("enter a number :"))
# ch=65  #ASCII of A
# for  i in range(1,row+1):
#   pattern=""
#   for j in range(1,i+1):
#     pattern+=chr(ch) + " "
#     ch+=1
#   print(pattern)


# Alphabet Revrse Triangle Code:in ascii numbers

# row=int(input("enter a number :"))
# ch=65  #ASCII of A
# for  i in range(row,0,-1):
#   pattern=""
#   for j in range(1,i+1):
#     pattern+=chr(ch) + " "
#     ch+=1
#   print(pattern)