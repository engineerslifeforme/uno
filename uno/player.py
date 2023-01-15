""" Uno Player """

from cards import Card, WildCard, ColorCard, Color, WildDrawFourCard
from actions import RequiredActions

class PlayerProtype:

    def __init__(self, initial_hand: list):
        self.hand = initial_hand

    def execute_turn(self, top_card: Card) -> Card:
        selected_card = self.select_card(top_card)
        if selected_card is not None:
            assert(selected_card.allowed(top_card)), f"{select_card} cannot be placed on {top_card}"
            if issubclass(type(selected_card), WildDrawFourCard) and issubclass(type(top_card), ColorCard):
                hand_colors = [card.color for card in self.hand if issubclass(type(card), ColorCard)]
                assert(top_card.color not in hand_colors), "Cannot play Draw 4 wild if you have the color"

        return selected_card
    
    def select_card(top_card: Card) -> Card:
        raise(NotImplementedError())

    @property
    def win(self) -> bool:
        return len(self.hand) == 0

    def __repr__(self) -> str:
        return '\n-'.join([str(card) for card in self.hand])

    def choose_color_initial_wild(self) -> Color:
        color_counts = {}
        for card in self.hand:
            try:
                this_color = card.color
                if this_color not in color_counts:
                    color_counts[this_color] = 1
                else:
                    color_counts[this_color] += 1
            except AttributeError:
                continue
        max_color = None
        max_count = 0
        for color, quantity in color_counts.items():
            if quantity > max_count:
                max_color = color
                max_count = quantity
        return max_color

class NaivePlayer(PlayerProtype):
    def select_card(self, top_card: Card) -> Card:        
        selected_card = None
        draw_four_card = None
        for card in self.hand:
            if issubclass(type(card), WildDrawFourCard):
                draw_four_card = card
                continue
            elif card.allowed(top_card):
                selected_card = card
        if selected_card is None and draw_four_card is not None:
            selected_card = draw_four_card
        if selected_card is not None:
            self.hand.remove(selected_card)
            if issubclass(type(selected_card), WildCard):
                for card in self.hand:
                    if issubclass(type(card), ColorCard):
                        selected_card.color = card.color
                        break

        return selected_card
        