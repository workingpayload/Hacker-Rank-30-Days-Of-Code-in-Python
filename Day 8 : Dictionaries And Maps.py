x = int(input())
dic = {}

for i in range(x):
    text = input().split()
    dic[text[0]] = text[1]

while True:
   try:
    inpt = input()
    if inpt in dic:
        print(inpt + "=" + dic[inpt])
    else:
        print("Not found")
   except EOFError:
       break
