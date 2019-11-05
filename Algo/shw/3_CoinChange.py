if __name__ == "__main__":
    #print("Enter the coin denominations: ")
    #denominations = [int(x) for x in input().strip().split(' ')]
    denominations = [25,15,10,5]
    denominations.sort(reverse=True)

    #print("Enter the amount: ")
    #money = int(input())
    money = 40

    coins = 0
    for i in denominations:
        coins = coins + money//i
        money = money%i

    print("Required Coins " ,  coins)
