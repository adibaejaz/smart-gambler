# smart-gambler
A simulation of the gambler's ruin problem: the traditional set-up with 2 players, as well as a general solution in 
n players.

You will ruin yourself because the house always wins – and this game will help you simulate that feeling of loss
 virtually!
 
## Inspiration
This summer, I took part in a probability theory reading seminar under Dr. Xuan Wu, a postdoc att the University of 
Chicago, alongside 2 other college students.

We surveyed topics such as the monkey at the cliff, transience and recurrence in simple random walks, and Markov chains.

One of the 3 presentations I gave was on something called the gambler's ruin problem. Around this time, I also watched 
the movies *Casino*, *21*, and *The Big Short*.

Naturally, I've been feeling like losing some money. 

PS Notes for the seminar and recordings of my talks are available upon request.

## Problem statement

### Traditional 2-player set up 

A gambler **G** starts with $ *i* and decides to stop playing after m rounds. The gambler's opponent, **O**, on the other 
hand, has $f – when playing against the house, f is usually several times i.
With each round, **G** either gains or loses a constant bet amount, usually $1, with fixed probabilities 
p and 1-p respectively. **G** can also choose to 'double down', i.e. double the bet amount when **G** wins and halve it
when **G**  loses.
The game ends when either **G** or **O** has 0 dollars remaining.

### My extensions
* What happens when we generalize to n players?
* What happens when the probability of success depends on the immediately previous outcome?


