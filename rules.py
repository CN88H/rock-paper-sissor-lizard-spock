
class Gesture:
    def __init__(self, name, defeats_gesture1, defeats_gesture2):
        self.name = name
        self.defeats = [defeats_gesture1, defeats_gesture2]
        self.defeats_gesture1 = defeats_gesture1
        self.defeats_gesture2 = defeats_gesture2

    def gesture_option(self):

            self.gestures = [Gesture('Rock', 'Scissors', 'Lizard'), 
                        Gesture('Paper', "Rock", 'Spock'),
                        Gesture('Sissor', 'Paper', 'Lizard'),
                        Gesture('Lizard', 'Spock', 'Ppaer'),
                        Gesture('Spock', 'Sissor', 'Rock')]


# class Rules:
#     def __init__(self) -> None:
#         self.gestures = ["rock", "paper", "sissor", "lizard", "spock"]
#         self.game_factor()

# #     # def option(self):
# #     #     gestures_1 = "Rock"
#     #     gestures_2 = "Paper"
#     #     gestures_3 = "Sissor"
#     #     gestures_4 = "Lizard"
#     #     gestures_5 = "Spock"
    
    # def game_factor(self):
    #     self.gestures[0] > self.gestures[2] or self.gestures[3]
