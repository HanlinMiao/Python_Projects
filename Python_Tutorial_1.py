print("Hello World")
print("more string")
print(3)

a = 1

print(a);

def sleep_in(weekday, vacation):
    work = False;
    if(weekday == False or vacation == True):
        return True;
    else:
        return False;

print(sleep_in(True, False));

def string_times(word, num):
    sentence = "";
    rep = num;
    for i in range(0, rep):
         sentence += word;
    
    print(sentence)

string_times("Yeet", 5);

def double_char(string):
    sentence = ""
    for i in string:
        sentence = sentence + 2 * i
    return sentence
print(double_char("Hi-There"))
