import sys
sys.stdin = open('4358.txt')

tree_dict = {}
total = 0
while True:
  try:
    tree = input()
    total += 1
    if tree in tree_dict:
      tree_dict[tree] += 1
    else:
      tree_dict[tree] = 1
  except:
    break
result = sorted(tree_dict.items())
for name, number in result:
  print("%s %.4f" % (name, number / total * 100))
