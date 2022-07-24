# import all the required module
import random
import matplotlib.pyplot as plt

# main function , takes 2 argumnets itr= number of iterations to be performed , num_doors= number of doors
def game_simulation(itr , num_doors=3):
    win = 0
    count = 0
    while count < itr:
        prize_door = random.randint(0,num_doors-1)
        player_choice = random.randint(0,num_doors-1)
        # if prize door equal player choice then after switching player will lose and when player choice is not equal to prize containing door then on switching the will win
        if prize_door == player_choice:
            pass
        else:
            win = win + 1
        count = count + 1
    return win/itr

results = []
num_door = []

# loop to get the probability of winning on different numbers of doors
for num_doors in range(3,100):
    results.append(game_simulation(100000,num_doors))
    num_door.append(num_doors)

# plot the results
plt.figure(figsize=(30,15))
plt.plot(num_door , results)
plt.show()