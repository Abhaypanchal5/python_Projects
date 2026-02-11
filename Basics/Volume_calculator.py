class VolumeCalculator:
    def calculate_volume(self, shape, dimensions):
        if shape == "cube":
            return self.calculate_cube_volume(dimensions)
        elif shape == "sphere":
            return self.calculate_sphere_volume(dimensions)
        elif shape == "cylinder":
            return self.calculate_cylinder_volume(dimensions)
        else:
            raise ValueError("Unsupported shape")

    def calculate_cube_volume(self, dimensions):
        side_length = dimensions.get("side_length")
        if side_length is None:
            raise ValueError("Missing dimension: side_length")
        return side_length ** 3

    def calculate_sphere_volume(self, dimensions):
        radius = dimensions.get("radius")
        if radius is None:
            raise ValueError("Missing dimension: radius")
        return (4/3) * 3.14159 * (radius ** 3)

    def calculate_cylinder_volume(self, dimensions):
        radius = dimensions.get("radius")
        height = dimensions.get("height")
        if radius is None or height is None:
            raise ValueError("Missing dimensions: radius and/or height")
        return 3.14159 * (radius ** 2) * height
    
    
# Example usage:
volume_calculator = VolumeCalculator()
shape = input("Enter the shape (cube, sphere, cylinder): ").lower()
dimensions = {}
if shape == "cube":
    dimensions["side_length"] = float(input("Enter the side length of the cube: "))
elif shape == "sphere":
    dimensions["radius"] = float(input("Enter the radius of the sphere: ")) 
elif shape == "cylinder":
    dimensions["radius"] = float(input("Enter the radius of the cylinder: "))
    dimensions["height"] = float(input("Enter the height of the cylinder: "))

try:
    volume = volume_calculator.calculate_volume(shape, dimensions)
    print(f"The volume of the {shape} is: {volume}")
except ValueError as e:    print(e)


# This code defines a class `VolumeCalculator` with methods to calculate the volume of a cube, sphere, and cylinder based on user input.
# The user is prompted to enter the shape and its dimensions, and the corresponding volume is calculated and displayed.