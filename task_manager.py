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


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks found.')
        return
    for task in tasks:
        print(f'{task['id']} - {task['description']} - {task['status']}\nCreated: {task['createdAt']}\nUpdated: {task['updatedAt']}')


def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None
