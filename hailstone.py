# Dan Wu
# 10/19/2020
# Write a function named hailstone that takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it takes to reach 1

def hailstone(num):
    """function takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it takes to reach 1."""
    while num != 1:
      count = 1
      if num % 2 == 0 :
           count += hailstone ( num / 2 )
      else:
          count += hailstone ( (num * 3) + 1 )
      return count
    if num == 1 :
      count = 0
      return count

