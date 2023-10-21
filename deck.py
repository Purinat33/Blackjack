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
        
    
    def card_score(self, card: (str, str)): #Score of a particular card
        # In the end we will ignore ace
        card_score = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
        rank = card[0]
        return card_score[rank]
    
    
    def calculate_ace(self, hand_score):
        if (hand_score + 11) > 21:
            # If we add and it goes over 21 then just add 1 
            return 1
        else:
            return 11
        
    
    def hand_score(self): # List of cards on hand (Score of all cards on hand)
        # If theres an ace, swap it with the last element of the list
        score = 0
        non_ace = []
        ace_list = []
        
        for i in range(len(self.hands)):
            card = self.hands[i]
            if card[0] != 'Ace':
                non_ace.append(self.hands[i])
            else:
                ace_list.append(self.hands[i])
                
        
        for card in non_ace:
            score += self.card_score(card) 
            
        if len(ace_list) > 0:
            # Add ace point to each element
            for card in ace_list:
                score += self.calculate_ace(score)
           
        return score
    
    
    def print_hand(self): # Print the entire hand
        # print in box format, Card on top, score on the bottom
        non_ace = []
        ace = []
        print(f'---{self.name}\'s hands---')
        for card in self.hands:
            print(f'{card[0]} of {card[1]}\t|')
            if card[0] != 'Ace':
                non_ace.append(card)
                print(f'{self.card_score(card)}\t\t|')
            else:
                ace.append(card)
                print(f'1 or 11\t\t|')
                
            print(f'--------------------')
            
        # print total hand score
        non_ace_score = 0
        for card in non_ace:
            non_ace_score += self.card_score(card)
        
        ace_score = 0
        if len(ace) > 1:
            # Both can't be 11 since it will be over 21
            for card in ace:
                ace_score += 1
        else:
            for card in ace:
                # Check non_ace_scre
                # if sum > 21 then just 1
                if non_ace_score + 11 > 21:
                    ace_score += 1
                else:
                    ace_score += 11
                    
        
        print(f'--------------------')
        print(f'Total (Excluding_Ace): {non_ace_score}')
        print(f'Total (Ace Only): {ace_score}')
        print(f'--------------------')
        print(f'Total: {ace_score + non_ace_score}')
        print(f'--------------------')

        
class Blackjack:
    def __init__(self) -> None:
        pass
        
        
        
    