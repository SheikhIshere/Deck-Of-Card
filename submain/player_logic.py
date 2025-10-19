from card_pair_to_emoji import card_pair_to_emoji as cte

class PlayerLogic:    
    def __init__(self, username='', on_hand_cards=None, total_win=0, won_last_round=False):
        self.username = username
        self.on_hand_cards = on_hand_cards if on_hand_cards is not None else []
        self.total_win = total_win 
        self.won_last_round = won_last_round

    def show_card_emoji(self):
        return cte(*self.on_hand_cards) if self.on_hand_cards else []

class Bot1Logic(PlayerLogic):
    def __init__(self, username="", on_hand_cards=None, total_win=0, won_last_round=False):
        super().__init__(username or "bot1", on_hand_cards, total_win, won_last_round)

class Bot2Logic(PlayerLogic):
    def __init__(self, username="", on_hand_cards=None, total_win=0, won_last_round=False):
        super().__init__(username or "bot2", on_hand_cards, total_win, won_last_round)

class Bot3Logic(PlayerLogic):
    def __init__(self, username="", on_hand_cards=None, total_win=0, won_last_round=False):
        super().__init__(username or "bot3", on_hand_cards, total_win, won_last_round)

class UserPlayerLogic(PlayerLogic):
    def __init__(self, username="", on_hand_cards=None, total_win=0, won_last_round=False):
        super().__init__(username or "user", on_hand_cards, total_win, won_last_round)