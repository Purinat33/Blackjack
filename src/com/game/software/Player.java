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
            sum += this.hands.get(i).getValue();
        }
        return sum;
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


}
