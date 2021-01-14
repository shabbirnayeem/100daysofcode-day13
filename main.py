####################### End of the day project#################
#Blind Auction 
#from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secrete auction program.")


auction = {}
end_of_auction = False

def highest_bidder():
	higest = 0
	winner = ''
	for bidder in auction:
		if auction[bidder] > higest:
			higest = auction[bidder]
			winner = bidder
	print(f"The winner is {winner} with a bid of ${higest}.")

while not end_of_auction:
	#while loop will loop all the lines upto the in statement. Depending on the answer it either loop again or end
	name = input("What is your name?: ")
	bid = int(input("What's your bid?: $"))	
	auction[name] = bid
	more_bidders = input("Are there any other bidders? Type 'yes' or 'no'" ).lower()

	if more_bidders == 'no':
		end_of_auction = True
		print(auction)
		highest_bidder()
	elif more_bidders == 'yes':
		#clear()
