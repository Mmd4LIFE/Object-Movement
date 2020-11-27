""" Created by Mmd4LIFE at Nov 25/2020
"""
from numpy import (
    random as np_random
    )
from typing import List
import matplotlib.pyplot as plt
from time import sleep

from numpy.core.fromnumeric import size

class Main():
    def __init__(self):
        super(Main, self).__init__()
        self.random_movement: List = list()
        self.measure_of_horizontal_movement: float = 0.5
        self.measure_of_vertical_movement: float = 0.7
        

    @property
    def object_moving(self):
        """ This function determined next step of movement
            by using random of numpy
            :params:
            :return: next movement of object
        """
        binomial_random = np_random.binomial(1, 0.5, 2)

        if binomial_random[0] == 0:
            self.random_movement.append((binomial_random[0]-1)*self.measure_of_horizontal_movement)
        else:
            self.random_movement.append((binomial_random[0])*self.measure_of_horizontal_movement)
        
        if binomial_random[1] == 0:
            self.random_movement.append((binomial_random[1]-1)*self.measure_of_vertical_movement)
        else:
            self.random_movement.append((binomial_random[1])*self.measure_of_vertical_movement)
        return self.random_movement
        
    def next_destination(self):
        """ This function returned all steps of movement
            by using object_moving function
            :params:
            :return: all steps of movement
        """
        before_location: List = [0, 0]
        self.all_steps = [before_location]
        step = 0
        count_of_steps = 1000
        while step < count_of_steps-1:
            self.new_location: List = list()
            for item in range(2):
                result = round(before_location[item] + Main().object_moving[item], 1)
                self.new_location.append(result)
            
            # This condition guarantees that results not be repetitious
            if self.all_steps.count(self.new_location) == 0:
                self.all_steps.append(self.new_location)
                print(str(len(self.all_steps)), " -> ", self.new_location)
                sleep(0.1)
                before_location = self.new_location
                step += 1
            
                if (self.condition_of_break):
                    self.limiting_points
                    break

    @property
    def condition_of_break(self):
        return(
            self.all_steps.count([
                round(self.new_location[0] + self.measure_of_horizontal_movement, 1),
                round(self.new_location[1] + self.measure_of_vertical_movement, 1)]) == 1
            and 
            self.all_steps.count([
                round(self.new_location[0] + self.measure_of_horizontal_movement, 1),
                round(self.new_location[1] - self.measure_of_vertical_movement, 1)]) == 1
            and 
            self.all_steps.count([
                round(self.new_location[0] - self.measure_of_horizontal_movement, 1), 
                round(self.new_location[1] + self.measure_of_vertical_movement, 1)]) == 1
            and 
            self.all_steps.count([
                round(self.new_location[0] - self.measure_of_horizontal_movement, 1), 
                round(self.new_location[1] - self.measure_of_vertical_movement, 1)]) == 1
        )

    @property
    def limiting_points(self):
        return(
            plt.scatter(
                round(self.new_location[0] + self.measure_of_horizontal_movement, 1), 
                round(self.new_location[1] + self.measure_of_vertical_movement, 1), 
                color="red")
            and 
            plt.scatter(
                round(self.new_location[0] + self.measure_of_horizontal_movement, 1), 
                round(self.new_location[1] - self.measure_of_vertical_movement, 1), 
                color="red")
            and
            plt.scatter(
                round(self.new_location[0] - self.measure_of_horizontal_movement, 1), 
                round(self.new_location[1] + self.measure_of_vertical_movement, 1), 
                color="red")
            and
            plt.scatter(
                round(self.new_location[0] - self.measure_of_horizontal_movement, 1), 
                round(self.new_location[1] - self.measure_of_vertical_movement, 1), 
                color="red")
        )


    def show_figure(self):
        self.next_destination()
        x_array: List = []
        y_array: List = []
        for coordinates in self.all_steps:
            x_array.append(coordinates[0])
            y_array.append(coordinates[1])
        plt.plot(x_array, y_array)
        plt.axis([min(x_array)-1, max(x_array)+1, min(y_array)-1, max(y_array)+1])
        plt.grid(True, axis='x')
        plt.grid(True, axis='y')
        plt.scatter(self.all_steps[0][0], self.all_steps[0][1], color="black")
        #for item in range (len(all_steps)):
        #    plt.plot([0, all_steps[item][0]], [all_steps[item][1], all_steps[item][1]], linestyle="--", color="black")
        #    plt.plot([all_steps[item][0], all_steps[item][0]], [0, all_steps[item][1]], linestyle="--", color="black")
        plt.show()
        

if __name__ == "__main__":
    Main().show_figure()

