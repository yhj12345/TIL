import sys
sys.stdin = open('7682.txt')

while True: 
  a = input()
  if a == 'end':
    break
  
  # flag가 True면 invalid 
  # flagrk False면 valid
  flag = False
  # O, X, .의 개수를 카운트
  o_count, x_count, dot_count = 0, 0, 0
  for i in a:
    if i == 'X':
      x_count += 1
    elif i == 'O':
      o_count += 1
    else:
      dot_count += 1
  
  # 만약에 (X의 개수 - O의 개수)가 0, 1이 아니면 invalid
  if x_count - o_count > 1 or x_count - o_count < 0:
    flag = True

  # 게임이 끝나는 모든 경우의 수
  arr = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

  # O, X가 3개를 모앗는가
  # True면 모앗다
  o_flag = False
  x_flag = False
  for i in arr:
    if a[i[0]] == a[i[1]] == a[i[2]]:
      if a[i[0]] == 'O':
        o_flag = True
      elif a[i[0]] == 'X':
        x_flag = True
  
  # 게임판이 다 안찻는데 둘 다 3개를 못모앗으면 invalid
  if dot_count != 0:
    if o_flag == False and x_flag == False:
      flag = True
  
  # O가 이겻는데 X의 카운트가 많을수가 없다
  if o_flag == True and x_flag == False:
    if x_count > o_count:
      flag = True
  
  if o_flag == False and x_flag == True:
    if x_count == o_count:
      flag = True
  
  if o_flag == True and x_flag == True:
    flag = True
  if flag == False:
    print('valid')
  else:
    print('invalid')
