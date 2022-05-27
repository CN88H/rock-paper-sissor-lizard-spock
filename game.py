from human import Human
from ai import AI
from rules import Gesture

import random

class Play_game:
    def __init__(self) -> None:
        self.human = Human("player 1")
        self.human_two = Human("player 2")
        self.ai = AI("CPU")


    def choose_opp(self):
        choice_opp = int(input("Choose 1 to vs an AI or choose 2 to vs another player: "))

        if choice_opp == 1:
            print("You are facing an Cpu.")
            # choice_opp = [self.human, self.ai]
            self.human_vs_ai()
        elif choice_opp == 2:
            print("You are facing another Player.")
            choice_opp = [self.human, self.human_two]
            self.human_vs_human()
        else:
            "Please reselect."



        # self.player = Human()
        # self.ai = AI()
    def game_play(self):
        self.display_welcome()
        self.choose_opp()


    def display_welcome(self):
        print("Welcome to Rock, Paper, Sissor, Lizard, Spock!")
        print("")
        print("Rules are Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper ,Paper disproves Spock, Spock vaporizes Rock.")
    

    # def game_rules(self):
        
    #     self.gestures = ["rock, paper, sissor, lizard, spock"]


        # while self.human.score and self.human_two.score and self.ai.score >= 2:

    def human_vs_ai(self):
        
        print("1 = rock")
        print("2 = paper")
        print("3 = sissor")
        print("4 = lizard")
        print("5 = spock")

        gestures = [Gesture('Rock', 'Scissors', 'Lizard'), 
            Gesture('Paper', "Rock", 'Spock'),
            Gesture('Sissor', 'Paper', 'Lizard'),
            Gesture('Lizard', 'Spock', 'Paper'),
            Gesture('Spock', 'Sissor', 'Rock')]

        # ai_lists = ['Rock', 'Paper', 'Sissor', 'Lizard', 'Spock']


        while self.human.score or self.ai.score <= 2:
            human_choice = gestures[int(input("Select your gesture: ")) - 1] 
            print(f"You've choosen {human_choice.name}")

            ai_choice = gestures[random.randint(0, 4)]
            print(f"CPU Chose {ai_choice.name}")

            if human_choice == ai_choice:
                print("It's a tie! Try again.")
            elif ai_choice.name == human_choice.defeats_gesture2 or human_choice.defeats_gesture1:
                print("You win this hand.")
                self.human.score += 1
            elif human_choice.name == ai_choice.defeats_gesture1 or ai_choice.defeats_gesture2:
                print('You lost this hand.')
                self.ai.score += 1
            else:
                print('Please pick from 1-5.')
            
    


    def human_vs_human(self):
        
        print("1 = rock")
        print("2 = paper")
        print("3 = sissor")
        print("4 = lizard")
        print("5 = spock")

        gestures = [Gesture('Rock', 'Scissors', 'Lizard'), 
            Gesture('Paper', "Rock", 'Spock'),
            Gesture('Sissor', 'Paper', 'Lizard'),
            Gesture('Lizard', 'Spock', 'Paper'),
            Gesture('Spock', 'Sissor', 'Rock')]

        while self.human.score or self.ai.score <= 2:
                human_choice = gestures[int(input("Select your gesture: ")) - 1] 
                print(f"You've choosen {human_choice.name}")

                human_two_choice = gestures[int(input("Select your gesture: ")) - 1]
                print(f"CPU Chose {human_two_choice.name}")

                if human_choice == human_two_choice:
                    print("It's a tie! Try again.")
                elif human_two_choice.name == human_choice.defeats_gesture2 and human_choice.defeats_gesture1:
                    print("You win this hand.")
                    self.human.score += 1
                elif human_choice.name == human_two_choice.defeats_gesture1 and human_two_choice.defeats_gesture2:
                    print('You lost this hand.')
                    self.ai.score += 1
                else:
                    print('Please pick from 1-5.')
            







