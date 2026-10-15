# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:29:51 2026

@author: AA
"""

from task import Task

tasks = {}

# --------------------------------------------------------


def create_task(task):
    '''
    یک تسک جدید ایجاد می‌کند و در دیکشنری tasks ذخیره می‌کند.
    شناسه تکراری و اولویت یا وضعیت نامعتبر را بررسی می‌کند.
    '''
    if task.id not in tasks:
        if task.priority in ["LOW", "MEDIUM", "HIGH"]:
            if task.status in ["OPEN", "IN_PROGRESS", "DONE"]:
                tasks[task.id] = task
                print("Task created successfully.")
            else:
                print("Invalid status.")
        else:
            print("Invalid priority.")
    else:
        print("Task ID already exists.")


# --------------------------------------------------------


def read_task(task_id):
    '''
    یک تسک را با استفاده از شناسه آن پیدا می‌کند.
    اگر تسک پیدا نشود، پیام خطا و فهرست تسک‌ها را نمایش می‌دهد.
    '''
    if task_id in tasks:
        return tasks[task_id]

    print("Task not found! Here is the list of all tasks:")

    for task in tasks.values():
        print(task)

    return None


# --------------------------------------------------------

def show_all_tasks():
    '''
    تمام تسک‌ها را نمایش می‌دهد.
    '''
    for task in tasks.values():
        print(task)


# --------------------------------------------------------


def update_task(task_id, title=None, assignee=None,
                priority=None, status=None):
    '''
    اطلاعات یک تسک موجود را تغییر می‌دهد.
    قبل از اعمال تغییرات، اولویت و وضعیت جدید را بررسی می‌کند.
    '''
    if task_id not in tasks:
        print("Task not found!")
        return

    task = tasks[task_id]

    if priority is not None:
        if priority not in ["LOW", "MEDIUM", "HIGH"]:
            print("Invalid priority!")
            return

    if status is not None:
        if status not in ["OPEN", "IN_PROGRESS", "DONE"]:
            print("Invalid status!")
            return

        if task.status == "OPEN" and status == "IN_PROGRESS":
            pass
        elif task.status == "IN_PROGRESS" and status == "DONE":
            pass
        elif task.status == status:
            pass
        else:
            print("Invalid status transition!")
            return

    if title is not None:
        task.title = title

    if assignee is not None:
        task.assignee = assignee

    if priority is not None:
        task.priority = priority

    if status is not None:
        task.status = status

    print("Task updated successfully.")


# --------------------------------------------------------


def delete_task(task_id):
    '''
    یک تسک را با استفاده از شناسه آن حذف می‌کند.
    برای حذف تسک‌های در حال انجام یا تکمیل‌شده، تأیید می‌گیرد.
    '''
    try:
        if task_id not in tasks:
            raise ValueError("Task not found!")
    except ValueError as e:
        print(e)
        return

    task = tasks[task_id]

    if task.status == "IN_PROGRESS" or task.status == "DONE":
        confirm = input(
            "Are you sure you want to delete this task? (yes/no): "
        )

        if confirm.lower() == "yes":
            del tasks[task_id]
            print("Task deleted successfully.")
        else:
            print("Task deletion cancelled.")
    else:
        del tasks[task_id]
        print("Task deleted successfully.")


# --------------------------------------------------------


def search_tasks(assignee=None, priority=None, status=None):
    '''
    تسک‌ها را بر اساس مسئول، اولویت یا وضعیت جست‌وجو می‌کند.
    اگر چند معیار مشخص شوند، همه آن‌ها باید برقرار باشند.
    '''
    for task in tasks.values():
        if (assignee is None or task.assignee == assignee) and \
           (priority is None or task.priority == priority) and \
           (status is None or task.status == status):
            print(task)


# --------------------------------------------------------


def generate_report():
    '''
    تعداد کل تسک‌ها، تسک‌های تکمیل‌شده و تسک‌های باز را محاسبه می‌کند.
    '''
    total = len(tasks)
    completed = 0
    open_tasks = 0

    for task in tasks.values():
        if task.status == "DONE":
            completed += 1
        elif task.status == "OPEN":
            open_tasks += 1

    print("Total tasks:", total)
    print("Completed tasks:", completed)
    print("Open tasks:", open_tasks)


# --------------------------------------------------------


def assignee_report():
    '''
    تعداد تسک‌های هر مسئول و مسئول دارای بیشترین تسک باز را مشخص می‌کند.
    '''
    assignee_counts = {}
    open_counts = {}

    for task in tasks.values():
        if task.assignee not in assignee_counts:
            assignee_counts[task.assignee] = 0
            open_counts[task.assignee] = 0

        assignee_counts[task.assignee] += 1

        if task.status == "OPEN":
            open_counts[task.assignee] += 1

    print("Tasks per assignee:")

    for assignee in assignee_counts:
        print(assignee, ":", assignee_counts[assignee])

    max_open = 0
    best_assignee = None

    for assignee in open_counts:
        if open_counts[assignee] > max_open:
            max_open = open_counts[assignee]
            best_assignee = assignee

    if best_assignee is not None:
        print("Most open tasks:", best_assignee)
        print("Number of open tasks:", max_open)
    else:
        print("No open tasks.")


# --------------------------------------------------------
# ساخت تسک‌های اولیه

task1 = Task(101, "Fix login bug", "Ali", "HIGH", "OPEN")
task2 = Task(102, "Update API", "Sara", "MEDIUM", "IN_PROGRESS")
task3 = Task(103, "Write tests", "Ali", "LOW", "DONE")


# اضافه کردن تسک‌ها
create_task(task1)
create_task(task2)
create_task(task3)


# --------------------------------------------------------
# نمایش یک تسک

print("\n--- Read Task ---")
task = read_task(102)

if task is not None:
    print(task)

# --------------------------------------------------------
# تست شناسه نامعتبر

print("\n--- Test Invalid ID ---")
read_task(999)

# --------------------------------------------------------
# نمایش همه تسک‌ها

print("\n--- All Tasks ---")
show_all_tasks()

# --------------------------------------------------------
# ویرایش تسک

print("\n--- Update Task ---")
update_task(101, title="Fix database bug")

# تست اولویت نامعتبر
update_task(101, title="New title", priority="URGENT")

# تست تغییر وضعیت غیرمجاز
update_task(101, status="DONE")

# نمایش اطلاعات تسک پس از تست‌ها
task = read_task(101)

if task is not None:
    print(task)

update_task(999, title="Test")
# --------------------------------------------------------
# حذف تسک

print("\n--- Delete Task ---")
delete_task(999)
delete_task(103)

# --------------------------------------------------------
# جست‌وجو

print("\n--- Search by Assignee ---")
search_tasks(assignee="Ali")

print("\n--- Search by Priority ---")
search_tasks(priority="HIGH")

print("\n--- Search by Status ---")
search_tasks(status="DONE")

print("\n--- Search by Assignee and Priority ---")
search_tasks(assignee="Ali", priority="HIGH")


# --------------------------------------------------------
# گزارش‌گیری

print("\n--- Task Report ---")
generate_report()

print("\n--- Assignee Report ---")
assignee_report()