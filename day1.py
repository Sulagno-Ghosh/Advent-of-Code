f = open("input.txt", "r")
lines = f.readlines()
list = []

def forwardfunc(s):
  for i in range(len(s)):
    if s[i].isdigit():
      return str(s[i])


def backwordfunc(s):
  for i in range(len(s)-1,-1,-1):
    if s[i].isdigit():
      return str(s[i])



for i in range(len(lines)):

  a = forwardfunc(lines[i])
  b = backwordfunc(lines[i])

  result = a + b

  list.append(int(result))

  result = sum(list)



print(result)

