from EventManager import EventManager
from Task import Task
class TaskManager:
    def __init__(self,tasks=None,total=0,finished=0,remaining=0,failed=0,eventmanagernew=None):
        if tasks is None:
            self.tasks = []
        else:
            self.tasks = tasks

        if eventmanagernew is None:
            self.eventmanager = EventManager()
        else:
            self.eventmanager = eventmanagernew

        self.total = total
        self.finished = finished
        self.remaining = remaining
        self.failed = failed

    def addTaskonStart(self, taskname, taskdescription, duedate, completion_state):
        newtask = Task(taskname, taskdescription, duedate, completion_state)
        self.tasks.append(newtask)


    def addTask(self, taskname, taskdescription, duedate):
        newtask = Task(taskname, taskdescription, duedate)
        self.tasks.append(newtask)
        self.total += 1
        self.remaining += 1
        self.eventmanager.emit("task_added",newtask)

    def removeTask(self, taskname):
        for task in self.tasks:
            if task.name == taskname:
                if task.complete:
                    self.finished -= 1
                else:
                    self.failed += 1
                    self.remaining -= 1
                self.eventmanager.emit("task_removed", task)
                self.tasks.remove(task)
                break


    def listTasks(self):
        for x in range(0,len(self.tasks)):
            print(f"{x+1})Name: {self.tasks[x].name}\n  Description: {self.tasks[x].description}\n  Due By: {self.tasks[x].duedate}\n  Completed: {self.tasks[x].complete}")

    def completeTask(self, taskname):
        for task in self.tasks:
            if task.name == taskname:
                if not task.complete:
                    self.finished += 1
                    self.remaining -= 1
                    task.complete = True
                    self.eventmanager.emit("task_completed",task)
                break

    def printstats(self):
        print(f" Total Tasks: {self.total} \n Finished:{self.finished} \n Remaining:{self.remaining} \n Failed: {self.failed}")

    def to_dict(self):
        listdic={}
        for task in self.tasks:
            listdic[task.name]=task.to_dict()
        return {"total": self.total, "finished": self.finished, "remaining": self.remaining, "failed": self.failed, "tasks": listdic}
