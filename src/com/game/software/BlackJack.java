package com.game.software;

public class BlackJack {
    public static void welcome(){
        System.out.println("Welcome to BlackJack");
        System.out.println("v1:");
        System.out.println("Only card with face values");
        System.out.println("---------------------------");
    }

    public static Player getWinner(Player p1, Player p2){
        return p1.handValue()>p2.handValue()?p1:p2; // Suppose to be 21 and more logic but Ill do it LATER
    }

    public static void main(String[] args) {
        welcome();
        System.out.println("Init Card");
        Deck.createDeck();
        Deck.printDeck();
        System.out.println("Total Cards: " + Deck.getDeck().size());
        System.out.println("------------");
        System.out.println("Shuffle Card");
        Deck.shuffle();
        System.out.println("----------");
        Player p1 = new Player("P1");
        p1.draw();
        p1.draw();
        System.out.println(p1);

        Player bot = new Player("Bot");
        bot.draw();
        bot.draw();
        System.out.println(bot);

        Player winner = getWinner(p1, bot);
        System.out.println("The winnder is: " + winner.getUsername());
    }
}
