# Building an Agentic Layer for Enterprise SaaS Applications

Team SaaS Turtle's submission for the [LLM Agents MOOC Hackathon](https://rdi.berkeley.edu/llm-agents-hackathon/) as part of the [LLM Agents MOOC](https://llmagents-learning.org/f24). This project uses the [openai/swarm](https://github.com/openai/swarm) which has an [MIT](https://choosealicense.com/licenses/mit/) license and uses an approach similar to the swarm [Triage Agent Example](https://github.com/openai/swarm/blob/main/examples/triage_agent/README.md). 

## Setup

To run the agent Swarm:

1. Run

```shell
python3 run.py
```


## Table of Contents

- [Overview](#overview)
- [Domain](#domain)
- [Usage](#usage)

# Overview

Should your Enterprise SaaS Application come bundled with an Agent?  Will an agentic layer amplify the capabilities provided by the REST API in most enterprise applications? This project tries to build a proof of concept of ideas discussed in linkedin posts [post1](https://www.linkedin.com/feed/update/urn:li:activity:7222769633836089344/) and [post2](https://www.linkedin.com/feed/update/urn:li:activity:7272455370579537920/).  We look at the following two use cases:

1. An agent providing a natural language interface for exploratory analysis using the REST API. 
2. An agent that can help a user craft complex solutions as a task list that can be submitted for asynchronous execution. The ability to build an entire task list before submitting for execution is very useful whan each task in the task list could be a long running operation with some tasks taking hours to complete execution. 

# Domain

Supply Chain Planning domain is used to explore these use cases. The entities or REST resources in our example are Items, Suppliers, Orders, Locations, Plans and Scenarios. Location is used to denote the city where a factory or distribution center is located. Items are things like Keyboard, Mouse and Displays that this fictitious company KM&D sells.  KM&D buys raw materials and finished goods from Suppliers. Each supplier has a daily capacity for each item they supply, which is the maximum amount of  the item that the supplier can make and ship on that day. Orders or Sales Orders represent the details of orders placed by Customers. Due to supplier capacity constraints it is not always possible to meet all the customer's sales orders on time or for the full quantity. Plans are created to match customer sales orders to available supplier capacity.Global events can disrupt supply chain operations. Often there is uncertainty when such disruptions occur and multiple scenarios are created to model possible outcomes. 



# Usage

Some example queries to try.

## TASK LIST

- Jill is a supply chain manager at company KM&D. She receives a news report about heavy rains and flooding in Thailand with potential factory closures. She wants to run multiple scenarios to understand what impact it has on the supply chain plan and if any customer sales orders will have to be shipped late resulting in a revenue short fall for the company this quarter. She hopes to have all the answers before she meets her manager later in the day. She creates a scenario F50 to model a 50% loss of supplier capacity in Bangkok. She has multiple scenarios to model the various possible outcomes like 25%, 50%, 75% loss of supplier capacity in Bangkok. Hence she won't have time to babysit each task in the task list as some tasks in her task list for example generate a feasible plan can take hours to complete. So she will submit each task list for asynchronous execution. She will use the returned execution id later to check the results and create a nice report before the meeting with her manger.
 
```
Starting Swarm CLI 🐝
User: create new task list
Triage Agent: transfer_to_tasks()
Tasks Agent: What would you like to name your new task list?
User: F50
Tasks Agent: create_task_list("name"= "F50")
Tasks Agent: The task list named "F50" has been created successfully! What would you like to do next? You can add tasks, run tasks, or submit the task list for execution.
User: add a create scenario task               
Tasks Agent: Please provide me with the following details to add a create scenario task:

1. Plan name: 
2. Scenario name: 
User: planA, F50
Tasks Agent: add_create_scenario_task("task_list_name"= "F50", "plan_name"= "planA", "scenario_name"= "F50")
Tasks Agent: The create scenario task has been added to the task list "F50." What would you like to do next? You can add more tasks, run the tasks, or submit the task list for execution.
User: add a task to update supplier capacities
Tasks Agent: Please provide the following details to add a task to update supplier capacities:

1. Plan name:
2. Scenario name:
3. Location:
4. Percentage change (e.g., 10 for a 10% increase, -5 for a 5% decrease):
User: planA, F50, Bangkok, -50
Tasks Agent: add_update_supplier_capacity_task("task_list_name"= "F50", "plan_name"= "planA", "scenario_name"= "F50", "location"= "Bangkok", "pct_change"= -50)
Tasks Agent: The task to update supplier capacities has been added to the task list "F50." 

What would you like to do next? You can add more tasks, run the tasks, or submit the task list for execution.
User: add a task to generate a feasible plan
Tasks Agent: Please provide the following details to add a task to generate a feasible plan:

1. Plan name:
2. Scenario name: 
User: planA, F50
Tasks Agent: add_generate_plan_task("task_list_name"= "F50", "plan_name"= "planA", "scenario_name"= "F50")
Tasks Agent: The task to generate a feasible plan has been added to the task list "F50." 

What would you like to do next? You can add more tasks, run the tasks, or submit the task list for execution.
User: submit task list F50 for execution
[Mock] submitting F50 for execution
Tasks Agent: submit_tasks("task_list_name"= "F50")
Tasks Agent: The task list "F50" has been submitted for execution. You can check the status of the execution using the execution ID: **3581**.

Is there anything else you would like to do?
```
- You want to create a task list but run it synchronously i.e., you have the time to babysit each task in the task list.
```
User: create a new task list for the plan
Tasks Agent: transfer_back_to_triage()
Triage Agent: Please provide a name for your new task list.
User: F100
Triage Agent: transfer_to_tasks()
Tasks Agent: create_task_list("name"= "F100")
Tasks Agent: The task list named "F100" has been created successfully. What tasks would you like to add to this task list?
User: add a task to create a scenario
Tasks Agent: Please provide the plan name and the scenario name for the new scenario you want to create in the "F100" task list.
User: planA, F100
Tasks Agent: add_create_scenario_task("task_list_name"= "F100", "plan_name"= "planA", "scenario_name"= "F100")
Tasks Agent: The task to create the scenario "F100" under the plan "planA" has been successfully added to the task list "F100." Would you like to add more tasks, run the tasks immediately, or submit the task list for execution?
User: add a task to update supplier capacity
Tasks Agent: Please provide the following details to add the task to update supplier capacity:

1. Plan name
2. Scenario name
3. Location
4. Percentage change (e.g., increase or decrease in capacity)
User: planA, F100, Bangkok, -100
Tasks Agent: add_update_supplier_capacity_task("task_list_name"= "F100", "plan_name"= "planA", "scenario_name"= "F100", "location"= "Bangkok", "pct_change"= -100)
Tasks Agent: The task to update the supplier capacity by -100% at the location "Bangkok" under the plan "planA" has been added to the task list "F100." 

Would you like to add more tasks, run the tasks immediately, or submit the task list for execution?
User: add a task to generate a feasible plan
Tasks Agent: Please provide the following details to add the task to generate a feasible plan:

1. Plan name
2. Scenario name
User: planA, F100
Tasks Agent: add_generate_plan_task("task_list_name"= "F100", "plan_name"= "planA", "scenario_name"= "F100")
Tasks Agent: The task to generate a feasible plan under the plan "planA" and scenario "F100" has been successfully added to the task list "F100." 

Would you like to add more tasks, run the tasks immediately, or submit the task list for execution?
User: run the task immediately
Running task: CreateScenarioTask
[mock] Start Copying base scenario from plan planA to create new scenario F100
[mock] End Created new scenario F100
Task CreateScenarioTask completed.
Running task: UpdateSupplierCapacityTask
Executing update supplier capacity task
[{"supplier_id": 345, "supplier_name": "Thai Pictures", "item_id": 195, "item_desc": "24 inch display", "location": "Bangkok", "capacity": 0.0, "lead_time": 10}, {"supplier_id": 987, "supplier_name": "Japan Display", "item_id": 546, "item_desc": "24 inch display", "location": "Tokyo", "capacity": 60, "lead_time": 5}]
Task UpdateSupplierCapacityTask completed.
Running task: GeneratePlanTask
[mock] Start Generating a feasible material constrained plan for plan planA and scenario F100
[mock] End Generating a feasible material constrained plan for plan planA and scenario F100
Task GeneratePlanTask completed.
Tasks Agent: run_tasks("task_list_name"= "F100")
Tasks Agent: The tasks from the task list "F100" are now running. Please wait a moment while I execute them. 

If you have any further requests or need assistance while the tasks are running, feel free to let me know!

```

## COUNT


- How many items are there in the plan?
```
Starting Swarm CLI 🐝
User: How many items are there in the plan?
Triage Agent: transfer_to_items()
Items Agent: Please provide me with the name of your plan and the scenario name so I can find out the number of items for you.
User: planA, ScenarioB
[mock] There are 5 items in plan planA and scenario ScenarioB
Items Agent: get_items_count("plan_name"= "planA", "scenario_name"= "ScenarioB")
Items Agent: There are 5 items in the plan "planA" and scenario "ScenarioB".
```
## GET

- Get a list of sales orders
```
User: get orders
Orders Agent: get_orders("plan_name"= "planA", "scenario_name"= "ScenarioB", "display_fields"= "*")
Orders Agent: Here are the orders in the plan "planA" and scenario "ScenarioB":

1. **Order ID:** 744
   - **Customer:** Walmart
   - **Item Description:** 24 Inch Display
   - **Requested Date:** January 22, 2025
   - **Requested Quantity:** 25
   - **Planned Date:** January 22, 2025
   - **Planned Quantity:** 25
   - **Days Late:** 0

2. **Order ID:** 879
   - **Customer:** Costco
   - **Item Description:** Keyboard
   - **Requested Date:** January 8, 2025
   - **Requested Quantity:** 100
   - **Planned Date:** January 22, 2025
   - **Planned Quantity:** 100
   - **Days Late:** 14

3. **Order ID:** 245
   - **Customer:** Best Buy
   - **Item Description:** 24 Inch Display
   - **Requested Date:** January 15, 2025
   - **Requested Quantity:** 15
   - **Planned Date:** January 15, 2025
   - **Planned Quantity:** 15
   - **Days Late:** 0
User:
```
- Get item details by item_id
```
User: get item with item id 125
Tasks Agent: transfer_back_to_triage()
Triage Agent: Please hold on while I connect you to the appropriate agent for your request regarding the item. One moment, please.
transfer_to_items()
Items Agent: Please provide the plan name and the scenario name for the item with ID 125 that you would like to retrieve.
User: planA, scenarioB
Items Agent: get_item("plan_name"= "planA", "scenario_name"= "scenarioB", "item_id"= 125)
Items Agent: It seems that there are no items found with the ID 125 in the plan "planA" and scenario "scenarioB." 

If you need assistance with anything else or want to check for a different item, please let me know!
User: get item with item id 123 for planA and scenarioB
Items Agent: get_item("plan_name"= "planA", "scenario_name"= "scenarioB", "item_id"= 123)
Items Agent: Here are the details for the item with ID 123 in the plan "planA" and scenario "scenarioB":

- **Item ID:** 123
- **Description:** Keyboard
- **Location:** Oakland
- **Cost:** $19.99
- **Discount Percentage:** 5%
```
## UPDATE

- Update supplier capacity
```
User: update supplier capacity
Suppliers Agent: Please provide the following details to update the supplier capacity:

1. Plan name
2. Scenario name
3. Location
4. Percentage change (e.g., increase or decrease in capacity)
User: planA, scenarioB, Tokyo, 25
Suppliers Agent: update_supplier_capacity_for_location("plan_name"= "planA", "scenario_name"= "scenarioB", "location"= "Tokyo", "pct_change"= 25)
Suppliers Agent: The supplier capacity has been successfully updated for the location Tokyo under the plan "planA" and scenario "scenarioB." 

Here are the details of the suppliers after the update:

1. **Supplier ID:** 987
   - **Supplier Name:** Japan Display
   - **Item ID:** 546
   - **Item Description:** 24 inch display
   - **Location:** Tokyo
   - **Updated Capacity:** 75.0
   - **Lead Time:** 5 days

If you need any further assistance or have more requests, feel free to ask!
User: 
```
## DELETE

- delete an item by item id
```
User: delete item with item id 123
Items Agent: delete_item("plan_name"= "planA", "scenario_name"= "scenarioB", "item_id"= 123)
Items Agent: The item with ID 123 has been successfully deleted from the plan "planA" and scenario "scenarioB." 

If you need assistance with anything else, please let me know!
```



