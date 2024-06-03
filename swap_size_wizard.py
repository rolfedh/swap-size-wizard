import sys

def get_swap_size(ram_size, hibernation, logical_processors, is_virtual_guest):
    if ram_size <= 0:
        return "Invalid RAM size."

    if ram_size <= 4:
        swap_size = 2
    elif ram_size <= 16:
        swap_size = 4
    elif ram_size <= 64:
        swap_size = 8
    elif ram_size <= 256:
        swap_size = 16
    else:
        swap_size = 16
    
    if logical_processors > 140 or ram_size > 3072:
        swap_size = max(swap_size, 100)

    if hibernation:
        if ram_size <= 2:
            swap_size = 3 * ram_size
        elif ram_size <= 8:
            swap_size = 2 * ram_size
        elif ram_size <= 64:
            swap_size = 1.5 * ram_size
        else:
            return "Hibernation not recommended for systems with more than 64GB of RAM."

    if is_virtual_guest:
        swap_size = max(swap_size, 4) # ensure at least 4GB for virtual guests

    return f"Recommended swap size: {swap_size} GB."

def main():
    print("Swap Size Recommendation Wizard for Red Hat Platforms\n")

    # Prompt for RAM size
    try:
        ram_size = float(input("Enter the amount of RAM installed (in GB): "))
    except ValueError:
        print("Invalid input. Please enter a numerical value for RAM size.")
        sys.exit(1)

    # Prompt for hibernation requirement
    hibernation_input = input("Is hibernation required? (yes/no): ").strip().lower()
    if hibernation_input in ['yes', 'y']:
        hibernation = True
    elif hibernation_input in ['no', 'n']:
        hibernation = False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        sys.exit(1)

    # Prompt for logical processors count
    try:
        logical_processors = int(input("Enter the number of logical processors: "))
    except ValueError:
        print("Invalid input. Please enter a numerical value for the number of logical processors.")
        sys.exit(1)

    # Prompt for virtual guest
    virtual_guest_input = input("Is this a virtual guest? (yes/no): ").strip().lower()
    if virtual_guest_input in ['yes', 'y']:
        is_virtual_guest = True
    elif virtual_guest_input in ['no', 'n']:
        is_virtual_guest = False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        sys.exit(1)

    # Calculate and display the recommended swap size
    result = get_swap_size(ram_size, hibernation, logical_processors, is_virtual_guest)
    print(result)

if __name__ == "__main__":
    main()

