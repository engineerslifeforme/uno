""" Tests for player """

import pytest

from auto_uno.player import NaivePlayer
from auto_uno.cards import NumberCard, Color, WildDrawFourCard, ColorCard

def test_execute_turn():
    card = NumberCard(number=1, color=Color.BLUE)
    player = NaivePlayer([card])
    selected_card = player.execute_turn(NumberCard(number=2, color=Color.BLUE))
    assert(selected_card == card)

def test_turn():
    card = NumberCard(number=1, color=Color.BLUE)
    player = NaivePlayer([card])
    selected_card = player.turn(NumberCard(number=2, color=Color.BLUE), player.select_card)
    assert(selected_card == card)

def test_post_card_drawn():
    card = NumberCard(number=1, color=Color.BLUE)
    player = NaivePlayer([card])
    selected_card = player.post_card_drawn(NumberCard(number=2, color=Color.BLUE))
    assert(selected_card == card)

def test_select_card_after_draw():
    card = NumberCard(number=1, color=Color.BLUE)
    player = NaivePlayer([card])
    selected_card = player.select_card_after_draw(NumberCard(number=2, color=Color.BLUE))
    assert(selected_card == card)

def test_select_card():
    card = NumberCard(number=1, color=Color.BLUE)
    player = NaivePlayer([card])
    selected_card = player.select_card(NumberCard(number=2, color=Color.BLUE))
    assert(selected_card == card)

def test_win():
    player = NaivePlayer([])
    assert(player.win)
    player = NaivePlayer([1])
    assert(not player.win)

def test_choose_color_initial_wild():
    player = NaivePlayer([ColorCard(color=Color.BLUE)])
    assert(player.choose_color_initial_wild() == Color.BLUE)

    player.hand.extend(2*[ColorCard(color=Color.RED)])
    chosen_color = player.choose_color_initial_wild()
    assert(chosen_color == Color.RED)

    player.hand.extend(2*[ColorCard(color=Color.BLUE)])
    assert(player.choose_color_initial_wild() == Color.BLUE)

def test_verify_selection():
    player = NaivePlayer([])
    
    # Nothing to verify if players does not play a card
    player.verify_selection(None, None)
    
    # Player must play a card that can be played
    with pytest.raises(AssertionError):
        player.verify_selection(
            NumberCard(number=1, color=Color.BLUE),
            NumberCard(number=2, color=Color.GREEN),
        )
    # OK
    player.verify_selection(
        NumberCard(number=1, color=Color.BLUE),
        NumberCard(number=1, color=Color.GREEN),
    )

    # Can't play draw 4 if have color in hand
    player.hand = [NumberCard(number=3, color=Color.GREEN)]
    with pytest.raises(AssertionError):
        player.verify_selection(
            WildDrawFourCard(),
            NumberCard(number=2, color=Color.GREEN),
        )
    # OK
    player.verify_selection(
        WildDrawFourCard(),
        NumberCard(number=2, color=Color.BLUE),
    )
    