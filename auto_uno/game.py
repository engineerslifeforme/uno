""" Game Manager """

from auto_uno.actions import RequiredActions
from auto_uno.cards import Deck, WildCard, ReverseCard, SkipCard, DrawTwoCard, WildDrawFourCard, Card
from auto_uno.player import NaivePlayer

class Game:

    def __init__(self, players: int):
        assert(players > 1), "At least 2 players required"
        assert(players < 11), "Maximum of 10 players allowed"
        print(f"Executing game with {players} players")
        self.deck = Deck()
        initial_hands = self.deal(players)
        self.players = [NaivePlayer(hand) for hand in initial_hands]
        self.discard_pile = [self.deck.draw()]

    @property
    def top_card(self) -> Card:
        return self.discard_pile[-1]

    def play(self):        
        turn_index = 0
        increment = 1        
        previous_action = None
        turns = 0

        if issubclass(type(self.top_card), ReverseCard):
            increment = -1
        elif issubclass(type(self.top_card), DrawTwoCard):
            previous_action = RequiredActions.DRAW_TWO
        elif issubclass(type(self.top_card), SkipCard):
            turn_index += increment
        elif issubclass(type(self.top_card), WildDrawFourCard):
            self.deck.cards.append(self.top_card)
            self.deck.shuffle()
            self.discard_pile = [self.draw()]
            self.play()
            return
        elif issubclass(type(self.top_card), WildCard):
            self.top_card.color = self.players[turn_index].choose_color_initial_wild()


        while True:
            turns += 1
            if turns > 1000:
                print('Game took too long (> 1000 turns)')
                break
            print(f"Turn #{turns}")
            print(f"Top Card: {self.top_card}")
            player_index = turn_index % len(self.players)
            active_player = self.players[player_index]
            print(f"Player {player_index} Hand: {active_player}")
            extra_cards = None
            if previous_action is not None:
                if previous_action == RequiredActions.DRAW_TWO:
                    extra_cards = [self.draw() for _ in range(2)]
                elif previous_action == RequiredActions.DRAW_FOUR:
                    extra_cards = [self.draw() for _ in range(4)]
                active_player.hand.extend(extra_cards)
                previous_action = None
            else:
                played_card = active_player.execute_turn(self.top_card)
                if played_card is None:
                    drawn_card = self.draw()
                    print(f"Player {player_index} draws {drawn_card}")
                    active_player.hand.append(drawn_card)
                    played_card = active_player.post_card_drawn(self.top_card)
                if played_card is not None:
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

    def draw(self) -> Card:
        try:
            return self.deck.draw()
        except IndexError:
            top_card = self.discard_pile.pop()
            self.deck.cards = self.discard_pile.copy()
            self.deck.shuffle()
            self.discard_pile = [top_card]
            return self.draw()