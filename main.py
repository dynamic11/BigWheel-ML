from random import randint
import numpy as np
import random
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
# for _ in range(20):
#     bets= [1, 5, 20]
#     amounts = [5, 5, 1]
#     print(game.take_turn(bets, amounts))

alpha = 0.1
gamma = 0.6
epsilon = 0.1


q_table = np.ones([100, 6])

for i in range(1, 10000000):
    balance = 20
    state = game.reset()

    epochs, penalties, reward, = 0, 0, 0
    done = False

    turn=0

    while not done:
        oldbalance = state

        if random.uniform(0, 1) < epsilon or turn == 0:
            action = randint(0, 5)
        else:
            action = np.argmax(q_table[state])

        print ("action: " + str(action))
        turn = turn+1

        # if action is not cash out (0)
        if action != 0:
            # bet a dollar on number
            balance = game.take_turn([action], [1])
            print ("balance: " + str(balance))

        if action != 0 and (balance-oldbalance) < 0:
            reward = -0.5
        elif action == 0 and (balance-oldbalance) < 0:
            reward = -0.75
        elif balance <= 0:
            reward = -1
        elif action != 0 and (balance-oldbalance) >= 0:
            reward = 0.5
        elif action == 0 and (balance-oldbalance) > 30:
            reward = 1

        if action == 0:
            done=True#cash out

        new_state = balance

        old_q_value = q_table[state, action-1];
        next_q_max = np.max(q_table[new_state])

        new_value = (1 - alpha) * old_q_value + alpha * (reward + gamma * next_q_max)
        q_table[state, action] = new_value

        state = new_state
        epochs += 1


    print("+++++++++++++++++++++++")
    print ("epochs: "+str(epochs))
    print("+++++++++++++++++++++++")


print("Training finished.\n")