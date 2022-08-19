from os import system, name
from auction_art import logo


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


def main():
    print(logo)
    bids = {}
    bidding_finished = False
    while not bidding_finished:
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        bids[name] = price
        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
        if should_continue == "no":
            bidding_finished = True
            find_highest_bidder(bids)
        elif should_continue == "yes":
            clear()
            print(logo)


if __name__ == "__main__":
    main()
