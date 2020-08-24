""""
    A simulation of typical gambler's ruin problem with two players.
    Allows the user to enter the probability of success, number of trials, and initial amount.
    Returns:
        - A plot of net earnings vs number of trials
        - Expected time to ruin
"""

import argparse
from random import choices
from matplotlib import pyplot as plt


def subparser():
    parser = argparse.ArgumentParser(description="gamble with another player.")
    parser.add_argument('-n', "--num", type=int, default=1000,
                        help="number of bets you want to make")
    parser.add_argument('-w', "--wealth", type=int, default=50,
                        help="your starting wealth")
    parser.add_argument('-p', "--probability", type=float, default=0.3,
                        help="your probability of success")
    parser.add_argument('-d', "--double-down", action="store_true",
                        help="double down bet on winning/losing")
    return parser

def play(n=1000, a=50, b=100, p=0.3, double_down=False):
    count, wealth, vals, bet = n, a, [a], 1
    # generate list of values outside of loop to avoid calling rand multiple times
    wins = choices(population=[True, False], weights=[p, 1-p], k=n)
    while 0 < wealth < a + b + 1 and count > 0:
        count -= 1
        if wins[count]:
            wealth += bet
        else:
            wealth -= bet
        bet *= 2 if double_down else bet
        vals.append(wealth)
    if count > 0:
        print("Your wealth:", wealth, "bottle caps.")
        print(f"The game ended on trial {n - count}."
              f" {'You' if wealth else 'We'} won. Too bad.")
        plt.plot([i for i in range(n - count + 1)], vals)
    else:
        print(f"Game did not end within {n} trials."
              f" You have {wealth} bottle caps")
        plt.plot([i for i in range(n+1)], vals)
    plt.show()


if __name__ == '__main__':
    args = subparser().parse_args()
    play(n=args.num, a=args.wealth, b=args.wealth * 2, p=args.probability, double_down=args.double_down)
