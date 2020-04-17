from random import randint

from snakeGame import SnakeGame

game = SnakeGame(gui=False)
game.start()
for _ in range(20):
    game.step(randint(0, 3))
    game.generate_observations
    print(game.score)