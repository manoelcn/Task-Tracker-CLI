from datetime import datetime

from storage import load_tasks, save_tasks


def add_task(description):
    if not description.strip():
        print('Description cannot be empty.')
        return
    tasks = load_tasks()
    task_id = max((task['id'] for task in tasks), default=0) + 1
    now = datetime.now().isoformat()
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now,
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
        print(
            f'{task["id"]} - {task["description"]} - {task["status"]}\nCreated: {task["createdAt"]}\nUpdated: {task["updatedAt"]}'
        )


def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None


def task_mark_status(task_id, status):
    allowed_status = {'todo', 'in-progress', 'done'}
    if status not in allowed_status:
        print('Invalid status.')
        return
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)
    if not task:
        print('Task not found.')
        return
    now = datetime.now().isoformat()
    task['status'] = status
    task['updatedAt'] = now
    save_tasks(tasks)


def task_update(task_id, description):
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)
    if not task:
        print('Task not found.')
        return
    now = datetime.now().isoformat()
    task['description'] = description
    task['updatedAt'] = now
    save_tasks(tasks)


def task_delete(task_id):
    tasks = load_tasks()
    task = find_task_by_id(tasks, task_id)
    if not task:
        print('Task not found.')
        return
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
