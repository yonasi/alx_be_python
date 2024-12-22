task_discription = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
         if time_bound == "yes":
            print(f"Reminder: '{task_discription}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task_discription}' is a {priority} priority task. Consider completing it when you have free time.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task_discription}' is a {priority} priority task that requires your attention before the deadline!")
        elif time_bound == "no":
            print(f"Note: '{task_discription}' is a {priority} priority task. Consider completing it when you have free time.")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task_discription}' is a {task_priority} priority task. Consider completing it before the deadline!")
        elif time_bound == "no":
            print(f"Note: '{task_discription}' is a {task_priority} priority task. Consider completing it when you have free time.")
