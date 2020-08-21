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
        game_runner.take_turn(position)
        winner = game_runner.get_winner()
        print("Board state")
        print(game_runner.game.draw())
        if winner is not None or game_runner.game_over():
            print("Game Over!")
            if winner:
                print("Congrats! Player " + str(winner) + " won!")
            break
    except ValueError:
        print(str(position) + " position is already taken or invalid!")

print("Thanks for playing.")
