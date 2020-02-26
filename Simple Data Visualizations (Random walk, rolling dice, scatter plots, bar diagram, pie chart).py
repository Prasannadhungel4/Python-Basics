# Simple Data Visualixation and Plots

import matplotlib.pyplot as plt
from random import choice

# Plotting bar graph and scatter plots and saving it as an image

input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_value, squares, linewidth = 5)
plt.title("square numbers", fontsize = 25)
plt.xlabel("value", fontsize = 18)
plt.ylabel("square of value", fontsize = 18)
plt.tick_params(axis="both", labelsize = 14)
plt.show()

input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.scatter(input_value, squares, s=20)
plt.show()


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values,  c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=100)
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()

# Random Walk

class Randomwalk():
    def __init__(self, num_points = 5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    
    def walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([1,2,3,4,5])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([1,2,3,4,5])
            y_step = y_direction *y_distance

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


rw = Randomwalk()
rw.walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.savefig('ppp.png', bbox_inches='tight')
plt.show()


# rolling dice
from random import randint
import pygal

class die():
    def __init__(self, sides =6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

dice = die()
results = []
for roll_no in range(1000):
    result = dice.roll()
    results.append(result)

frequencies = []
for value in range(1, dice.sides+1):
 frequency = results.count(value)
 frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()
hist.x_labels = ['1','2','3','4','5','6']
hist.add("D6" , frequencies)
hist.render_to_file("die.svg") 