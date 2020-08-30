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


def play(m=1000, a=50, b=100, p=0.5, double_down=False):
    count, wealth, vals, bet = m, float(a), [float(a)], 1.0
    # generate list of values outside of loop to avoid calling rand multiple times
    wins = choices(population=[True, False], weights=[p, 1-p], k=m)
    while 0 < wealth < a + b and count > 0:
        count -= 1
        if wins[count]:
            wealth += bet
            bet *= 2.0 if double_down else bet
        else:
            wealth -= bet
            bet *= 0.5 if double_down else bet
        vals.append(wealth)
    return True if count > 0 else False, m - count, vals


def display_result(ended, end_trial, vals):
    if ended:
        print("Your wealth:", vals[-1], "bottle caps.")
        print(f"The game ended on trial {end_trial}."
              f" {'You' if vals[-1] else 'We'} won. Too bad.")
    else:
        print(f"Game did not end within {end_trial} trials."
              f" You have {vals[-1]} bottle caps")
    plt.plot([i for i in range(end_trial + 1)], vals, label="current wealth", )
    avg_wealth = [vals[0] + float(sum(val - vals[0] for val in vals)) / len(vals)] * len(vals)
    plt.plot([i for i in range(end_trial + 1)], avg_wealth, label="average wealth")
    plt.title("two-player gambler's ruin")
    plt.xlabel("turn index")
    plt.ylabel("number of bottlecaps")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    args = subparser().parse_args()
    result = play(m=args.num, a=args.wealth, b=args.wealth * 2, p=args.probability, double_down=args.double_down)
    display_result(*result)
