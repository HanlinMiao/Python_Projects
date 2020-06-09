a = [[1, 3, 9, 4],
     [5, 0, 8, -3]]
for row in a:
    for element in row:
        print(element)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
b = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

def diagnol_sum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i][i]
    return sum

print(diagnol_sum(b))

board = [[0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 0],
         [0, 1, 0, 1]]
def rooks_are_safe(chess):
    for i in range(len(chess)):
        num1 = 0
        num2 = 0
        for j in range (len(chess[i])):
            if chess[i][j] == 1:
                num1+=1
            if chess[j][i] == 1:
                num2+=1
            if num1 == 2 or num2 == 2:
                return False
    return True
print(rooks_are_safe(board))

a_2d = [[-9, -8, -1, 1],
        [-8, -7, 1, 2],
        [-7, -6, 2, 3],
        [-6, -5, 4, 5],
        [-5, -5, 5, 6]]
def find_negative (array_n2):
    count = 0
    for i in range(len(array_n2)):
        for j in range (len(array_n2[i])):
            if array_n2[i][j]< 0:
                count += 1
    return count
print (find_negative(a_2d))



def find_negativeN (array_n):
    count  = 0
    num = len(array_n[0])-1;
    for i in range(0,len(array_n), 1):
        for j in range (num, -1, -1):
            print(array_n[i][j])
            if array_n[i][j] < 0:
                count += j+1
                num = j
                break
    return count
print(find_negativeN(a_2d))
