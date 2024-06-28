from json import load
from cars_package.actions import add_car, cars_list, delete_car, search_cars
from storage.save_load import save, load
import json

file_path = "my_cars.json"


# my_cars = [
#     {"car_problems": ["engine", "breaks"], "total_cost": 3000},
#     {"car_problems": ["engine", "5000 km treatment"], "total_cost": 2500},
# ]


def menu():
    my_cars = load()
    while True:
        print("WELCOME TO RAN'S GARAGE!")
        print("1- List of cars")
        print("2- Add a car")
        print("3- Delete a car")
        print("4- Search a car")
        print("5- Exit")
        selection = int(input("enter your action: "))
        if selection == 1:
            cars_list(my_cars)
        elif selection == 2:
            add_car(my_cars)
        elif selection == 3:
            delete_car(my_cars)
        elif selection == 4:
            search_cars(my_cars)
        elif selection == 5:
            save()
            print("Exit..")
            break
