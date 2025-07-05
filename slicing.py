# Write a fun to return the no of palindromes in the string

# def count_palindrome(s):
#     s=s.split(" ")
#     count=0
#     for i in s:
#         if i==i[::-1]:
#             count+=1
#             print(i) 
#     return count
# str1=input()
# total=count_palindrome(str1)

# if total>0:
#     print("Total : ",total)
# else:
#     print("no palindromes")

        
#chcek if palindrome in sentence
def check_palindrome(s):
    s=s.split(" ")
    for word in s:
        if word == word[::-1]:
            return "There are palindromes"
    return "No palindromes in sentence"

str1 = input("Enter a sentence: ")
print(check_palindrome(str1))























#slicing syntax [start : stop : step]

# word=input() #mahishmathi
# sub_str=input() #ishma
# sub_len=len(sub_str)
# for i in range(0,len(word)): #0,1,2,3,...n
#     part=word[i:i+sub_len]  #0:0+5=[::5],1:1+5=[1:6]
    
#     if part == sub_str:
#         print(part,"is in sentences")
#         break
#     else:
#         print(sub_str,"not in sentences")



            
           




