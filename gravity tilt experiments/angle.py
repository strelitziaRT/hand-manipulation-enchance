import math

def compute_gravity(angle_degrees):
    if 0 <= angle_degrees <= 90:
        g = 9.81
        theta = math.radians(angle_degrees)

        g_x = g * math.sin(theta)
        g_z = g * math.cos(theta)

        # Set a small tolerance
        tolerance = 1e-10
        if abs(g_x) < tolerance:
            g_x = 0.0
        if abs(g_z) < tolerance:
            g_z = 0.0

        return [g_x, 0.0, -g_z]
    else:
        raise ValueError("Angle should be between 0 and 90 degrees.")

def main():
    angle_degrees = float(input("Enter the angle (between 0 and 90 degrees): "))
    gravity = compute_gravity(angle_degrees)
    print(f"Gravity parameters for {angle_degrees} degrees: {gravity}")

if __name__ == "__main__":
    main()
