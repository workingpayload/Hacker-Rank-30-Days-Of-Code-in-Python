# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(1, T + 1):
    S = input()
    print(S[0::2] + " " + S[1::2])



