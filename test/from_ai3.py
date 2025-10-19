import random
from card_pair_to_emoji import card_pair_to_emoji as cte

class Deck:
    def __init__(self):
        suits = ['s', 'h', 'd', 'c']
        ranks = ['a', 'k', 'q', 'j', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        self.all_cards = [(s, r) for s in suits for r in ranks]
        self.all_spread = []  # cards currently on the table

        self.bot1_cards = []
        self.bot2_cards = [] 
        self.bot3_cards = []
        self.player_cards = []
        
    def show_cards(self):        
        return self.all_cards

    def show_spread(self):
        return self.all_spread
    
    def card_shuffle(self):
        shuffled_card = self.all_cards.copy()
        random.shuffle(shuffled_card)
        return shuffled_card

    def card_splitter(self):
        shuffled_card = self.card_shuffle()
        
        # Split the cards
        self.bot1_cards = shuffled_card[0::4]
        self.bot2_cards = shuffled_card[1::4]
        self.bot3_cards = shuffled_card[2::4]
        self.player_cards = shuffled_card[3::4]

        # Sort each player's cards (weakest to strongest)
        self.bot1_cards = self.sort_cards(self.bot1_cards)
        self.bot2_cards = self.sort_cards(self.bot2_cards)
        self.bot3_cards = self.sort_cards(self.bot3_cards)
        self.player_cards = self.sort_cards(self.player_cards)

        return self.bot1_cards, self.bot2_cards, self.bot3_cards, self.player_cards
    
    def sort_cards(self, cards):
        # Define suit order (you can modify this if you want different suit ordering)
        suit_order = {'s': 0, 'h': 1, 'd': 2, 'c': 3}
        
        # Define rank order from WEAKEST to STRONGEST
        rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, 
                     '9': 7, '10': 8, 'j': 9, 'q': 10, 'k': 11, 'a': 12}
        
        # Sort by suit first, then by rank (weakest to strongest)
        return sorted(cards, key=lambda card: (suit_order[card[0]], rank_order[card[1]]))
    
    def bot_1(self):
        return self.bot1_cards
    
    def bot_2(self):
        return self.bot2_cards

    def bot_3(self):
        return self.bot3_cards

    def player(self):
        return self.player_cards

class PlayerLogic:    
    def __init__(self, username = '', on_hand_cards = [], total_win = 0):
        self.username = username
        self.on_hand_cards = on_hand_cards
        self.total_win = total_win 

class Bot1Logic(PlayerLogic, Deck):
    def __init__(self, username = "", on_hand_cards = [], total_win = 0):
        # Initialize the Deck parent first
        Deck.__init__(self)
        # Split the cards
        self.card_splitter()
        # Now initialize PlayerLogic with the cards
        PlayerLogic.__init__(self, username, self.bot_1(), total_win)
        self.username = "bot1"

    def show_card_emoji(self):
        return cte(*self.on_hand_cards)
    

class Bot2Logic(PlayerLogic, Deck):
    def __init__(self, username = "", on_hand_cards = [], total_win = 0):
        # Initialize the Deck parent first
        Deck.__init__(self)
        # Split the cards
        self.card_splitter()
        # Now initialize PlayerLogic with the cards
        PlayerLogic.__init__(self, username, self.bot_2(), total_win)
        self.username = "bot2"
    
    def show_card_emoji(self):
        return cte(*self.on_hand_cards)

class Bot3Logic(PlayerLogic, Deck):
    def __init__(self, username = "", on_hand_cards = [], total_win = 0):
        # Initialize the Deck parent first
        Deck.__init__(self)
        # Split the cards
        self.card_splitter()
        # Now initialize PlayerLogic with the cards
        PlayerLogic.__init__(self, username, self.bot_3(), total_win)
        self.username = "bot3"

    def show_card_emoji(self):
        return cte(*self.on_hand_cards)

class UserPlayerLogic(PlayerLogic, Deck):
    def __init__(self, username = "", on_hand_cards = [], total_win = 0):
        # Initialize the Deck parent first
        Deck.__init__(self)
        # Split the cards
        self.card_splitter()
        # Now initialize PlayerLogic with the cards
        PlayerLogic.__init__(self, username, self.player(), total_win)
        self.username = "user"

    def show_card_emoji(self):
        return cte(*self.on_hand_cards)

# Create instances
bot1 = Bot1Logic()
bot2 = Bot2Logic()
bot3 = Bot3Logic()
user = UserPlayerLogic()

print("\n-----------Organized cards for bot 1 (Weakest to Strongest)-----------\n")
print("Raw cards:", bot1.on_hand_cards)
print("Emojis:", bot1.show_card_emoji())

print("\n-----------Organized cards for bot 2 (Weakest to Strongest)-----------\n")
print("Raw cards:", bot2.on_hand_cards)
print("Emojis:", bot2.show_card_emoji())

print("\n-----------Organized cards for bot 3 (Weakest to Strongest)-----------\n")
print("Raw cards:", bot3.on_hand_cards)
print("Emojis:", bot3.show_card_emoji())

print("\n-----------Organized cards for player (Weakest to Strongest)-----------\n")
print("Raw cards:", user.on_hand_cards)
print("Emojis:", user.show_card_emoji())