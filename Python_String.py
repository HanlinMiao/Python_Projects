#python string is immutable

s = "abc"

for character in s:
    print(character)
    
for i in range (len(s)):
    print(s[i])

a_string  ="ABC"

def are_reverses(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    for i in range(len(string_1)):
        if string_1[i] != string_2[len(string_2)-i-1]:
           return False
    return True;
           
print(are_reverses("yeet", "hell"))


def larger_than(str1, str2):
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if(str1[i] > str2[i]):
               return str1
            elif(str1[i] < str2[i]):
                return str2
            else:
                continue
    else:
        if len(str1) > len(str2):
            return str1
        else:
            return str2
print(larger_than("1221", "123"))
