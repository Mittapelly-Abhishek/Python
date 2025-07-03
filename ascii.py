#checking the character is lowercase or uppercase or number

def check_char(char):
    ascii_val=ord(char)

    if 97 <= ascii_val <= 122: #
        return "lowercase"
    elif 65 <= ascii_val <= 90:
        return "uppercase"
    elif 48 <= ascii_val <= 57:
        return "number"
    
    return "special character"

s=input("enter a charcter :")
print("the character is in ",check_char(s))


#function to convert vowel character into next character(Abhi - Bbhj)

def convert_vowel(word):
    result=""
    for ch in range(len(word)):
        s=word[ch]
        char=ord(s)
        if s in "aeiouAEIOU":
            result+=chr(char+1)
        else:
            result+=s
    return result

string=input("enter a word :")
print(convert_vowel(string))
