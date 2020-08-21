""""
    A simulation of typical gambler's ruin problem with two players.
    Allows the user to enter the probability of success, number of trials, and initial amount.
    Returns:
        - A plot of net earnings vs number of trials
        - Expected time to ruin
"""

from random import choices
from matplotlib import pyplot as plt

def play(n=1000, a=50, b=100, p=0.3):
    count, wealth, vals = n, a, [a]
    # generate list of values outside of loop to avoid calling rand multiple times
    wins = choices(population=[True, False], weights=[p, 1-p], k=n)
    while 0 < wealth < a + b + 1 and count > 0:
        count -= 1
        if wins[count]:
            wealth += 1
        else:
            wealth -= 1
        vals.append(wealth)
    if count > 0:
        print(f"The game ended on trial {n - count}."
              f" {'You' if wealth else 'We'} lost. Too bad.")
        plt.plot([i for i in range(n - count + 1)], vals)
    else:
        print(f"Game did not end within {n} trials."
              f" You have {wealth} bottle caps")
        plt.plot([i for i in range(n+1)], vals)
    plt.show()

play()