# T_Learns_Python/Gym_Exercise_Tracker.py

# Dictionary to store gym exercises and their weights
gym_exercises = {
    "Low row": "20 kg",
    "Lat machine convergent": "30 kg",
    "Rear delt fly": "5 kg each side",
    "Overhead triceps extensions": "10 kg",
    "Lat pulldown": "35 kg",
    "Inclined chest press": "10 kg",
}

def display_exercises():
    """Prints the current list of exercises and their weights."""
    for exercise, weight in gym_exercises.items():
        print(f"{exercise}: {weight}")

def update_exercise(exercise, new_weight):
    """Updates the weight of an exercise."""
    gym_exercises[exercise] = new_weight

def add_exercise(exercise, weight):
    """Adds a new exercise and its weight."""
    gym_exercises[exercise] = weight

# Display the current list of exercises and their weights
display_exercises()

# Allow the user to update the weight of any exercise or add a new one
while True:
sweep/add-new-exercise-option
    exercise = input("Enter the name of the exercise to update or add (or 'quit' to exit): ")
    if exercise.lower() == 'quit':
        break
    new_weight = input("Enter the new weight for the exercise: ")
    if exercise not in gym_exercises:
        print(f"Adding new exercise {exercise} with weight {new_weight}")
    else:
        print(f"Updating exercise {exercise} to new weight {new_weight}")

        main

