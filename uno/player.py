""" Uno Player """

from cards import Card, WildCard, ColorCard
from actions import RequiredActions

class PlayerProtype:

    def __init__(self, initial_hand: list):
        self.hand = initial_hand

    def execute_turn(self, top_card: Card, extra_cards: list = None) -> Card:
        if extra_cards is not None:
            self.hand.extend(extra_cards)
        selected_card = self.select_card(top_card)
        if selected_card is not None:
            assert(selected_card.allowed(top_card)), f"{select_card} cannot be placed on {top_card}"
        return selected_card
    
    def select_card(top_card: Card) -> Card:
        raise(NotImplementedError())

    @property
    def win(self) -> bool:
        return len(self.hand) == 0

    def __repr__(self) -> str:
        return '\n-'.join([str(card) for card in self.hand])

class NaivePlayer(PlayerProtype):
    def select_card(self, top_card: Card) -> Card:        
        selected_card = None
        for card in self.hand:
            if card.allowed(top_card):
                selected_card = card
        if selected_card is not None:
            self.hand.remove(selected_card)
            if issubclass(type(selected_card), WildCard):
                for card in self.hand:
                    if issubclass(type(card), ColorCard):
                        selected_card.color = card.color
                        break
        return selected_card
        