import time
from suppliers.suppliers_agent import update_supplier_capacity_for_location

class Task:

    def __init__(self, name: str):
        self.name = name
    
    def run(self):
        print("Executing generic task")

class CreateScenarioTask(Task):

    def __init__(self,plan_name: str, scenario_name: str, name: str = "CreateScenarioTask"):
        super().__init__(name)
        self.plan_name = plan_name
        self.scenario_name = scenario_name

    def run(self):
        print(f'[mock] Start Copying base scenario from plan {self.plan_name} to create new scenario {self.scenario_name}')
        time.sleep(5) #sleep for 5 seconds to simulate creating a deep copy
        print(f'[mock] End Created new scenario {self.scenario_name}')

class UpdateSupplierCapacityTask(Task):

    def __init__(self, plan_name: str, scenario_name: str, location: str, capacity: int, name: str = "UpdateSupplierCapacityTask"):
        super().__init__(name)
        self.plan_name = plan_name
        self.scenario_name = scenario_name
        self.location = location
        self.capacity = capacity

    def run(self):
        print("Executing update supplier capacity task")
        res = update_supplier_capacity_for_location(self.plan_name, self.scenario_name, self.location, self.capacity)
        print(res)

class GeneratePlanTask(Task):

    def __init__(self, plan_name: str, scenario_name: str, name: str = "GeneratePlanTask"):
        super().__init__(name)
        self.plan_name = plan_name
        self.scenario_name = scenario_name

    def run(self):
        print(f'[mock] Start Generating a feasible material constrained plan for plan {self.plan_name} and scenario {self.scenario_name}')
        time.sleep(8) #sleep for 8 seconds to simulate a plan run
        print(f'[mock] End Generating a feasible material constrained plan for plan {self.plan_name} and scenario {self.scenario_name}')


class TaskManager:
    def __init__(self,name: str):
        self.tasks = []
        self.name = name

    def add_task(self, task):
        self.tasks.append(task)

    def run_tasks(self):
        for task in self.tasks:
            print(f"Running task: {task.name}")
            task.run()
            print(f"Task {task.name} completed.")



if __name__ == "__main__":
    manager = TaskManager("Job1")
    manager.add_task(CreateScenarioTask("planA","ScenarioB"))
    manager.add_task(UpdateSupplierCapacityTask("planA","scenarioB","Bangkok",7))
    manager.add_task(GeneratePlanTask("planA","ScenarioB"))
    manager.run_tasks()