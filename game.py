from human import Human
from ai import AI

class Play_game:
    def __init__(self) -> None:
        self.player = Human()
        self.ai = AI()

    def display_welcome(self):
        print("Welcome to Rock, Paper, Sissor, Lizard, Spock!")
        print("")
        print("Rules are Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper.")
    
    def game_play(self):
        self.display_welcome()


    # def matches(self):
    #     print("Please choose your hand gestures.")

    #     while 
