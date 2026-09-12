'''
Pattern 1 :

for i in range(1, 6):
  for j in range(1, 6):
    print(j, end=" ")
  print()
'''

'''
Pattern 2:

for i in range(1, 6):
  for j in range(1, 6):
    if j<=i:
      print("*", end=' ')
  print()
'''

'''
Pattern 3:

for i in range(1, 5):
  for j in range(i, 0, -1):
    print(j, end=" ")
  print(sep="\n")
'''