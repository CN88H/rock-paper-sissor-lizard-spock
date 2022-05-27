
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        # self.gesture_lists = ["rock", "paper", "sissor", "lizard", "spock"]

    # def get_gestures(self, hand_name, gesture_1, gesture2):
    #     self.hand_name = hand_name
    #     self.defeats = [gesture_1, gesture2]
    #     self.loses = [gesture_1, gesture2]
    #     self.ties = hand_name == gesture_1 == gesture2
