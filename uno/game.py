""" Game Manager """

from actions import RequiredActions
from cards import Deck, WildCard, ReverseCard, SkipCard, DrawTwoCard, WildDrawFourCard
from player import NaivePlayer

class Game:

    def __init__(self, players: int):
        self.deck = Deck()
        initial_hands = self.deal(players)
        self.players = [NaivePlayer(hand) for hand in initial_hands]
        self.discard_pile = [self.deck.draw()]
        while type(self.discard_pile[-1]) == WildCard:
            self.discard_pile.append(self.deck.draw())
        
        turn_index = 0
        increment = 1
        previous_action = None
        turns = 0
        while True:
            turns += 1
            print(f"Top Card: {self.discard_pile[-1]}")
            player_index = turn_index % players
            active_player = self.players[player_index]
            print(f"Player {player_index} Hand: {active_player}")
            extra_cards = None
            if previous_action is not None:
                if previous_action == RequiredActions.DRAW_TWO:
                    extra_cards = [self.deck.draw() for _ in range(2)]
                elif previous_action == RequiredActions.DRAW_FOUR:
                    extra_cards = [self.deck.draw() for _ in range(4)]
            played_card = active_player.execute_turn(self.discard_pile[-1], extra_cards=extra_cards)
            if played_card is None:
                drawn_card = self.deck.draw()
                print(f"Player {player_index} draws {drawn_card}")
                active_player.hand.append(drawn_card)
            else:
                print(f"Player {player_index} played {played_card}")
                self.discard_pile.append(played_card)
                played_card_type = type(played_card)
                previous_action = None
                if played_card_type == ReverseCard:
                    increment *= -1
                elif played_card_type == DrawTwoCard:
                    previous_action = RequiredActions.DRAW_TWO
                elif played_card == WildDrawFourCard:
                    previous_action = RequiredActions.DRAW_FOUR
                elif played_card == SkipCard:
                    turn_index += increment
            if active_player.win:
                print(f"Player {player_index} Wins!")
                break
            turn_index += increment
        print(f"Turns played: {turns}")
    
    def deal(self, player_quantity: int) -> list:
        hands = [[] for _ in range(player_quantity)]
        for _ in range(7):
            for hand in hands:
                hand.append(self.deck.draw())
        return hands