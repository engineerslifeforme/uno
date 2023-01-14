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

# TODO

1. Provide player additional info
    
    - Quantity of cards in opponents hands
    - Recent/All cards previous played

2. Reshuffle the deck if empty