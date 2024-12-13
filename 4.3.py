###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a,b,c):
    import math
    s = 1/2 * (a+b+c)
    result = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return result
area_1 = triangle_area(3,4,5)
area_2 = triangle_area(5,12,13)
area_3 = triangle_area(7,24,25)

print(f'The area of ​​a triangle with sides 3, 4, 5  is {area_1}')
print(f'The area of ​​a triangle with sides 5, 12, 13 is {area_2}')
print(f'The area of ​​a triangle with sides 7, 24, 25 is {area_3}')