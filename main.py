import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
} 
 
def get_slot_machine_spin(rows, colsm symbols):
    

    pass


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
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You do not have enough balance. Your bet amount is: $ {total_bet} and current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: {total_bet}")


if __name__ == "__main__":
    main()