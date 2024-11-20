import math
# They produce the same thing
# for here, it's 31 lines, and for the other one, its 49.
# It was easier to fix the one with the function
# It was easier to add the one with the function 

def main():
    area = triangle_area(3, 3, 3)
    print(f"A triangle with sides 3, 3, 3 has an area of {area}")

    area = triangle_area(3, 4, 5)
    print(f"A triangle with sides 3, 4, 5 has an area of {area}")

    area = triangle_area(7, 8, 9)
    print(f"A triangle with sides 7, 8, 9 has an area of {area}")

    area = triangle_area(5, 12, 13)
    print(f"A triangle with sides 5, 12, 13 has an area of {area}")

    area = triangle_area(10, 9, 11)
    print(f"A triangle with sides 10, 9, 11 has an area of {area}")
    
    area = triangle_area(8, 15, 17)
    print(f"A triangle with sides 8, 15, 17 has an area of {area}")
    
    area = triangle_area(9, 9, 9)
    print(f"A triangle with sides 9, 9, 9 has an area of {area}")


def triangle_area(a: int, b: int, c: int) -> float:
    """Calculates a triangles area.
    
    Args:
        a: length of side a
        b: length of side b
        c: length of side c
    
    Returns:
        The area of the triangle
    """
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return area
    # ^ after computing the area, "return" it


if __name__ == "__main__":
    main()
