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

def main():
    balance = deposit()

if __name__ == "__main__":
    main()