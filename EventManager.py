class EventManager:
    def __init__(self):
        self.events = {
            "task_added": [],
            "task_completed": [],
            "task_removed": []
        }

    def on(self, event_name, function):
        self.events[event_name].append(function)

    def emit(self, event_name, *tasks):
        for task in tasks:
            for event in self.events[event_name]:
                event(task)







