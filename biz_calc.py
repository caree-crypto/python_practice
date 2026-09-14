print("\033[32m_______HI MARY, LET'S DO THIS________ \033[0m")
# buying price of one packet of sweets
daily_profits = []

while True:
    while True:
        try:
            bp_1pckt =int(input("what was the price of the packet? "))
            if bp_1pckt < 0:
                print("that can't be negative, try again")
                continue
            break
        except ValueError:
            print("please enter a number")

    # number of sweets in the packet
    no_sweets = 50

    #buying price of one sweet
    bp_1sweet = bp_1pckt / no_sweets

    #selling price of one sweet
    sp_1sweet = 10
    #profit of one sweet
    profit_1sweet = sp_1sweet - bp_1sweet

    while True:
        try:
            sweets_sold = int(input("how many sweets did you sell? "))
            if sweets_sold < 0:
                print("that can't be negative, try again")
                continue
            break
        except ValueError:
            print("\033[31mPlease enter a whole number\033[0m")

    todays_profit = profit_1sweet * sweets_sold
    daily_profits.append(todays_profit)

    print("here is your profit of the day: " + str(round(todays_profit, 2)))
 
    again = input("\033[33mLog another day? (y/n)\033[0m ").strip().lower()
    if again != 'y':
        break

print("\033[36m\n_______ SUMMARY _______\033[0m")
for i, profit in enumerate(daily_profits, start=1):
    print(f"Day {i}: {profit}")
print(f"Total profit: {round(sum(daily_profits), 2)}")
print(f"Average profit per day: {round(sum(daily_profits) / len(daily_profits), 2)}")


