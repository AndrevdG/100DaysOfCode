# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art

# HINT: You can call clear() to clear the output in the console.
auction = {}


def highest_bidder(completed_auction):
    bid_max = 0
    bid_name = ""
    for bidder in completed_auction:
        if completed_auction[bidder] > bid_max:
            bid_max = completed_auction[bidder]
            bid_name = bidder
    print(f"Bidder with name {bid_name} has won the auction with a bid of {bid_max}")


print(art.logo)
should_continue = True
while should_continue:
    bidder_name = input("What is your name?: ")
    bidder_value = int(input("What's your bid?: $"))
    auction[bidder_name] = bidder_value
    more_bidding = input("\nAre there more bidders? type 'yes' to continue\n").lower()
    if not more_bidding == "yes":
        should_continue = False

highest_bidder(auction)