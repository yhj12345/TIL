# import sys
# sys.stdin = open('2174.txt')

# A, B = map(int, input().split())
# N, M = map(int, input().split())

# arr = [[[] for _ in range(A)] for _ in range(B)]
# robot_dir = {}
# for i in range(N):
#   a, b, c = input().split()
#   arr[int(b)-1][int(a)-1].append(i+1)
#   if c == 'E':
#     robot_dir[i+1] = 0
#   elif c == 'S':
#     robot_dir[i+1] = 1
#   elif c == 'W':
#     robot_dir[i+1] = 2
#   elif c == 'N':
#     robot_dir[i+1] = 3

# result = ''
# for _ in range(M):
#   a, b, c = input().split()
#   a = int(a)
#   c= int(c)

#   if b == 'R':
#     for r in range(int(c)):
#       robot_dir[a] = (robot_dir[a] + 1) % 4
#   elif b == 'L':
#     for l in range(int(c)):
#       robot_dir[a] = (robot_dir[a] - 1) % 4
#   elif b == 'F':
#     x, y = 0, 0
#     for i in range(A):
#       for j in range(B):
#         if int(a) in arr[j][i]:
#           x, y = i, j
#           arr[y][x].pop()
#           break
#     for _ in range(int(c)):      
#       if robot_dir[a] == 0:
#         x += 1
#         if x >= A:
#           result = f'Robot {a} crashes into the wall'
#           break
#         elif len(arr[y][x]) != 0:
#           result = f'Robot {a} crashes into robot {arr[y][x][0]}'
#           break
#         else:
#           arr[y][x].append(a)
#           break
#       elif robot_dir[a] == 1:
#         y -= 1
#         if y < 0:
#           result = f'Robot {a} crashes into the wall'
#           break
#         elif len(arr[y][x]) != 0:
#           result = f'Robot {a} crashes into robot {arr[y][x][0]}'
#           break
#         else:
#           arr[y][x].append(a)
#       elif robot_dir[a] == 2:
#         x -= 1
#         if x < 0:
#           result = f'Robot {a} crashes into the wall'
#           break
#         elif len(arr[y][x]) != 0:
#           result = f'Robot {a} crashes into robot {arr[y][x][0]}'
#           break
#         else:
#           arr[y][x].append(a)
#           break
#       elif robot_dir[a] == 3:
#         y += 1
#         if y >= B:
#           result = f'Robot {a} crashes into the wall'
#           break
#         elif len(arr[y][x]) != 0:
#           result = f'Robot {a} crashes into robot {arr[y][x][0]}'
#           break
#         else:
#           arr[y][x].append(a)
#           break
#   if result != '':
#     print(result)
#     break
# else:
#   print('OK')

import sys
sys.stdin = open('2174.txt')

A, B = map(int, input().split())
N, M = map(int, input().split())

arr = [[0 for _ in range(A)] for _ in range(B)]
robot_dir = {}
for i in range(N):
  a, b, c = input().split()
  arr[int(b)-1][int(a)-1] = i+1
  if c == 'E':
    robot_dir[i+1] = 0
  elif c == 'S':
    robot_dir[i+1] = 1
  elif c == 'W':
    robot_dir[i+1] = 2
  elif c == 'N':
    robot_dir[i+1] = 3

result = ''
for _ in range(M):
  a, b, c = input().split()
  a = int(a)
  c= int(c)

  if b == 'R':
    for r in range(int(c)):
      robot_dir[a] = (robot_dir[a] + 1) % 4
  elif b == 'L':
    for l in range(int(c)):
      robot_dir[a] = (robot_dir[a] - 1) % 4
  elif b == 'F':
    x, y = 0, 0
    for i in range(A):
      for j in range(B):
        if arr[j][i] == a:
          x, y = i, j
    for _ in range(int(c)):      
      if robot_dir[a] == 0:
        x += 1
        if x >= A:
          result = f'Robot {a} crashes into the wall'
          break
        elif arr[y][x] != 0:
          result = f'Robot {a} crashes into robot {arr[y][x]}'
          break
        else:
          arr[y][x] = a
          arr[y][x-1]= 0
      elif robot_dir[a] == 1:
        y -= 1
        if y < 0:
          result = f'Robot {a} crashes into the wall'
          break
        elif arr[y][x] != 0:
          result = f'Robot {a} crashes into robot {arr[y][x]}'
          break
        else:
          arr[y][x] = a
          arr[y+1][x]= 0
      elif robot_dir[a] == 2:
        x -= 1
        if x < 0:
          result = f'Robot {a} crashes into the wall'
          break
        elif arr[y][x] != 0:
          result = f'Robot {a} crashes into robot {arr[y][x]}'
          break
        else:
          arr[y][x] = a
          arr[y][x+1]= 0
      elif robot_dir[a] == 3:
        y += 1
        if y >= B:
          result = f'Robot {a} crashes into the wall'
          break
        elif arr[y][x] != 0:
          result = f'Robot {a} crashes into robot {arr[y][x]}'
          break
        else:
          arr[y][x] = a
          arr[y-1][x]= 0
  if result != '':
    print(result)
    break
else:
  print('OK')
