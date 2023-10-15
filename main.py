import deck

if __name__ == '__main__':
    poker = deck.Deck()
    poker.print_deck()
    poker.shuffle()
    print('-----------')
    poker.print_deck()
    
    john = deck.Player()
    # john.print_hand()
    john.hands.append(('Ace', 'Hearts'))
    john.hands.append(('2', 'Clubs'))
    john.hands.append(('10', 'Spades'))
    john.print_hand()