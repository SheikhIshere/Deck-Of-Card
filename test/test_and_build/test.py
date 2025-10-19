import random

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
        shuffled_card = self.all_cards
        random.shuffle(shuffled_card)
        return shuffled_card

    def card_splitter(self):
        shuffled_card = self.card_shuffle()
        # print(shuffled_card)
        self.bot1_cards = shuffled_card[0::4]
        self.bot2_cards = shuffled_card[1::4]
        self.bot3_cards = shuffled_card[2::4]
        self.player_cards = shuffled_card[3::4]

        # sorting cards
        self.bot1_cards =   shuffled_card[0::4]
        self.bot2_cards =   shuffled_card[1::4]
        self.bot3_cards =   shuffled_card[2::4]
        self.player_cards = shuffled_card[3::4]


        return self.bot1_cards, self.bot2_cards, self.bot3_cards, self.player_cards
    

    def bot_1(self):
        return self.bot1_cards
    
    def bot_2(self):
        return self.bot2_cards

    def bot_3(self):
        return self.bot3_cards

    def player(self):
        return self.player_cards
    

    


d = Deck()
d.card_splitter()


print("\n-----------splitted card for bot 1-----------\n")
print(d.bot_1())
print("\n-----------splitted card for bot 2-----------\n")
print(d.bot_2())
print("\n-----------splitted card for bot 3-----------\n")
print(d.bot_3())
print("\n-----------splitted card for player-----------\n")
print(d.player())
print("\n-----------splitted card-----------\n")

# print(f"Bot1: {len(bot1)} cards")
# print(f"Bot2: {len(bot2)} cards")
# print(f"Bot3: {len(bot3)} cards")
# print(f"Player: {len(player)} cards")

# print("\n--Showing cards--")

# print(d.show_cards())

# print("\n------------shuffled card----------\n")

# print(d.card_shuffle())

# print("\n-----------splitted card-----------\n")

# print(bot1)

# print("\n-----------splitted card-----------\n")

# print(bot2)

# print("\n-----------splitted card-----------\n")

# print(bot3)

# print("\n-----------splitted card-----------\n")

# print(player)

