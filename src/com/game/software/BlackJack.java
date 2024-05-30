package com.game.software;

import java.util.Scanner;

public class BlackJack {
    public static void welcome(){
        System.out.println("Welcome to BlackJack");
        System.out.println("v1:");
        System.out.println("Only card with face values");
        System.out.println("---------------------------");
    }

    public static Player getWinner(Player p1, Player p2){

        System.out.println(p1.getUsername() + "'s Value: " + p1.handValue());
        System.out.println(p2.getUsername() + "'s Value: " + p2.handValue());
        if(p1.handValue() > p2.handValue() && p1.handValue() <= 21){
            return p1;
        } else if (p2.handValue() > p1.handValue() && p2.handValue() <= 21) {
            return p2;
        } else if(p2.handValue() > 21 && p1.handValue() <= 21){
            return p1;
        }
        else if(p1.handValue() > 21 && p2.handValue() <= 21){
            return p2;
        }
        else return new Player("Draw");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String choice;

        welcome();
        System.out.println("Init Card");
        Deck.createDeck();
        Deck.printDeck();
        System.out.println("Total Cards: " + Deck.getDeck().size());
        System.out.println("------------");
        System.out.println("Shuffle Card");
        for(int i = 0 ; i < 20; i++){
            Deck.shuffle();
            Deck.shuffle();
        }
        System.out.println("----------");
        Player p1 = new Player("P1");
        p1.draw();
        p1.draw();
        while (true){
            System.out.println(p1);
            if (p1.handValue() >= 21){
                break;
            }

            System.out.print("Hit or Stand?: ");
            choice = sc.nextLine();
            choice = choice.toUpperCase();
            if(choice.contains("H") || choice.contains("HIT")){
                p1.draw();
            }
            else if(choice.contains("S") || choice.contains("STAND")){
                break;
            }
            else{
                System.out.println("Error try again");
            }

        }
        System.out.println("---------------------");


        Bot bot = new Bot("bot");
        bot.play();
        System.out.println(bot);
        System.out.println("-------------------------------");
        Player winner = getWinner(p1, bot);
        System.out.println("The winner is: " + winner.getUsername());


        sc.close();
    }
}
