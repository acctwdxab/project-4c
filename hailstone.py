# Dan Wu
# 10/20/2020
# Write a function named hailstone that takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it takes to reach 1



def hailstone(num) :
    """function takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it takes to reach 1."""

    count = 0

    while (num > 1) :

        if num % 2 == 0 :

            num = num // 2

        else :

            num = 3 * num + 1

        count += 1

    return count

