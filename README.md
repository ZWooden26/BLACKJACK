# BLACKJACK
Blackjack is a classic casino card game, in which each player (if there are multiple) is competing against the house to win money, and the rules are as follows:
To join the game, a player must throw chips (money) into the pot.  To do this, simply raise or lower your bet using the up and down arrows.
Once you have set your bet, you cannot change it until a result has been decided, so bet carefully.
Cards can now be dealt, two to each player and two to the house.  House cards are shown one face down and one face up, but player cards are both face up.  To deal cards, hit TAB.
Once you see your cards, decide if you want to HIT (space) or STAY ("s").  The goal is to beat the house's hand (have a greater cad value) without going over 21.
Numbered cards hold their own value, while face cards are all worth 10 and aces are worth either 1 or 11. 
For simplicity within this game, aces are assumed to be 11 unless your value is above 21, then they are pushed down to 1.
After the player chooses to stay, the house will have a turn to manipulate their hand by hitting or staying, which happens automatically in this game.
Traditionally, the house must hit on any value less than 17, which is the same in this iteration.
If the player wins they get paid out 2:1 their original bet, if they hit blackjack (value = 21) they get paid out 3:1, if they tie the payout is 1:1, and if you lose your money is gone.
If you are a smart gambler, you will cashout ("q") while you're ahead.  Have fun!

---- credits ----
Sean Milanette helped me come up with some of the graphics and the gameplay functions, such as moving chips between the player's stack and the pot.
Andrew Galvan-Arrien showed me how to continuously blit images, so that they remain on screen after a button is pressed.
CAPT Severson suggested the pygame.display.update function which I used extensively, and it allowed my code to run much more smoothly and made for a better user experience.
My sprites came from this website: https://www.kenney.nl/assets
My sounds are downloaded from various royalty-free websites
A significant source of code inspiration and direction came from here: https://www.pygame.org/docs/ref/display.html
