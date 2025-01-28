import random


sbreak_tasks = ["cleaning the kitchen", "cleaning the livingroom", "doing laundry", "taking out the trash", "fetching a drink", ""]

lbreak_tasks = [""]

def short_break_tasks():
    if sbreak_tasks:
        task = random.choice(sbreak_tasks)
        sbreak_tasks.remove(task)
        return task
    else:
        return "no more tasks available"
    

def long_break_tasks():
    if lbreak_tasks:
        task = random.choice(lbreak_tasks)
        lbreak_tasks.remove(task)
        return task
    else:
        return "no more tasks available"
    

