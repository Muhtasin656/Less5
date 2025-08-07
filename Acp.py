
import math
def calculate_trigonometric_values():
    """
    Calculates and prints the sine, cosine, and tangent of an angle.
    The user can input the angle in degrees.
    """
    try:
        angle_degrees = float(input("Enter the angle in degrees: "))
        angle_radians = math.radians(angle_degrees)
        sine_value = math.sin(angle_radians)
        cosine_value = math.cos(angle_radians)
        tangent_value = math.tan(angle_radians)
        print(f"\nFor an angle of {angle_degrees} degrees:")
        print(f"Sine: {sine_value}")
        print(f"Cosine: {cosine_value}")
        print(f"Tangent: {tangent_value}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the angle.")
calculate_trigonometric_values()