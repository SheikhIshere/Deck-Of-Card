#  --- Usage example (do this after deck creation) ---
from from_ai import Deck, Bot1Logic, Bot2Logic, Bot3Logic, UserPlayerLogic

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