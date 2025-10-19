from Game import Game


def main():

    game = Game(
        size=(1000, 800),
        caption="Tic Tac Toe by rohithvp",
        fps=60
    )

    game.start_loop()


if __name__ == "__main__":
    main()
