import game_logic


if __name__ == "__main__":
    while True:
        game_logic.play_game()
        if not input("Do you want to play again (type 'yes')? ").lower().strip() == "yes":
            print("Good bye!")
            break

