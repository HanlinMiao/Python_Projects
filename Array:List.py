a = [1, 2, "this is not a numebr"]
print(len(a))
#iteration method
#for element in a

for i in range(len(a)):
    print(a[i]);
    
b_list = [0, 0, 0]
b_list[1] = 1
print(b_list)

c_list = ["item0", "item1", "item2"]

for i in c_list:
    print(i)

e_list = [32, 55, 710, 1]
sum = 0

for i in e_list:
    sum += i
print(sum)

num_list = [1,3,4,5,5,5]

def second_largest(a):
    if len(a) == 0 or len(a) == 1:
        return None
    elif len(a) == 2:
        return min(a[0], a[1])
    else:
        num1 = max(a);
        num2 = min(a);
        for i in range(len(a)):
            if a[i] >= num2 and i != a.index(num1):
                num2 = a[i]
        return num2
print(second_largest(num_list))
    
