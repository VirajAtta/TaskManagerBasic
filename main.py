#Importing All Other Modules
from TaskManager import TaskManager
from EventManager import EventManager
import json
from pathlib import Path
#Creating and Reading Path of TM or Creating new TM
TMpath=Path("TMstoragefile.json")
try:
    data_json = json.loads(TMpath.read_text())
    TM = TaskManager(total=data_json["total"],finished=data_json["finished"],remaining=data_json["remaining"],failed=data_json["failed"])
    for task in data_json["tasks"].values():
        TM.addTaskonStart(task["name"], task["description"], task["duedate"],task["complete"])
except FileNotFoundError:
    TM = TaskManager()
#Testing the on and emit




def make_logger(prefix):

    def printlog(task):
        print(f"{prefix} {task.name}")
    return printlog

task_added_logger = make_logger("Task added:")
task_completed_logger = make_logger("Task completed:")
task_removed_logger = make_logger("Task removed:")

TM.eventmanager.on("task_added", task_added_logger)
TM.eventmanager.on("task_completed", task_completed_logger)
TM.eventmanager.on("task_removed", task_removed_logger)

def make_history_tracker(limit):
    history = []

    def track(event=None):

        if event is not None:
            history.append(event)

            if len(history) > limit:
                history.pop(0)

        return history

    return track

history_tracker = make_history_tracker(5)






def make_history_handler(action):

    def handler(task):
        history_tracker(f"{action}: {task.name}")


    return handler

added_history = make_history_handler("Task added")
completed_history = make_history_handler("Task completed")
removed_history = make_history_handler("Task removed")

TM.eventmanager.on("task_added", added_history)
TM.eventmanager.on("task_completed", completed_history)
TM.eventmanager.on("task_removed", removed_history)



#Main Loop
while True:
    prompt= input("What would you like to do?")
    if prompt == "exit" or prompt == "quit" or prompt == "q":
        TMdict=TM.to_dict()
        json_string = json.dumps(TMdict, indent=4)
        TMpath.write_text(json_string)
        break
    elif prompt == "add" or prompt == "a":
        TM.addTask(input("What is the name of the task?"),input("What is the description?"),input("What is the due date?"))
    elif prompt == "remove" or prompt == 'r':
        TM.removeTask(input("Which task would you like to remove?"))
    elif prompt == "list" or prompt == "l":
        TM.listTasks()
    elif prompt == "stats" or prompt == "s":
        TM.printstats()
    elif prompt == "complete" or prompt == "c":
        TM.completeTask(input("Which task would you like to mark complete?"))
    elif prompt == "history" or prompt == "h":
        for event in history_tracker():
            print(event)