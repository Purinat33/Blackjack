import random


class Deck: # I think this class can pretty much be used with other games as well like poker? 
    # 4 suits: Spades, Clubs, Diamonds, Hearts
    # 13 ranks(?) each: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
    
    def __init__(self):
        self.suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']       
        self.cards = [(rank, suit) for rank in self.ranks for suit in self.suits]
    

    def print_deck(self):
        # We are not really using this function in the game really
        # Because we only wants to show only cards on each player's hand
        count = 0
        for card in self.cards:
            print(f'{card[0]} of {card[1]}', end='\t')
            count += 1
            if count == 4:
                print()
                count = 0
                           
    def shuffle(self):
        random.shuffle(self.cards)
        
    
    def deal_card(self, isFaceUp: bool) -> (str, str):
        if isFaceUp:
            drawn_card = self.cards.pop()
            print("Dealt: ", drawn_card)
            return drawn_card
        else:
            print("Dealth a card")
            return self.cards.pop()
    
    
class Player:
    
    def __init__(self):
        self.score = 0 # This will be useful when counting later
        self.hands = []
        self.name = 'Player'
        
    def hand_score(self): # List of cards on hand (Score of all cards on hand)
        score = 0
        card_score = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
        for card in self.hands:
            rank = card[0]
            score += card_score[rank]
        
        return score    
    
    
    def card_score(self, card: (str, str)): #Score of a particular card
        card_score = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
        rank = card[0]
        return card_score[rank]
    
    
    def calculate_ace(self):
        # Ace is either 1 or 11 based on the circumstance (Should probably fix scoring system afterward)
        pass

    
    def print_hand(self): # Print the entire hand
        # print in box format, Card on top, score on the bottom
        print(f'---{self.name}\'s hands---')
        for card in self.hands:
            print(f'{card[0]} of {card[1]}\t|')
            print(f'{self.card_score(card)}\t\t|')
            print(f'--------------------')
            
        # print total hand score
        print(f'--------------------')
        print(f'Total: {self.hand_score()}')
        print(f'--------------------')
        
        
        
    