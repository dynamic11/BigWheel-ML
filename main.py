from random import randint

from snakeGame import SnakeGame
from wheelGame import WheelGame

# game = SnakeGame(gui=False)
# game.start()
# for _ in range(20):
#     game.step(randint(0, 3))
#     game.generate_observations
#     print(game.score)

game = WheelGame()
print(game.start());
print(game.take_turn(5));
for _ in range(20):
    print(game.take_turn(5));