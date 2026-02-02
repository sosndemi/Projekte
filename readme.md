How to start the connection:

1. start the connection in your terminal with -- uvicorn app:app --reload
2. copy the domain with /docs to access your task list

Task List Functions:
1. get("/tasks"): press try out to open up the task list that includes all your tasks (empty if you did not add a task) Note: you can also end your domain with /tasks to view a list that includes all your tasks
2. post("/tasks/addTasks/"): press try out to open up a window that can be used to add tasks if you want to add a new task you will have to use the following structure: {"task_name": "X", "task_description": "X"} once you filled out all the placeholders (X) you can execute it and your new task should be added. The first talk you add has the task_id of 1, every new task has the id of +1.
3. put("/tasks/update/{task_id}"): press try out to open up a window that can be used to change the contents of tasks if you want to change the contents of your list you will have to add the associated task id and use the following structure: {"task_name": "change", "task_description": "change"} once you filled out all the placeholders (change) you can execute it and your task should be updated.
4. delete("/tasks/delete/{task_id}"): press try out to delete tasks. If you want to delete a task add the associated task id and execute to delete.

Dockerfile:
build the image: docker build -t tasksqlalchemy .
run the container: docker run -d -p 8000:80 --name task-container tasksqlalchemy
use http://localhost:8000/docs to access the api
