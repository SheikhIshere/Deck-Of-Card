import random
from card_pair_to_emoji import card_pair_to_emoji as cte

class Deck:
    def __init__(self):
        suits = ['s', 'h', 'd', 'c']
        ranks = ['a', 'k', 'q', 'j', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        self.all_cards = [(s, r) for s in suits for r in ranks]
        self.all_spread = []
        
        # Initialize empty card lists
        self.bot1_cards = []
        self.bot2_cards = [] 
        self.bot3_cards = []
        self.player_cards = []
        
    def card_shuffle(self):
        return random.sample(self.all_cards, len(self.all_cards))
    
    def card_splitter(self):
        shuffled_card = self.card_shuffle()
        
        # Split the cards
        self.bot1_cards = shuffled_card[0::4]
        self.bot2_cards = shuffled_card[1::4]
        self.bot3_cards = shuffled_card[2::4]
        self.player_cards = shuffled_card[3::4]

        # Sort each player's cards
        self.bot1_cards = self.sort_cards(self.bot1_cards)
        self.bot2_cards = self.sort_cards(self.bot2_cards)
        self.bot3_cards = self.sort_cards(self.bot3_cards)
        self.player_cards = self.sort_cards(self.player_cards)

    def sort_cards(self, cards):
        suit_order = {'s': 0, 'h': 1, 'd': 2, 'c': 3}
        rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, 
                     '9': 7, '10': 8, 'j': 9, 'q': 10, 'k': 11, 'a': 12}
        return sorted(cards, key=lambda card: (suit_order[card[0]], rank_order[card[1]]))

class PlayerLogic:
    def __init__(self, username='', on_hand_cards=[], total_win=0):
        self.username = username
        self.on_hand_cards = on_hand_cards
        self.total_win = total_win 

    def show_card_emoji(self):
        return cte(*self.on_hand_cards)

# Create deck and split cards first
deck = Deck()
deck.card_splitter()

# Then create players with the already-dealt cards
bot1 = PlayerLogic("bot1", deck.bot1_cards)
bot2 = PlayerLogic("bot2", deck.bot2_cards)
bot3 = PlayerLogic("bot3", deck.bot3_cards)
user = PlayerLogic("user", deck.player_cards)

print("\n-----------Organized cards for bot 1 (Weakest to Strongest)-----------\n")
print(bot1.show_card_emoji())
print("\n-----------Organized cards for bot 2 (Weakest to Strongest)-----------\n")
print(bot2.show_card_emoji())
print("\n-----------Organized cards for bot 3 (Weakest to Strongest)-----------\n")
print(bot3.show_card_emoji())
print("\n-----------Organized cards for player (Weakest to Strongest)-----------\n")
print(user.show_card_emoji())