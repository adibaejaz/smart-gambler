from twoplayer import play as two_play


def game_stats(game, m=1000, a=50, b=100, p=0.51, double_down=False):
    num_ended, num_won, pdoc = 0, 0, {}
    for x in range(50):
        res = game(m, a, b, p, double_down)
        if res[0]:
            num_ended += 1
            if res[-1][-1]:
                num_won += 1
    pdoc.update({"number of games finished": num_ended,
                 "number of games won": num_won,
                 "probability of success": float(num_won) / float(num_ended)
                 })
    return pdoc


if __name__ == '__main__':
    stats = game_stats(two_play)
    for k, v in stats.items():
        print(k, v)



