import random

# Memory
tasks = []

boosts = [
    "Small steps still move you forward!",
    "Helping one person today makes the world better.",
    "Done is better than perfect.",
    "You've got this!",
    "Kindness is worth doing every day."
]


# Functions
def is_duplicate(title):
    for task in tasks:
        if task["title"].lower() == title.lower():
            return True
    return False


def get_icon(priority):
    if priority == "high":
        return "🔴"
    elif priority == "medium":
        return "🟡"
    else:
        return "🟢"


def show_tasks():
    if len(tasks) == 0:
        print("\nNothing here yet. Add your first task!")
        return

    done_count = 0
    print("\n--- YOUR TASKS ---")

    for i, task in enumerate(tasks):
        status = "✔️" if task["done"] else "⬜"

        if task["done"]:
            done_count += 1

        print(
            f"{i + 1}. {status} {get_icon(task['priority'])} "
            f"{task['title']} (for: {task['for']})"
        )

    print(f"Progress: {done_count} of {len(tasks)} done")


def get_index():
    try:
        number = int(input("Enter task number: "))
        index = number - 1

        if 0 <= index < len(tasks):
            return index

        print("Invalid task number!")
        return -1

    except ValueError:
        print("Please enter a valid number!")
        return -1


# Main program
print("🌱 KIND TO-DO")
print("Plan your day, and help someone else too.")

while True:
    print("\n--- MENU ---")
    print("1. Give me a boost")
    print("2. Add a task")
    print("3. Show tasks")
    print("4. Mark task as done")
    print("5. Delete a task")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        print("\n✨", random.choice(boosts))

    elif choice == "2":
        title = input("Task title: ").strip()

        if title == "":
            print("Please type a task title first.")
            continue

        if is_duplicate(title):
            print("This task is already in your list!")
            continue

        helping = input(
            "Who is this for? (Press Enter for yourself): "
        ).strip()

        if helping == "":
            helping = "Me"

        priority = input(
            "Priority (high/medium/low): "
        ).strip().lower()

        if priority not in ["high", "medium"]:
            priority = "low"

        tasks.append({
            "title": title,
            "for": helping,
            "priority": priority,
            "done": False
        })

        print("✅ Task added!")

    elif choice == "3":
        show_tasks()

    elif choice == "4":
        show_tasks()

        if len(tasks) > 0:
            index = get_index()

            if index != -1:
                tasks[index]["done"] = True
                print("🎉 Great job! Task completed.")

    elif choice == "5":
        show_tasks()

        if len(tasks) > 0:
            index = get_index()

            if index != -1:
                deleted_task = tasks.pop(index)
                print("🗑️ Deleted:", deleted_task["title"])

    elif choice == "6":
        print("Goodbye! Keep spreading kindness. 🌱")
        break

    else:
        print("Invalid option. Please choose 1 to 6.")
