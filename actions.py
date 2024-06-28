
def cars_list(my_cars):
    for index, car in enumerate(my_cars):
        car["car_number"] = index + 1
        print(
            f"Car's number is: {car['car_number']}, car's problems are: {car['car_problems']}, total cost is: ${car['total_cost']}"
        )

def add_car(my_cars):
    problem_costs = {
        "engine": 2000,
        "breaks": 1000,
        "5000 km treatment": 500,
        "10,000 km treatment": 1000,
        "filters + Oil": 250,
        "gear": 1000
    }
    car_problems = []
    total_cost = 0
    while True: 
        problem = input("please enter your car problem (Engine/Breaks/5000 km treatment/10,000 km treatment/ Filters + Oil/ Gear) ").lower()
        if problem not in problem_costs:
            print("Invalid problem entered. Please choose from the given list.")
            continue
        if problem in car_problems:
            print("Problem already entered. Please choose a different problem.")
            continue

        car_problems.append(problem)
        total_cost += problem_costs[problem]

        user_contiue = input("Do you have another problem? (yes/no): ").lower()
        if user_contiue.lower() != "yes":
            break

    new_car = {"car_problems":car_problems, "total_cost": total_cost}
    print(f"your cars problems are: {car_problems}")
    print(f"Your total repair cost will be: ${total_cost}")
    user_approval = input("Do you approve the total cost? (yes/no): ").lower()
    if user_approval == "yes":
        my_cars.append(new_car)
        print("Car has been added successfully.")
    else:
        print("Car was not added.")


def delete_car(my_cars):
    cars_list(my_cars)
    car_num_selection = int(input("Which car number do you want to delete?: "))
    for car in my_cars:
        if car_num_selection == car["car_number"]:
            my_cars.remove(car)

def search_cars(my_cars):
    cars_list(my_cars)
    while True:
        user_search_text = input("Please enter your car's number or problems(type 'exit' to quit): ")
        if user_search_text.lower() == "exit":
            break

        for car in my_cars:
            if (any(user_search_text in problem.lower() for problem in car["car_problems"]) or 
                user_search_text == str(car["car_number"])):
                print("Cars search list:")
                print(f"The car number is: {car["car_number"]} and the problems are: {car["car_problems"]}")
        
