task_discription = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match time_bound:
    case "yes":
        if task_priority.lower() == "high":
            print(f"Reminder: '{task_discription}' is a {task_priority} priority task that requires immediate attention today!")
        elif task_priority.lower() == "medium":
            print(f"Reminder: '{task_discription}' is a {task_priority} priority task that requires your attention before the deadline!")
        elif task_priority.lower() == "low":
            print(f"Reminder: '{task_discription}' is a {task_priority} priority task that requires your attention before the deadline!")

    case "no":
        if task_priority.lower() == "high":
            print(f"Note: '{task_discription}' is a {task_priority} priority task. Consider completing it when you have free time.")
        elif task_priority.lower() == "medium":
            print(f"Note: '{task_discription}' is a {task_priority} priority task. Consider completing it when you have free time.")
        elif task_priority.lower() == "low":
            print(f"Note: '{task_discription}' is a {task_priority} priority task. Consider completing it when you have free time.")
