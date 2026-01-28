How to start the connection:
1. start the connection in your terminal with -- fastapi dev main.py
2. copy the domain with /docs to access your task list

Task List Functions:
1. get("/tasks"): press try out to open up a list that includes all your tasks (one sample task always exist by default with the task id 1)
   Note: you can also end your domain with /tasks to view a list that includes all your tasks
2. post("/tasks/addTasks/"): press try out to open up a window that can be used to add tasks
   if you want to add a new task you will have to use the following structure: {"task_id": X, "task_name": "X", "task_description": "X"}
   once you filled out all the placeholders (X) you can execute it and your new task should be added
3. put("/tasks/update/{task_id}"): press try out to open up a window that can be used to change the contents of tasks
   if you want to change the contents of your list you will have to use the following structure: {"task_id": changed number, "task_name": "change", "task_description": "change"}
   once you filled out all the placeholders (change) you can execute it and your task should be updated
4. delete("/tasks/delete/{task_id}"): press try out to open up a textbox that can be used to delete tasks
   if you want to delete a task add the associated task id and execute to delete
