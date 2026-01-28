from fastapi import FastAPI


app = FastAPI()
all_tasks = [{"task_id": 1, "task_name": "Sample Task", "task_description": "This is a sample task description."}]
         

@app.get("/tasks")
def getalltasks():
        return all_tasks


@app.post("/tasks/addTasks/")
def addtasks(task:dict):
    new_task_id = max(task["task_id"] for task in all_tasks) + 1
    new_task = {
         "task_id": new_task_id,
         "task_name": task["task_name"],
         "task_description": task["task_description"]
        }
    all_tasks.append(new_task)
    return new_task

@app.put("/tasks/update/{task_id}")
def updatetask(task_id:int, updated_task:dict):
    for task in all_tasks:
        if task["task_id"] == task_id:
            task["task_name"] = updated_task["task_name"]
            task["task_description"] = updated_task["task_description"]
            return task
        
    
@app.delete("/tasks/delete/{task_id}")
def deletetask(task_id:int):
    for index, task in enumerate(all_tasks):
        if task["task_id"] == task_id:
            deleted_task = all_tasks.pop(index)
            return deleted_task
        
    
