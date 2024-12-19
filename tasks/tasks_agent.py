from swarm import Agent
import json
from tasks.tasks import *
from typing import List
import random

jobs: List[TaskManager] = []

def create_task_list(name: str) -> str:
    """Create a task list.  
       Call this whenever the user wants to create a task list.
       for example when a user asks 'I want to create a task list'.
       Always ask the user for a name for the task list.
    """
    job = TaskManager(name)
    jobs.append(job)
    return(f'Created  task list named {name}')


def add_create_scenario_task(task_list_name: str, plan_name: str, scenario_name: str) -> str:
    """Add a create scenario task.
       Call this whenever the user wants to add a create scenario task.
       for example when a user asks 'How do I add a task to create a new scenario?'.
       Always ask the user for the task_list_name, the plan_name and scenario_name.
    """
    for job in jobs:
        if job.name == task_list_name:
            job.add_task(CreateScenarioTask(plan_name, scenario_name))
            return (f'CreateScenarioTask added to list {task_list_name}')
    return(f'Could not find task list named {task_list_name}')

def add_update_supplier_capacity_task(task_list_name: str, plan_name: str, scenario_name: str, location: str, pct_change: float) -> str:
    """Add a task to update or mass update the capacity of suppliers at a particular location.
       Call this whenever the user wants to add a task to a task_list to update or 
       change the capacity of multiple suppliers at a location by a percentage.
       for example when a user asks 'I want to add a task to update supplier capacities by location?'.
       Always ask the user for a task_list_name, plan name, scenario name, location and percentage change.
    """
    for job in jobs:
        if job.name == task_list_name:
            job.add_task(UpdateSupplierCapacityTask(plan_name, scenario_name,location,pct_change))
            return (f'UpdateSupplierCapacityTask added to list {task_list_name}')
    return(f'Could not find task list named {task_list_name}')

def add_generate_plan_task(task_list_name: str, plan_name: str, scenario_name: str) -> str:
    """Add a task to generate a feasible supply chain plan respecting the supplier capacity constraints.
       Call this whenever the user wants to add a task to generate a new feasible plan.
       For example when a user asks 'How do I add a task to run the plan or how do I add a task to generate a new plan?'.
       Always ask the user for the task_list_name, the plan name and the name for the scenario.
    """
    for job in jobs:
        if job.name == task_list_name:
            job.add_task(GeneratePlanTask(plan_name, scenario_name))
            return(f'GeneratePlanTask added to list {task_list_name}')
    return(f'Could not find task list named {task_list_name}')

def run_tasks(task_list_name: str) -> str:
    """Run all tasks in the task list synchronously. The chat window will block as the tasks in the task list are run.
       Call this whenever the user wants to run all the tasks in a task_list in sequential order. 
       for example when a user asks 'run a task_list or run_tasks or execute a task list'.
       Always ask the user for a task_list_name.
    """
    for job in jobs:
        if job.name == task_list_name:
            job.run_tasks()
            return(f'Running tasks from list {task_list_name}')
    return(f'Could not find task list named {task_list_name}')

def submit_tasks(task_list_name: str) -> str:
    """Submit all tasks in the task list for execution asynchronously i.e. in a non blocking manner.
       This function will return with an execution_id and the user can check the status using the execution_id
       Call this whenever the user wants to submit a task list for execution. 
       for example when a user asks 'submit a task_list for execution or schedule a task_list for execution'.
       Always ask the user for a task_list_name.
    """
    for job in jobs:
        if job.name == task_list_name:
            #job_spec: str = json.dumps(job)
            # Mock submission of the task list to 
            print(f'[Mock] submitting {task_list_name} for execution')
            exec_id: int = random.randint(1000,10000)
            return(f'Submitted tasklist {task_list_name}. The execution_id is {exec_id}')
    return(f'Could not find task list named {task_list_name}')
        


tasks_agent = Agent(
    name="Tasks Agent",
    model='gpt-4o-mini',
    instructions="Help the user with creating task lists, adding tasks to task list and running tasks from a task list",
    functions=[create_task_list, submit_tasks, run_tasks, add_generate_plan_task, add_update_supplier_capacity_task, add_create_scenario_task],
)