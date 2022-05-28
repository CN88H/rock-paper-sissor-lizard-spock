from human import Human
from ai import AI
from rules import Gesture

import random

class Play_game:
    def __init__(self) -> None:
        self.human = Human("player one")
        self.human_two = Human("player two")
        self.ai = AI("CPU")

        # self.player = Human()
        # self.ai = AI()
    def game_play(self):
        self.display_welcome()
        self.choose_opp()
        # self.display_winner()



    def display_welcome(self):
        print("Welcome to Rock, Paper, Sissor, Lizard, Spock!")
        print("")
        print("Rules are Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper ,Paper disproves Spock, Spock vaporizes Rock.")
    

    def choose_opp(self):
        choice_opp = int(input("Choose 1 to vs an AI or choose 2 to vs another player: "))

        if choice_opp == 1:
            print("You are facing an Cpu.")
            choice_opp = [{self.human}, {self.ai}]
            self.human_vs_ai()

        elif choice_opp == 2:
            print("You are facing another Player.")
            choice_opp = [{self.human}, {self.human_two}]
            self.human_vs_human()

        else:
            "Please reselect."


    def human_vs_ai(self):
        

        gestures = [Gesture('Rock', 'Sissor', 'Lizard'), 
            Gesture('Paper', "Rock", 'Spock'),
            Gesture('Sissor', 'Paper', 'Lizard'),
            Gesture('Lizard', 'Spock', 'Paper'),
            Gesture('Spock', 'Sissor', 'Rock')]

        # ai_lists = ['Rock', 'Paper', 'Sissor', 'Lizard', 'Spock']



        while self.human.score <= 2 or self.ai.score <= 2:
            print("")
            print("This is the choices.")
            print("1 = rock")
            print("2 = paper")
            print("3 = sissor")
            print("4 = lizard")
            print("5 = spock")
            print("")

            human_choice = gestures[int(input("Select your gesture: ")) - 1] 
            print(f"You've choosen {human_choice.name}")

            ai_choice = gestures[random.randint(0, 4)]
            print(f"CPU Chose {ai_choice.name}")

            
            if human_choice == ai_choice:
                print("It's a tie! Try again.")
                print("")
                print(f"{self.human.name} score is {self.human.score}, and {self.ai.name} score is {self.ai.score}.")
            elif ai_choice.name == human_choice.defeats_gesture2 or ai_choice.name == human_choice.defeats_gesture1:
                print(f"{self.human.name} won this hand.")
                print("")
                self.human.score += 1
                print(f"{self.human.name} score is {self.human.score}, and {self.ai.name} score is {self.ai.score}.")
                if self.human.score == 2:
                    self.display_winner()
            elif human_choice.name == ai_choice.defeats_gesture1 or human_choice.name == ai_choice.defeats_gesture2:
                print(f'{self.ai.name} won this hand.')
                print("")
                self.ai.score += 1
                print(f"{self.human.name} score is {self.human.score}, and CPU score is {self.ai.score}.")
                if self.ai.score == 2:
                    self.display_winner()
            else:
                print('Please pick from 1-5.')
            
    


    def human_vs_human(self):

        gestures = [Gesture('Rock', 'Sissor', 'Lizard'), 
            Gesture('Paper', "Rock", 'Spock'),
            Gesture('Sissor', 'Paper', 'Lizard'),
            Gesture('Lizard', 'Spock', 'Paper'),
            Gesture('Spock', 'Sissor', 'Rock')]

        while self.human.score <= 2 or self.human_two.score <= 2:
            print("")
            print("This is the choices.")
            print("1 = rock")
            print("2 = paper")
            print("3 = sissor")
            print("4 = lizard")
            print("5 = spock")
            print("")

            human_choice = gestures[int(input("Select your gesture: ")) - 1] 
            print(f"{self.human.name} chose {human_choice.name}")

            human_two_choice = gestures[int(input("Select your gesture: ")) - 1]
            print(f"{self.human_two.name} Chose {human_two_choice.name}")

            if human_choice == human_two_choice:
                print("It's a tie! Try again.")
                print("")
                print(f"{self.human.name} score is {self.human.score}, and {self.human_two.name} score is {self.human_two.score}.")
            elif human_two_choice.name == human_choice.defeats_gesture1 or human_two_choice.name == human_choice.defeats_gesture2:
                print(f"{self.human.name} wins this hand.")
                print("")
                self.human.score += 1
                print(f"{self.human.name} score is {self.human.score}, and {self.human_two.name} score is {self.human_two.score}.")
                if self.human.score == 2:
                    self.display_winner()
            elif human_choice.name == human_two_choice.defeats_gesture1 or human_choice.name == human_two_choice.defeats_gesture2:
                print(f'{self.human_two.name} wins this hand.')
                print("")
                self.human_two.score += 1
                print(f"{self.human.name} score is {self.human.score}, and {self.human_two.name} score is {self.human_two.score}.")
                if self.human_two.score == 2:
                    self.display_winner
            else:
                print('Please pick from 1-5.')
            

    def display_winner(self):
        if self.human.score == 2:
            print(f"{self.human.name} is the Winner!")
            self.ask_to_play_again()
        elif self.human_two.score == 2:
            print(f"{self.human_two.name} is the Winner!")
            self.ask_to_play_again()
        elif self.ai.score == 2:
            print(f"{self.ai.name} is the Winner!")
            self.ask_to_play_again()
        else:
            print("Select correct response.")


    def ask_to_play_again(self):
        
        ending_question = True
        while ending_question == True:

            final_quesiton = input("Do you want to play again? y/n: ")
            if final_quesiton == "y":
                self.game_play()
            elif final_quesiton == "n":
                print("Thank you for playing.")
                ending_question = False
                break
                
            else:
                print("Please choose a correct response.")
                break