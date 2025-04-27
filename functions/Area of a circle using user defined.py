import math


def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area


# Example usage
radius = float(input("Enter the radius of the circle: "))
area_of_circle = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area_of_circle}")
