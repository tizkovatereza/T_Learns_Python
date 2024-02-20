# T_Learns_Python/Gym_Exercise_Tracker.py

# Dictionary to store gym exercises and their weights
gym_exercises = {
"Low row": "20 kg",
"Lat machine convergent": "30 kg",
"Rear delt fly": "4 kg each side",
"Overhead triceps extensions": "10 kg",
"Lat pulldown": "35 kg",
"Inclined chest press": "10 kg",
"squat": "50 kg",
"hip thrust": "100 kg",
"master gluteus": "40 kg",
"abductor": "60 kg",
"adductor": "65 kg",
"torsion": "35 kg",
"deltoid press": "10 kg"
    
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

# Allow the user to update the weight of any exercise
while True:
    exercise = input("Enter the name of the exercise to update, 'add' to add a new exercise, or 'quit' to exit: ")
    if exercise.lower() == 'quit':
        break
    elif exercise.lower() == 'add':
        new_exercise = input("Enter the name of the new exercise: ")
        new_weight = input("Enter the weight for the new exercise: ")
        add_exercise(new_exercise, new_weight)
    else:
        new_weight = input("Enter the new weight for the exercise: ")
        update_exercise(exercise, new_weight)
    display_exercises()
