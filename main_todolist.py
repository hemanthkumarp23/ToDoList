from module_todolist import TodoList

myList = TodoList("Hemanth")

while(True):

	y = eval(input("Choose the option below: \n 1. Add task to the list \n 2. To see current TO_Do list and DONE list \n 3. Mark the task as done \n"))

	if y == 1:
		for i in range(1, 6):
			addtask = input("Enter the task to add: ")
			lower_addtask = addtask.lower()
			myList.add_task(lower_addtask)

	elif y == 2:
		myList.see_list()

	elif y == 3:
		myList.see_list()
		donetask = input("Enter the task you have completed: ")
		myList.mark_done(donetask.lower())

	else:
		break
