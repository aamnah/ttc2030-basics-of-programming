def print_deck(deck):
    new_deck = deck
    pointer = 13
    # make it look pretty
    # Add a line break after every 13 items (one suit has 13 cards)
    # basically print every suit on it's own line
    for i in range (1,5): # 5 not included, will run four times
        new_deck.insert(pointer, '\n')
        pointer += (13 + 1) # 13, 27, 41, 55 (the list will be displaced by 1 because of the new item we added)

    for index, i in enumerate(new_deck):
        if i != "\n":
            print(i, end = " ")
        else: print(i)