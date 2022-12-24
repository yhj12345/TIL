import sys
from bisect import bisect_left
sys.stdin = open('9991.txt')
W, N = map(int, input().split())
word_list = list(input() for _ in range(W))

sotred_word_list = sorted(word_list)

for _ in range(N):
  K, K_word = input().split()
  word_Idx = bisect_left(sotred_word_list, K_word) + int(K) - 1
  if word_Idx < W:
    if sotred_word_list[word_Idx].startswith(K_word):
      print(word_list.index(sotred_word_list[word_Idx]) + 1)
    else:
      print(-1)
  else:
    print(-1)
  
  
  