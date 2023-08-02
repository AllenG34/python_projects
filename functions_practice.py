#1
def hello():
    print('hello guys and girls')

#2
def letters(a,b,c):
    return[a,b,c]

#3
def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

hello()
print(letters("a","b","c"))
print(letters(1,2,3))
eat_lunch([])
eat_lunch(["Adobo"])
eat_lunch(["yogurt","pbj","milk","ice cream"])

"""
OUTPUT IN TERMINAL
$ python3 functions_practice.py
hello guys and girls
['a', 'b', 'c']
[1, 2, 3]
My lunchbox is empty!
First I eat Adobo
First I eat yogurt
Next I eat pbj
Next I eat milk
Next I eat ice cream
"""