string_to_int = {
	"0" : 0,
	"1" : 1,
	"2" : 2,
	"3" : 3,
	"4" : 4,
	"5" : 5,
	"6" : 6,
	"7" : 7,
	"8" : 8,
	"9" : 9
    }
x = "4567";

def string_to_int_num(string):
	index = len(string);
	num = 0;
	for i in string:
		num = num + (string_to_int.get(i) * 10 **(index-1))
		index = index-1
		print(num);
		
	return num;
print(string_to_int_num(x));





