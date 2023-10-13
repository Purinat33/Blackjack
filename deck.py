import random


class Deck:
    # 4 suits: Spades, Clubs, Diamonds, Hearts
    # 13 ranks(?) each: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
    
    def __init__(self):
        self.suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']       
        self.cards = [(rank, suit) for rank in self.ranks for suit in self.suits]
    

    def print_deck(self):
        count = 0
        for card in self.cards:
            print(f'{card[0]} of {card[1]}', end='\t')
            count += 1
            if count == 4:
                print()
                count = 0
                           
    def shuffle(self):
        random.shuffle(self.cards)
    
    
class Player:
    def __init__(self):
        self.score = 0 # This will be useful when counting later?
        self.hands = []
        
        
    