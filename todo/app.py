from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)
tasks = []
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        task_content = request.form["task"]
        priority = request.form.get("priority", "Low")
        category = request.form.get("category", "General")
        completion_date = request.form.get("completion_date", None)
        if completion_date:
            completion_date = datetime.strptime(completion_date, "%Y-%m-%d")

          tasks.append({
            "id": len(tasks) + 1,
            "content": task_content,
            "completed": False,
            "priority": priority,
            "category": category,
            "completion_date": completion_date
        })
        return redirect("/")
    else:
        return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    
    task_to_remove = next((task for task in tasks if task["id"] == id), None)
    if task_to_remove:
        tasks.remove(task_to_remove)
    return redirect("/")

@app.route("/update/<int:id>", methods=["POST", "GET"])
def update(id):
    
    task_to_update = next((task for task in tasks if task["id"] == id), None)
    if request.method == "POST":
        if task_to_update:
            task_to_update["content"] = request.form["task"]
            task_to_update["priority"] = request.form["priority"]
            task_to_update["category"] = request.form["category"]
            task_to_update["completion_date"] = request.form.get("completion_date", task_to_update["completion_date"])
        return redirect("/")
    else:
        return render_template("index.html", update_task=task_to_update, tasks=tasks)

@app.route("/toggle/<int:id>")
def toggle(id): 
    task_to_toggle = next((task for task in tasks if task["id"] == id), None)
    if task_to_toggle:
        task_to_toggle["completed"] = not task_to_toggle["completed"]
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)
