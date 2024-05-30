package com.game.software;

import java.util.ArrayList;

public class Player {
    public String getUsername() {
        return username;
    }

    private final String username;
    private ArrayList<Card> hands;
    public Player(String username){
        this.username = username;
        this.hands = new ArrayList<>();
    }

    public void draw(){
        hands.add(Deck.draw());
    }

    public int handValue(){

        int sum = 0;
        for (int i = 0 ; i <hands.size();i++){
            if(!this.hands.get(i).getName().equals("A"))
                sum += this.hands.get(i).getValue();
            else{
                if(sum + 11 <= 21) {
                    // If Ace is 11, and it wouldn't go past 21 then that ace is 11
                    sum += 11;
                }
                else{
                    sum += 1;
                }
            }
        }
        return sum;
    }

    public ArrayList<Card> getHands(){
        return this.hands;
    }

    @Override
    public String toString() {
        // Show cards and value
        StringBuilder val = new StringBuilder();
        for(int i = 0 ; i < this.hands.size(); i++){
            val.append(this.hands.get(i).toString());
            val.append('\n');
        }

        val.append("Total Value: ").append(this.handValue());
        return val.toString();
    }

    public void testHand(){
        Card card = new Card("A", "Spades");
        Card card2 = new Card("A", "Hearts");
        Card card3 = new Card("A", "Clubs");
        // Expected = 12?
        this.hands.add(card);
        this.hands.add(card2);
        this.hands.add(card3);
        System.out.println(this);
    }

}
