from random import random

import random

if __name__ == "__main__":
      n = int(input("Enter N: "))
      print(f'Size: {n}')
      l = []
      for i in range(n):
          if 0 < i < n-1:
              s = '_'
              for j in range(1, n-1):
                  s += '*' if random.random() >= 0.75 else '_'
              s += '_'
              l.append(s)
          else:
              l.append('_' * n)

      for line in l:
          print(line)