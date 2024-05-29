package com.game.software;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class Deck {

    private static ArrayList<Card> deck = new ArrayList<>();
    public static ArrayList<Card> getDeck() {
        return deck;
    }

    // Game needs to create Deck
    public static void createDeck(){
        //loop through the 4 suit
        for(int i = 0 ; i < 4; i++){
            // loop through each 13 face
            for(int j = 0 ; j < Face.getFace().length; j++){
                deck.add(new Card(Face.getFace()[j], suit[i]));
            }
        }
    }


    // 13 face: A 2 3 - 10, J, Q, K
    // val = 1-10 (ignore Ace (1/11) for now)
    private static String[] suit = {"Clubs", "Diamond", "Heart", "Spade"};

    public static void printDeck(){
        for(int i = 0 ; i < deck.size(); i++){
            // loop through each face/name
            System.out.print(deck.get(i));
            System.out.print(" Value: ");
            System.out.print(deck.get(i).getValue());
            System.out.println();
        }
    }

    public static void shuffle(){
        //https://stackoverflow.com/questions/16112515/how-to-shuffle-an-arraylist
        Collections.shuffle(deck);
    }

    public static Card draw(){
        return deck.remove(0);
    }



}
