import json

file_path = "my_cars.json"


def load():
    try:
        with open(file_path, "r") as f:
            my_cars = json.load(f)
            print("loading cars...")
            return my_cars
    except:
        print("No file found")
        my_destinations = []
        return my_cars


def save(my_cars):
    with open(file_path, "w") as f:  # f=open()
        json.dump(my_cars, f)

    print("saving...")
