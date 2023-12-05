f = open("input.txt", "r")

lines = f.readlines()



test_line = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"

def forwardfunc(s):
  for i in range(len(s)):
    if s[i].isdigit():
      return str(s[i])



def splitfunc(s):
    return s.split(":")[1].split(";") 


print(splitfunc(test_line))
