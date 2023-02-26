"""Task bout trafficlight"""
from time import sleep


class TrafficLight:
    __colour = ['red', 'yellow', 'green']

    @staticmethod
    def running():
        i = 0
        while i < 3:
            print(f' Please wait... \n'
                  f'{TrafficLight.__colour[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


# Checking if everything runs
exam = TrafficLight()
exam.running()
