import re

string = """
yMoDsrwltV
7nQl6iyVRW
pvtOdYA8uX
w13rbQuuMF
n4eFpYABqR
jz65TB2ojt
bp77OORmp1
m7eFj6fWTT
xpH2KkHRHP
F2kkw9G3JN
"""

def findNums(s):
    ans = []
    for line in s.splitlines():
        print(f"line: {line}")
        if line.strip():
            digits = re.findall(r"\d", line)
            # find individual digits
            if digits:
                print(f"digits: {digits}")
                ans.append(int("".join(digits)))  # join into one number
    return ans

print(findNums(string))
