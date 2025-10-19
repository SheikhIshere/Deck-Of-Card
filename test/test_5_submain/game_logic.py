from deck_logic import Deck
from player_logic import Bot1Logic, Bot2Logic, Bot3Logic, UserPlayerLogic
import random

class Game:
    def __init__(self, board_cards = []):
        self.deck = Deck()
        # self.deck.card_splitter()
        self.bot1 = Bot1Logic(
            "bot1", 
            on_hand_cards=self.deck.bot1_cards, 
            total_win=0, 
            won_last_round=False
        )
        self.bot2 = Bot2Logic(
            "bot2", 
            on_hand_cards=self.deck.bot2_cards, 
            total_win=0, 
            won_last_round=False
        )
        self.bot3 = Bot3Logic(
            "bot3", 
            on_hand_cards=self.deck.bot3_cards, 
            total_win=0, 
            won_last_round=False
        )
        self.user = UserPlayerLogic(            
            "user", 
            on_hand_cards=self.deck.player_cards, 
            total_win=0, 
            won_last_round=False
        )

        # game logic global variables
        self.board_cards = board_cards
        self.last_winner = None
        self.players = [self.bot1, self.bot2, self.bot3, self.user]
        self.current_player_index = 0

    def who_will_play_first(self):
        # i will check here who have won last round
        if self.last_winner:
            return self.last_winner
        else:
            return random.choice(self.players)

    def taking_player_card(self):
        # check who who won last round
            # taking his card first from that player or bot
            # taking cards and pushing into board_cards[]
            # removing card from player's hand
            # then taking next
            #when it's time to take input from user
                # taking index of card with input function
                # pushing card into board_cards[]
                # removing card from player's hand

            # and then returnning board_cards[]
        pass

    def play(self):
        # here will be the game main logic
        # compare board_cards[] with each other and return the winner
        # update the total win of the winner
        # update the won_last_round of the winner
        # return the winner
        pass


# g = Game()
# g.play()