package com.game.software;

public class Bot extends Player{
    public Bot(String username) {
        super(username);
    }

    // The new state-of-the-art AI that surpasses OpenIA
    public void play(){
        this.draw();
        this.draw();
        while (true){
            if(this.handValue() < 21){
                this.draw();
            }
            else {
                break;
            }
        }
    }
}
