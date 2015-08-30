def is_triangle_number(number):
    """
    A triangle number is a number where n objects form an equilateral triangle.
    For example, 6 is a triangle number because you can arrange 6 objects into an
    equilateral triangle:
      1
     2 3
    4 5 6
    The nth triangle number is equal to the sum of the n natural numbers from
    1 to n.
    """
    if type(number) is not int:
        return False
    level = 1
    cmp_num = 1
    while number > cmp_num:
        level += 1
        cmp_num += level
    if number == cmp_num or number == 0:
        return True
    else:
        return False

from math import sqrt

def is_triangle_number_faster(number):
    """
    A better method would be noticing that a triangle number is defined by n(n+1)/2
    """
    if type(number) is not int:
        return False
    return ((sqrt(8*number + 1) - 1)/2.0).is_integer()


print is_triangle_number_faster(2)
print is_triangle_number_faster(1)
print is_triangle_number(3560)
print is_triangle_number_faster(15)
print is_triangle_number('hello')