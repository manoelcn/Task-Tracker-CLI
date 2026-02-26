from storage import load_tasks, save_tasks
from datetime import datetime


def add_task(description):
    tasks = load_tasks()
    if tasks:
        task_id = max(task['id'] for task in tasks) + 1
    else:
        task_id = 1
    now = datetime.now().isoformat()
    task = {
        'id': task_id,
        'description': description,
        'status': 'in-progress',
        'createdAt': now,
        'updatedAt': now
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {task_id})')