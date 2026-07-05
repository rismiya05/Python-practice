balance=5000
while True:
    user_input=int(input("Enter your choice: 1 for balance, 2 for withdraw, 3 for deposit: "))
    if user_input==1:
        print("Your current balance is:", balance)
    elif user_input==2:
        withdraw_amount=int(input("Enter amount to withdraw: "))
        if withdraw_amount<=balance:
         balance-=withdraw_amount
         print("Withdrawal successful. Your new balance is:", balance)
        else:
         print("Insufficient funds. Your current balance is:", balance)
    elif user_input==3:
        deposit_amount=int(input("Enter amount to deposit: "))
        balance+=deposit_amount
        print("Deposit successful. Your new balance is:", balance)
    else:
        print("Invalid choice. Please select a valid option.")