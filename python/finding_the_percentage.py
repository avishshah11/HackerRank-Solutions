
x = int(input())
dict = {}
for i in range(0, x):
	inputarray = input().split()
	marks = list(map(float, inputarray[1:]))
	dict[inputarray[0]] = sum(marks)/float(len(marks))
print("%.2f"% dict[input()])	