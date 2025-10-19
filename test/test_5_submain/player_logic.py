from deck_logic import Deck
from card_pair_to_emoji import card_pair_to_emoji as cte

class PlayerLogic:    
    def __init__(self, username = '', on_hand_cards = [], total_win = 0, won_last_round = False):
        self.username = username
        self.on_hand_cards = on_hand_cards
        self.total_win = total_win 
        self.won_last_round = won_last_round

class Bot1Logic(PlayerLogic, Deck):
    def __init__(self, username = "", on_hand_cards = [], total_win = 0, won_last_round = False):
        # Initialize the Deck parent first
        Deck.__init__(self)
        # Split the cards
        self.card_splitter()
        # Now initialize PlayerLogic with the cards
        PlayerLogic.__init__(self, username, self.bot_1(), total_win, won_last_round)
        self.username = "bot1"
    
    def show_card_emoji(self):
        return cte(*self.on_hand_cards)
    
    def show_info(self):
        return f"Username: {self.username}, On Hand Cards: {self.on_hand_cards}, Total Win: {self.total_win}, won Last Round: {self.won_last_round}"

class Bot2Logic(PlayerLogic, Deck):
    def __init__(self, username = "", on_hand_cards = [], total_win = 0, won_last_round = False):
        # Initialize the Deck parent first
        Deck.__init__(self)
        # Split the cards
        self.card_splitter()
        # Now initialize PlayerLogic with the cards
        PlayerLogic.__init__(self, username, self.bot_2(), total_win, won_last_round)
        self.username = "bot2"
    
    def show_card_emoji(self):
        return cte(*self.on_hand_cards)
    
    def show_info(self):
        return f"Username: {self.username}, On Hand Cards: {self.on_hand_cards}, Total Win: {self.total_win}, won Last Round: {self.won_last_round}"

class Bot3Logic(PlayerLogic, Deck):
    def __init__(self, username = "", on_hand_cards = [], total_win = 0, won_last_round = False):
        # Initialize the Deck parent first
        Deck.__init__(self)
        # Split the cards
        self.card_splitter()
        # Now initialize PlayerLogic with the cards
        PlayerLogic.__init__(self, username, self.bot_3(), total_win, won_last_round)
        self.username = "bot3"

    def show_card_emoji(self):
        return cte(*self.on_hand_cards)
    
    def show_info(self):
        return f"Username: {self.username}, On Hand Cards: {self.on_hand_cards}, Total Win: {self.total_win}, won Last Round: {self.won_last_round}"

class UserPlayerLogic(PlayerLogic, Deck):
    def __init__(self, username = "", on_hand_cards = [], total_win = 0, won_last_round = False):
        # Initialize the Deck parent first
        Deck.__init__(self)
        # Split the cards
        self.card_splitter()
        # Now initialize PlayerLogic with the cards
        PlayerLogic.__init__(self, username, self.player(), total_win, won_last_round)
        self.username = "user"

    def show_card_emoji(self):
        return cte(*self.on_hand_cards)
    
    def show_info(self):
        return f"Username: {self.username}, On Hand Cards: {self.on_hand_cards}, Total Win: {self.total_win}, won Last Round: {self.won_last_round}"

# Create instances
# bot1 = Bot1Logic()
# bot2 = Bot2Logic()
# bot3 = Bot3Logic()
# user = UserPlayerLogic()

# print("\n-----------Organized cards for bot 1 (Weakest to Strongest)-----------\n")
# print("Raw cards:", bot1.on_hand_cards)
# print("Emojis:", bot1.show_card_emoji())
# print("Info:", bot1.show_info())

# print("\n-----------Organized cards for bot 2 (Weakest to Strongest)-----------\n")
# print("Raw cards:", bot2.on_hand_cards)
# print("Emojis:", bot2.show_card_emoji())
# print("Info:", bot2.show_info())

# print("\n-----------Organized cards for bot 3 (Weakest to Strongest)-----------\n")
# print("Raw cards:", bot3.on_hand_cards)
# print("Emojis:", bot3.show_card_emoji())
# print("Info:", bot3.show_info())

# print("\n-----------Organized cards for player (Weakest to Strongest)-----------\n")
# print("Raw cards:", user.on_hand_cards)
# print("Emojis:", user.show_card_emoji())
# print("Info:", user.show_info())