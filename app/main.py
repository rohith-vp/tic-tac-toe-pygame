from Game import Game


def main():
    # Initialize the game window with custom size, title, and frame rate
    game = Game(
        size=(1000, 800),
        caption="Tic Tac Toe by rohithvp",
        fps=60
    )

    # Start the main game loop
    game.start_loop()


if __name__ == "__main__":
    # Run the game only if this script is executed directly
    main()
