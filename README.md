# Uno

Recreating uno for the purpose of testing different play approaches.

# Running

```
python run.py PLAYER_QUANTITY
```

e.g.

```
python run.py 2
python run.py 3
```

# Tests

```
python -m pytest tests
```

# Rules

## Basic Rules

[Mattel Uno Rules](https://service.mattel.com/instruction_sheets/42001pr.pdf)

## Rules of Note

1. Wild cards can be played on wild cards
2. Draw 4 cannot be played if you have the COLOR of the card on top of
   the card on top of the discard pile.
3. You can choose not to play a card even if you have one that is
   playable, BUT you must draw a card.  You do not have to play this
   card either.
4. The initial card takes effect on the first player according to the
   rules with the exception of the Draw 4 which causes a reshuffle
   (This is exactly per the rules).

# New Player Type Design

`NaivePlayer` in `player.py` attempts to demonstrate the most minimal
player example that follows the rules.

## Required

New players must inherit from `PlayerPrototype`, i.e.:

```
class AwesomePlayer(PlayerProtoype):
   ...
```

A new player must implement the `select_card` method which can
return a card (or None).  All returned cards must followed the
rules and will be verified.

## Optional

### Select Card After Drawing

`PlayerPrototype` by default simply executes `select_card` again
after drawing when no card was selected (i.e. return of `None`).
You can optionally implement an alternate version of
`select_card_after_draw` to modify this behavior.

### Choosing Initial Color if first Card is Wild

If a WildCard (not draw 4) is the first card in the discard pile,
the first player MUST select the starting color.  `PlayerPrototype`
by default will select the color which has the most cards in the
hand.  Random in the case of a tie of the highest quantity color.
`choose_color_initial_wild` can be re-written to modify this
behavior.

# TODO

1. Provide player additional info
    
    - Quantity of cards in opponents hands
    - Recent/All cards previous played

