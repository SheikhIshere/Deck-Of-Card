import random

# --- Converter function (one place only) ---
def card_pair_to_emoji(*cards):
    suit_map = {'s': 0x1F0A1, 'h': 0x1F0B1, 'd': 0x1F0C1, 'c': 0x1F0D1}
    rank_order = ['a','2','3','4','5','6','7','8','9','10','j','q','k']
    emojis = []
    for card in cards:
        try:
            suit, rank = card
            idx = rank_order.index(str(rank).lower())
            emojis.append(chr(suit_map[str(suit).lower()] + idx))
        except Exception:
            emojis.append('�')   # safe placeholder for invalid card
    return emojis

# --- Deck ---
class Deck:
    def __init__(self):
        suits = ['s', 'h', 'd', 'c']
        ranks = ['a','2','3','4','5','6','7','8','9','10','j','q','k']  # consistent with converter
        self.all_cards = [(s, r) for s in suits for r in ranks]
        self.bot1_cards = []
        self.bot2_cards = []
        self.bot3_cards = []
        self.player_cards = []

    def card_shuffle(self):
        deck = self.all_cards.copy()
        random.shuffle(deck)
        return deck

    def card_splitter(self):
        shuffled = self.card_shuffle()
        # Deal round-robin (like dealing 4 players)
        self.bot1_cards = shuffled[0::4]
        self.bot2_cards = shuffled[1::4]
        self.bot3_cards = shuffled[2::4]
        self.player_cards = shuffled[3::4]

        # Optionally sort hands (weakest->strongest)
        self.bot1_cards = self.sort_cards(self.bot1_cards)
        self.bot2_cards = self.sort_cards(self.bot2_cards)
        self.bot3_cards = self.sort_cards(self.bot3_cards)
        self.player_cards = self.sort_cards(self.player_cards)

        return self.bot1_cards, self.bot2_cards, self.bot3_cards, self.player_cards

    def sort_cards(self, cards):
        suit_order = {'s': 0, 'h': 1, 'd': 2, 'c': 3}
        rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6,
                      '9': 7, '10': 8, 'j': 9, 'q': 10, 'k': 11, 'a': 12}
        return sorted(cards, key=lambda card: (suit_order[card[0]], rank_order[card[1]]))

# --- Player classes (no risky defaults) ---
class PlayerLogic:
    def __init__(self, username, on_hand_cards=None, total_win=0):
        self.username = username
        self.on_hand_cards = on_hand_cards or []
        self.total_win = total_win

    def show_cards(self):
        return self.on_hand_cards

    def show_card_emoji(self):
        return card_pair_to_emoji(*self.on_hand_cards)

class Bot1Logic(PlayerLogic): pass
class Bot2Logic(PlayerLogic): pass
class Bot3Logic(PlayerLogic): pass
class UserPlayerLogic(PlayerLogic): pass

# --- Usage example (do this after deck creation) ---
if __name__ == "__main__":
    d = Deck()
    d.card_splitter()  # fills d.bot1_cards, d.bot2_cards, d.bot3_cards, d.player_cards

    # Create players and hand them cards explicitly
    bot1 = Bot1Logic("bot1", on_hand_cards=d.bot1_cards)
    bot2 = Bot2Logic("bot2", on_hand_cards=d.bot2_cards)
    bot3 = Bot3Logic("bot3", on_hand_cards=d.bot3_cards)
    user = UserPlayerLogic("you", on_hand_cards=d.player_cards)

    # Show emoji hands
    print("Bot1:", ' '.join(bot1.show_card_emoji()))
    print("Bot2:", ' '.join(bot2.show_card_emoji()))
    print("Bot3:", ' '.join(bot3.show_card_emoji()))
    print("User:", ' '.join(user.show_card_emoji()))
