MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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

def get_bet():
    while True:
        bet = input("Enter money you want to bet: $")

        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
            
        else:
            print("Enter digits only")
    
    return bet


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
    bet = get_bet()
    lines = get_number_of_lines()
    total_bet = lines * bet
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: {total_bet}")


if __name__ == "__main__":
    main()