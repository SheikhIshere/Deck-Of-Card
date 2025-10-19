import random


def card_pair_to_emoji(*cards):
    """
    Convert one or more card tuples (suit, rank) to their emoji.
    Each card: (suit, rank) where suit in 's', 'h', 'd', 'c' and rank in 'a','2'...'k'
    """
    suit_map = {'s': 0x1F0A1, 'h': 0x1F0B1, 'd': 0x1F0C1, 'c': 0x1F0D1}
    rank_order = ['a','2','3','4','5','6','7','8','9','10','j','q','k']

    emojis = []
    for card in cards:
        suit, rank = card
        index = rank_order.index(rank.lower())
        code_point = suit_map[suit.lower()] + index
        emojis.append(chr(code_point))
    return emojis

# Example usage
print(card_pair_to_emoji(('s','a'), ('h','10'), ('d','q'), ('c','5')))
# Output: ['🂡', '🂺', '🃍', '🃕']


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

# Test the organized deck (weakest to strongest)
d = Deck()
d.card_splitter()

print("\n-----------Organized cards for bot 1 (Weakest to Strongest)-----------\n")
print(d.bot_1())
print("\n-----------Organized cards for bot 2 (Weakest to Strongest)-----------\n")
print(d.bot_2())
print("\n-----------Organized cards for bot 3 (Weakest to Strongest)-----------\n")
print(d.bot_3())
print("\n-----------Organized cards for player (Weakest to Strongest)-----------\n")
print(d.player())