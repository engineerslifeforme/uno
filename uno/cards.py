""" Cards """

from enum import Enum
from random import shuffle

class Card:
    pass

    def allowed(self, other) -> bool:
        raise(NotImplemented())

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4


class ColorCard(Card):
    
    def __init__(self, color: Color = None):
        self.color = color

    def allowed(self, other: Card) -> bool:
        result = False
        if issubclass(ColorCard, type(other)):
            result = other.color == self.color
        return result


class NumberCard(ColorCard):
    
    def __init__(self, number: int = None, **kwargs):
        assert (number is not None), "Number must be provided!"
        self.number = number
        super().__init__(**kwargs)

    def allowed(self, other: Card) -> bool:
        result = super().allowed(other)
        if issubclass(NumberCard, type(other)):
            result |= self.number == other.number
        return result

    def __repr__(self):
        return f"{self.color} {self.number}"

class SpecialColorCard(ColorCard):
    special = "None"

    def allowed(self, other: Card) -> bool:
        result = super().allowed(other)
        return result or (type(self) == type(other))

    def __repr__(self):
        return f"{self.color} {self.special}"

class DrawTwoCard(SpecialColorCard):
    special = "Draw Two"

class ReverseCard(SpecialColorCard):
    special = "Reverse"

class SkipCard(SpecialColorCard):
    special = "Skip"

class WildCard(ColorCard):

    def __init__(self):
        self.color = None
    
    def allowed(self, other: Card) -> bool:
        return True

    def __repr__(self) -> str:
        return f"Wild ({self.color})"

class WildDrawFourCard(WildCard):
    def __repr__(self) -> str:
        return f"Wild Draw Four ({self.color})"

class Deck:

    def __init__(self):
        self.cards = self.create_deck()
        shuffle(self.cards)

    def create_deck(self) -> list:
        cards = []
        for color in [Color.BLUE, Color.GREEN, Color.RED, Color.YELLOW]:
            for _ in range(2):            
                for number in range(1,10):
                    cards.append(NumberCard(number=number, color=color))
                cards.append(SkipCard(color=color))
                cards.append(ReverseCard(color=color))
                cards.append(DrawTwoCard(color=color))
            cards.append(NumberCard(number=0, color=color))
        for _ in range(4):
            cards.append(WildCard())
            cards.append(WildDrawFourCard())
        return cards

    def draw(self) -> Card:
        return self.cards.pop()

        
