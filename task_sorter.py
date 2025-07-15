import pandas as pd

categories = {
    "Work": ["email", "meeting", "call", "project", "manager", "hr", "proposal", "resume", "zoom", "sprint", "invoice", "config"],
    "Study": ["read", "study", "exam", "course", "assignment", "lecture", "chapter", "dsp", "cn", "notes", "manual"],
    "Personal": ["buy", "clean", "cook", "family", "health", "birthday", "trip", "bill", "fruits", "milk", "grocery", "laundry", "yoga"],
    "Misc": []
}

sorted_tasks = {category: [] for category in categories}

try:
    df = pd.read_excel("tasks.xlsx", header=None)
except FileNotFoundError:
    print("Error: 'tasks.xlsx' not found in the current directory.")
    exit()


for task in df[0].dropna():
    task = str(task).strip()
    found = False
    for category, keywords in categories.items():
        if any(keyword in task.lower() for keyword in keywords):
            sorted_tasks[category].append(task)
            found = True
            break
    if not found:
        sorted_tasks["Misc"].append(task)


print("\nSorted Tasks:")
for category, tasks in sorted_tasks.items():
    if tasks:
        print(f"\n{category}:")
        for t in tasks:
            print(f" - {t}")
