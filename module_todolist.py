class TodoList(object):

    def __init__(self, name):
        self.new = []
        self.done = []
        self.name = name

    def add_task(self, new_task):
        self.new.append(new_task)

    def see_list(self):
        print("The TO_DO list is {}".format(self.new))
        print("The DONE list is {}".format(self.done))

    def mark_done(self, task_index):
        self.new.remove(task_index)
        self.done.append(task_index)
