# main.py
from deck_logic import Deck
from player_logic import Bot1Logic, Bot2Logic, Bot3Logic, UserPlayerLogic
# from card_pair_to_emoji import card_pair_to_emoji as cte

def main():
    deck = Deck()
    deck.card_splitter()
    bot1 = Bot1Logic("bot1", on_hand_cards=deck.bot1_cards)
    bot2 = Bot2Logic("bot2", on_hand_cards=deck.bot2_cards)
    bot3 = Bot3Logic("bot3", on_hand_cards=deck.bot3_cards)
    user = UserPlayerLogic("you", on_hand_cards=deck.player_cards)

    # Now print only when you want:
    print("Bot1:", ' '.join(bot1.show_card_emoji()))
    print("Bot2:", ' '.join(bot2.show_card_emoji()))
    print("Bot3:", ' '.join(bot3.show_card_emoji()))
    print("User:", ' '.join(user.show_card_emoji()))

if __name__ == "__main__":
    main()
