import time

from entities.player import Player
from games.hidden_number import hidden_number
from games.sifumi import sifumi

class Console:
    # Class constant storing the allowed user input in the console
    ALLOWED_COMANDS = ("1", "2", "exit")

    def __init__(self):
        self.player = None

    # Private method to get playe's info
    def __create_player(self):
        print("Welcome to this awesome game collection...")
        time.sleep(2)

        while True:
            try:
                player_name: str = input("What is your name ? \n")
                player_age: int = int(input("What is your age ? \n"))
                self.player = Player(player_name, player_age)
            except Exception as e:
                print("Sorry something went wrong : \n" + str(e))
            else :
                break
        

    # Private method to show the command pannel and allow user to type commands
    def __show_commands(self):
        user_command = None

        while user_command not in self.ALLOWED_COMANDS:
            print("Choose a game to start with, 1 for the hidden number, 2 for the sifumi, exit to leave : ")
            user_command = input("type your command : \n").lower()
            # Start functions according to user input
            if user_command == "1": 
                hidden_number()
            elif user_command == "2":
                sifumi()
            elif user_command == "exit":
                exit()
            
            # Reset user input to none to avoid closing the command panel
            time.sleep(2)
            user_command = None

    # Start the whole console by calling the above methods
    @classmethod
    def start_interface(cls):
        cls.__create_player(cls)
        cls.__show_commands(cls)