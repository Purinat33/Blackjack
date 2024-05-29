package com.game.software;

public class Card {

    public int getValue(){
        return switch (this.getName()) {
            case "A" -> 1; // This needs fixing later
            case "2" -> 2;
            case "3" -> 3;
            case "4" -> 4;
            case "5" -> 5;
            case "6" -> 6;
            case "7" -> 7;
            case "8" -> 8;
            case "9" -> 9;
            case "10", "J", "Q", "K" -> 10;
            default -> -1;
        };
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSuit() {
        return suit;
    }

    public void setSuit(String suit) {
        this.suit = suit;
    }

    public Card(String name, String suit) {
        this.name = name;
        this.suit = suit;
    }

    private String name;
    private String suit;


    @Override
    public String toString() {
        return "Card{" +
                "name='" + name + '\'' +
                ", suit='" + suit + '\'' +
                '}';
    }
}
