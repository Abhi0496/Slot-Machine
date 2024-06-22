MAX_LINES = 3

def deposit():
    while True:
        amount = input("Enter money you want to deposit: $")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
            
        else:
            print("Enter digits only")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES})? ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Lines must be between 1 - {MAX_LINES}")
            
        else:
            print("Enter digits only")
    
    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance,lines)

if __name__ == "__main__":
    main()