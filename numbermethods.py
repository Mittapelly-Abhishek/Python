# 1.abs() --  it returns always positive values
# num=-60
# print(abs(num)) #60

# without method logic
# if num>0:
#     print(num)
# else:
#     print(num*-1)

# 2.round(x)
# print(round(8.698,0)) #9.0
# print(round(8.69,1)) #8.7
# print(round(8.65,1)) #8.7
# print(round(8.61,1)) #8.6
# print(round(8.955,2))#8.96

# 3.pow(x, y) -- x raised to the power y 
# print(pow(2,4)) #16              -- (base,power)
# print(pow(2,-4)) #0.0625

#4.divmod(x,y)  returns (quotient, remainder)
# print(divmod(10,5)) #(2,0)
# print(divmod(22,4)) #(5,2)

#5.int(x)
# print(int(5.9))         # Output: 5

#6.float(x)
# print(float(3))         # Output: 3.0

#7.complex()
# print(complex(2, 3))    # Output: (2+3j)

#8.str(x)
# print(str(30.46))       #"30.46"

#9.bin(x) #number to binary value
print(bin(1))  #0b1
print(bin(3)) #ob11

#10.hex(x) #number to hexadecimal
print(hex(2))  #0x2

# 11.oct(x) #number to octal
print(oct(2))  #0o2

#12.isinstance(parameter,datatype) #check varaible type
print(isinstance(4.5,float)) #true
print(isinstance("",str))    #true

#13.type() #retuns the data type
print(type(""))    #<class 'str'>
print(type(3+5j))  #<class 'complex'>
 
#14. max() and min()  # Find largest/smallest value
print(max(3, 10, 7))  # 10
print(min(3, 10, 7))  # 3

# 7. sum() # Adds all values in an iterable (like list)
print(sum([1, 2, 3])) 


