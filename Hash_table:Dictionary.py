age_dict = {'Emily': 32,
            'Tom': 43}
age_dict['Tom'] = 33
age_dict['George'] = 22


#takes constant amount of time to change/add entries O(1)

if 'George' in age_dict:
    print("Hurray")
else:
    print("BOOO")

myList = ["George", "Tom", "Emily", "Jenny", "Tom"]


def appears_twice(given_list):
    myDict ={}
    for element in given_list:
        myDict[element] = 0;
    for element in given_list:
        myDict[element] +=1;
    for name in myDict:
        if myDict[name] > 1:
            return name
        else:
            return ""
print(appears_twice(myList))

num_list = [5, 5, 1, 0, 9]

def pair_sum_10(given_list):
    myDict = {}
    for element in given_list:
        myDict[element] = 0
    for element in given_list:
        myDict[element] +=1    
    print(myDict)
    
    for num in myDict:
        if 10-num in myDict:
            if 10-num == num and myDict[num] == 2:
                return (num, 10-num)
            elif 10-num!= num:
                return (num, 10-num)
            else:
                continue
    return "No pair found"

print(pair_sum_10(num_list))
    
    
