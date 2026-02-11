class VolumeCalculator:
    def calculate_volume(self, shape, dimensions):                                          # Check if the shape is a cube and call the corresponding method to calculate its volume
        if shape == "cube":
            return self.calculate_cube_volume(dimensions)                                    
        elif shape == "sphere":
            return self.calculate_sphere_volume(dimensions)
        elif shape == "cylinder":
            return self.calculate_cylinder_volume(dimensions)
        elif shape == "cone":
            return self.calculate_cone_volume(dimensions)
        elif shape == "rectanguler":
            return self.calculate_ractangale_volume(dimensions)
        else:
            raise ValueError("Unsupported shape")

    def calculate_cube_volume(self, dimensions):
        side_length = dimensions.get("side_length")                                          # Get the side length from the dimensions dictionary
        if side_length is None:
            raise ValueError("Missing dimension: side_length")                               # Check if the side length is provided
        return side_length ** 3

    def calculate_sphere_volume(self, dimensions):
        radius = dimensions.get("radius")                                                     # Get the radius from the dimensions dictionary
        if radius is None:
            raise ValueError("Missing dimension: radius")                                     # Check if the radius is provided
        return (4/3) * 3.14159 * (radius ** 3)

    def calculate_cylinder_volume(self, dimensions):
        radius = dimensions.get("radius")                                                     # Get the radius from the dimensions dictionary
        height = dimensions.get("height")                                                     # Get the height from the dimensions dictionary
        if radius is None or height is None:
            raise ValueError("Missing dimensions: radius and/or height")                      # Check if the radius and height are provided
        return 3.14159 * (radius ** 2) * height
    
    def calculate_cone_volume(self, dimensions):
        radius = dimensions.get("radius")                                                     # Get the radius from the dimensions dictionary
        height = dimensions.get("height")                                                     # Get the height from the dimensions dictionary        
        if radius is None or height is None:
            raise ValueError("Missing dimensions: radius and/or height")                      # Check if the radius and height are provided
        return (1/3) * 3.14159 * (radius ** 2) * height
    def calculate_ractangale_volume(self, dimensions):
        length = dimensions.get("length")                                                     # Get the length from the dimensions dictionary
        width = dimensions.get("width")                                                       # Get the width from the dimensions dictionary
        height = dimensions.get("height")                                                     # Get the height from the dimensions dictionary
        if length is None or width is None or height is None:
            raise ValueError("Missing dimensions: length and/or width and/or height")         # Check if the length, width and height are provided
        return length * width * height
    
    
# Example usage:
volume_calculator = VolumeCalculator()
shape = input("Enter the shape (cube, sphere, cylinder, cone, rectanguler): ").lower()
dimensions = {}
if shape == "cube":                                                                          # Get the side length from the user input and store it in the dimensions dictionary
    dimensions["side_length"] = float(input("Enter the side length of the cube: "))
elif shape == "sphere":
    dimensions["radius"] = float(input("Enter the radius of the sphere: ")) 
elif shape == "cylinder":
    dimensions["radius"] = float(input("Enter the radius of the cylinder: "))
    dimensions["height"] = float(input("Enter the height of the cylinder: "))
elif shape == "cone":
    dimensions["radius"] = float(input("Enter the radius of the cone: "))
    dimensions["height"] = float(input("Enter the height of the cone: "))
elif shape == "rectanguler":
    dimensions["length"] = float(input("Enter the length of the rectangular prism: "))
    dimensions["width"] = float(input("Enter the width of the rectangular prism: "))
    dimensions["height"] = float(input("Enter the height of the rectangular prism: "))

try:
    volume = volume_calculator.calculate_volume(shape, dimensions)
    print(f"The volume of the {shape} is: {volume}")
except ValueError as e:    print(e)


# This code defines a class `VolumeCalculator` with methods to calculate the volume of a cube, sphere, cone, rectangular and cylinder based on user input.
# The user is prompted to enter the shape and its dimensions, and the corresponding volume is calculated and displayed.