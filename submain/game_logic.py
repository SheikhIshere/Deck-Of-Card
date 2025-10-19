from deck_logic import Deck
from player_logic import Bot1Logic, Bot2Logic, Bot3Logic, UserPlayerLogic
import random
import time
from card_pair_to_emoji import card_pair_to_emoji as cte

class Game:
    def __init__(self, board_cards=[]):
        self.deck = Deck()
        self.deck.card_splitter()  # Actually split the cards
        
        # Initialize players with their cards
        self.bot1 = Bot1Logic("bot1", self.deck.bot1_cards)
        self.bot2 = Bot2Logic("bot2", self.deck.bot2_cards)
        self.bot3 = Bot3Logic("bot3", self.deck.bot3_cards)
        self.user = UserPlayerLogic("user", self.deck.player_cards)

        self.board_cards = board_cards
        self.played_cards_this_round = []  # (player, card)
        self.last_winner = None
        self.players = [self.bot1, self.bot2, self.bot3, self.user]
        self.current_player_index = 0
        self.leading_suit = None

    def who_will_play_first(self):
        if self.last_winner:
            return self.last_winner
        else:
            first_player = random.choice(self.players)
            print(f"🎲 {first_player.username.capitalize()} starts first!")
            return first_player

    def get_next_player(self):
        self.current_player_index = (self.current_player_index + 1) % 4
        return self.players[self.current_player_index]

    def compare_cards(self, card1, card2):
        """Compare two cards and return which one wins (1: card1, -1: card2)"""
        rank_order = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, 
                     '9': 7, '10': 8, 'j': 9, 'q': 10, 'k': 11, 'a': 12}
        
        suit_order = {'s': 0, 'h': 1, 'd': 2, 'c': 3}
        
        rank1, suit1 = card1[1], card1[0]
        rank2, suit2 = card2[1], card2[0]
        
        # Compare by rank first
        if rank_order[rank1] > rank_order[rank2]:
            return 1
        elif rank_order[rank1] < rank_order[rank2]:
            return -1
        else:
            # If ranks are equal, compare by suit
            if suit_order[suit1] < suit_order[suit2]:
                return 1
            else:
                return -1

    def find_round_winner(self):
        """Find the winner of the current round"""
        if not self.played_cards_this_round:
            return None
            
        winner_index = 0
        winner_card = self.played_cards_this_round[0][1]
        
        for i in range(1, len(self.played_cards_this_round)):
            comparison = self.compare_cards(winner_card, self.played_cards_this_round[i][1])
            if comparison == -1:
                winner_index = i
                winner_card = self.played_cards_this_round[i][1]
        
        return self.played_cards_this_round[winner_index][0]

    def can_play_spread(self, player, card):
        """Check if player can play a spread card (different suit from leading suit)"""
        if self.leading_suit is None:
            return False  # First player can't play spread
            
        card_suit = card[0]
        return card_suit != self.leading_suit

    def has_leading_suit_card(self, player):
        """Check if player has any card of the leading suit"""
        if self.leading_suit is None:
            return True  # First player, no restriction
            
        for card in player.on_hand_cards:
            if card[0] == self.leading_suit:
                return True
        return False

    def get_valid_cards(self, player):
        """Get list of valid cards player can play"""
        if self.leading_suit is None:
            return player.on_hand_cards  # First player can play any card
            
        if self.has_leading_suit_card(player):
            # Must play leading suit
            return [card for card in player.on_hand_cards if card[0] == self.leading_suit]
        else:
            # Can play any card (spread)
            return player.on_hand_cards

    def play_user_turn(self, player):
        """Handle user's card selection"""
        # print(f"\n🃏 Your turn!")
        # print(f"Leading suit: {self.leading_suit if self.leading_suit else 'None (you set it)'}")
        
        valid_cards = self.get_valid_cards(player)
        emojis = cte(*player.on_hand_cards)
        
        # print("\nYour cards:")
        # for i, (card, emoji) in enumerate(zip(player.on_hand_cards, emojis)):
        #     marker = "  ✅ " if card in valid_cards else "  ❌ "
        #     print(f"  {i}: {emoji}  = {marker}")
        

        print("\nYour cards:")
        line = ""
        for i, (card, emoji) in enumerate(zip(player.on_hand_cards, emojis)):
            marker = "✅" if card in valid_cards else "❌"
            line += f"  {emoji}  "  # add spaces for separation
        print(line)


        while True:
            try:
                card_index = int(input(f"\nChoose a card (0-{len(player.on_hand_cards)-1}): "))
                if 0 <= card_index < len(player.on_hand_cards):
                    chosen_card = player.on_hand_cards[card_index]
                    if chosen_card in valid_cards:
                        emoji = cte(chosen_card)[0]
                        print(f"🧒 You play: {emoji}")
                        break
                    else:
                        print("❌ You must follow the leading suit if you have it!")
                else:
                    print("❌ Invalid index!")
            except ValueError:
                print("❌ Please enter a number!")
        
        return chosen_card

    def play_bot_turn(self, player):
        """Handle bot's card selection"""
        valid_cards = self.get_valid_cards(player)
        
        # Simple strategy: play the lowest valid card
        chosen_card = valid_cards[0] if valid_cards else player.on_hand_cards[0]
        
        emoji = cte(chosen_card)[0]
        print(f"🧒 {player.username} plays: {emoji}")
        time.sleep(1)
        
        return chosen_card

    def play_round(self):
        """Play one complete round"""
        self.played_cards_this_round = []
        self.leading_suit = None
        
        # Determine first player
        first_player = self.who_will_play_first()
        current_player = first_player
        
        # Find index of first player
        for i, player in enumerate(self.players):
            if player == first_player:
                self.current_player_index = i
                break
        
        print(f"\n{'='*50}")
        print(f"🔄 Round starting! Cards remaining: {len(self.user.on_hand_cards)}")
        print(f"{'='*50}")
        
        # Play turns for all 4 players
        for turn in range(4):
            player = current_player
            
            if player.on_hand_cards:
                # Get card from player
                if player.username == "user":
                    chosen_card = self.play_user_turn(player)
                else:
                    chosen_card = self.play_bot_turn(player)
                
                # # Set leading suit if first player
                # if self.leading_suit is None:
                #     self.leading_suit = chosen_card[0]
                #     print(f"🎯 Leading suit set to: {self.leading_suit}")
                
                # Play the card
                self.played_cards_this_round.append((player, chosen_card))
                player.on_hand_cards.remove(chosen_card)
                self.board_cards.append(chosen_card)
            
            # Move to next player
            current_player = self.get_next_player()
        
        # Determine round winner
        round_winner = self.find_round_winner()
        if round_winner:
            round_winner.total_win += 1
            self.last_winner = round_winner
            
            # Update won_last_round status
            for player in self.players:
                player.won_last_round = (player == round_winner)
            
            print(f"\n🎉 {round_winner.username.capitalize()} wins the round!")
            print(f"🏆 Total wins - {round_winner.username}: {round_winner.total_win}")
        
        return True

    def play(self):
        """Main game loop"""
        print("🎴 Starting the Card Game!")
        print("💡 Rule: You must follow the leading suit if you have it!")
        time.sleep(2)
        
        round_number = 1
        while all(len(player.on_hand_cards) > 0 for player in self.players):
            if not self.play_round():
                break
            round_number += 1
            time.sleep(2)
        
        # Game over
        self.display_final_results()

    def display_final_results(self):
        """Show final game results"""
        print(f"\n{'='*60}")
        print("🏁 GAME OVER! 🏁")
        print(f"{'='*60}")
        
        # Find winner(s)
        max_wins = max(player.total_win for player in self.players)
        winners = [player for player in self.players if player.total_win == max_wins]
        
        if len(winners) == 1:
            print(f"🎊 CHAMPION: {winners[0].username.upper()} with {max_wins} wins! 🎊")
        else:
            print(f"🤝 It's a tie! Winners: {', '.join(w.username for w in winners)} with {max_wins} wins each!")
        
        print(f"\n📊 Final Scores:")
        for player in sorted(self.players, key=lambda p: p.total_win, reverse=True):
            print(f"  {player.username.capitalize()}: {player.total_win} wins")
        
        print(f"{'='*60}")