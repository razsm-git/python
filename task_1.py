from time import sleep


class TrafficLight:
    __color = "red"

    def running(self):
        second_color = 'yellow'
        third_color = 'green'
        while True:
            r = TrafficLight.__color
            print(r)
            sleep(7)
            print(second_color)
            sleep(2)
            print(third_color)
            sleep(10)
            print(second_color)
            sleep(2)


a = TrafficLight()
a.running()
