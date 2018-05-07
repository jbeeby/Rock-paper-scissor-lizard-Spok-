import sys

numplay = input("How many players?")

if numplay == 1
	print('''Please pick one:
				rock
				paper
				scissors
				spock
				lizard''')

	while True:
		game_dict = {'rock': 1, 'paper': 2, 'scissors': 3, 'spock': 4, 'lizard': 5}
		player_a = str(input("Player a: "))
		a = game_dict.get(player_a)
		b = str(random.randint(0,5))
		
		def compare(u1, u2):
				if u1 == u2:
					return("It's a tie!")
				elif u1 == 1:
					if u2 == 2:
						return("The computer wins with Paper!")
					elif u2 == 3:
						return("You win with Rock!")
					elsif u2 == 4:
						return("The computer wins with Spock!")
					else:
						return("You win with Rock!")
				elif u1 == 2:
					if u2 == 1:
						return("You win with Paper!")
					elif u2 == 3:
						return("The computer wins with Scissors!")
					elsif u2 == 4:
						return("You win with Paper!")
					else:
						return("The computer wins with Lizard!")
				elif u1 == 3:
					if u2 == 1:
						return("The computer wins with Rock!")
					elif u2 == 2:
						return("You win with Scissors!")
					elsif u2 == 4:
						return("The computer wins with Spock!")
					else:
						return("You win with Scissors!")
				elif u1 == 4:
					if u2 == 1:
						return("You win with Spock!")
					elif u2 == 2:
						return("The computer wins with Paper!")
					elsif u2 == 3:
						return("You win with Spock!")
					else:
						return("The computer wins with Lizard!")
				elif u1 == 5:
					if u2 == 1:
						return("The computer wins with Rock!")
					elif u2 == 2:
						return("You win with Lizard!")
					elsif u2 == 3:
						return("The computer wins with Scissors!")
					else:
						return("You win with Lizard!")
		else:
			return("Invalid input! You have not entered rock, paper scissors, lizard or spock; Please try again.")
			sys.exit()

		print(compare(a, b))
		
			
else:

	user1 = input("What's your name?")
	user2 = input("And your name?")
	user1_answer = input("%s, do yo want to choose rock, paper, scissors, lizard or spock?" % user1)
	user2_answer = input("%s, do yo want to choose rock, paper, scissors, lizard or spock?" % user2)

		def compare(u1, u2):
				if u1 == u2:
					return("It's a tie!")
				elif u1 == 'rock':
					if u2 == 'paper':
						return("Paper Wins!")
					elif u2 == 'scissors':
						return("Rock Wins!")
					elsif u2 == 'spock':
						return("Spock Wins!")
					else:
						return("Rock Wins!")
				elif u1 == 'paper':
					if u2 == 'rock':
						return("Paper Wins!")
					elif u2 == 'scissors':
						return("Scissors Wins!")
					elsif u2 == 'spock':
						return("Paper Wins!")
					else:
						return("Lizard Wins!")
				elif u1 == 'scissors':
					if u2 == 'rock':
						return("Rock Wins!")
					elif u2 == 'paper':
						return("Scissors Wins!")
					elsif u2 == 'spock':
						return("Spock Wins!")
					else:
						return("Scissors Wins!")
				elif u1 == 'spock':
					if u2 == 'rock':
						return("Spock Wins!")
					elif u2 == 'paper':
						return("Paper Wins!")
					elsif u2 == 'scissors':
						return("Spock Wins!")
					else:
						return("Lizard Wins!")
				elif u1 == 'lizard':
					if u2 == 'rock':
						return("Rock Wins!")
					elif u2 == 'paper':
						return("Lizard Wins!")
					elsif u2 == 'scissors':
						return("Scissors Wins!")
					else:
						return("Lizard Wins!")
		else:
			return("Invalid input! You have not entered rock, paper scissors, lizard or spock; Please try again.")
			sys.exit()


	print(compare(user1_answer, user2_answer))
