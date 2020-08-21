from GameLib.GameRunner import GameRunner

print("Welcome to tic-tac-toe")
game_runner = GameRunner()
print("Use this board to pick your position:")
print(game_runner.game.draw(False))

while True:
    current_player = game_runner.get_current_player()
    symbol = game_runner.get_current_player_symbol()
    try:
        position = int(input("Player " + str(current_player + 1) +
                             " enter your position [" + symbol + "]: "))
        valid = game_runner.take_turn(position)
        winner = game_runner.get_winner()
        print("Board state")
        print(game_runner.game.draw())
        if not valid or len(winner) > 0:
            print("Game Over!")
            print("Congrats! Player " + " ".join([str(w + 1) for w in winner]) + " won!")
            break
    except ValueError:
        print(str(position) + " position is already taken!")

print("Thanks for playing.")
