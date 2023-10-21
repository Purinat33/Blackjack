import deck

if __name__ == '__main__':
    poker = deck.Deck()
    for i in range(5):
        poker.shuffle() 
    
    dealer = deck.Player()