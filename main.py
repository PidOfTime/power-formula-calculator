# Function to calculate electrical power based on user input
def calculate_power():
    print("Choose the method for calculating electrical power:")
    print("1. Current and Voltage (P = V * I)")
    print("2. Current and Resistance (P = I^2 * R)")
    print("3. Voltage and Resistance (P = V^2 / R)")
    
    # Get user choice
    choice = int(input("Enter your choice (1/2/3): "))
    
    # Option 1: Using current and voltage
    if choice == 1:
        V = float(input("Enter the voltage (V): "))
        I = float(input("Enter the current (I): "))
        P = V * I
        print(f"Electrical Power (P) = {P} Watts")
    
    # Option 2: Using current and resistance
    elif choice == 2:
        I = float(input("Enter the current (I): "))
        R = float(input("Enter the resistance (R): "))
        P = I**2 * R
        print(f"Electrical Power (P) = {P} Watts")
    
    # Option 3: Using voltage and resistance
    elif choice == 3:
        V = float(input("Enter the voltage (V): "))
        R = float(input("Enter the resistance (R): "))
        P = V**2 / R
        print(f"Electrical Power (P) = {P} Watts")
    
    # Invalid choice
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

# Call the function to start the program
calculate_power()
