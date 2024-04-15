# Importing libraries
import math

# Stefan-Boltzmann constant (in units of W/m^2K^4)
sigma = 5.67e-8

def calculate_L(R, T):
    """
    Calculates the luminosity L of a star given its radius R (in meters) and temperature T (in Kelvin).
    """
    area = 4 * math.pi * R ** 2
    L = area * sigma * T ** 4
    return L

def calculate_R(L, T):
    """
    Calculates the radius R of a star given its luminosity L (in Watts) and temperature T (in Kelvin).
    """
    R = math.sqrt(L / (4 * math.pi * sigma * T ** 4))
    return R

def calculate_T(L, R):
    """
    Calculates the temperature T of a star given its radius R (in meters) and luminosity L (in Watts).
    """
    T = ((L / (4 * math.pi * R ** 2 * sigma)) ** 0.25)
    return T

def main():
    choice = input("Which variable do you want to calculate? (L, R, T): ").upper()
    if choice == 'L':
        R = float(input("Enter the star's radius R in meters: "))
        T = float(input("Enter the star's temperature T in Kelvin: "))
        result = calculate_L(R, T)
        print(f"The luminosity L of the star is {format(result, '.3e')} Watts")
    elif choice == 'R':
        L = float(input("Enter the star's luminosity L in Watts: "))
        T = float(input("Enter the star's temperature T in Kelvin: "))
        result = calculate_R(L, T)
        print(f"The radius R of the star is {format(result, '.3e')} meters")
    elif choice == 'T':
        L = float(input("Enter the star's luminosity L in Watts: "))
        R = float(input("Enter the star's radius R in meters: "))
        result = calculate_T(L, R)
        print(f"The temperature T of the star is {format(result, '.3e')} Kelvin")
    else:
        print("Invalid option. Please choose between L, R, or T.")

if __name__ == "__main__":
    main()
