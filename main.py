import deck

if __name__ == '__main__':
    poker = deck.Deck()
    poker.print_deck()
    poker.shuffle()
    print('-----------')
    poker.print_deck()