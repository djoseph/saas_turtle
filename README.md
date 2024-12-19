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
- [Dataset](#dataset)
- [Approach](#approach)
- [Usage](#usage)

# Overview

Should your Enterprise SaaS Application come bundled with an Agent?  Will an agentic layer amplify the capabilities provided by the REST API in most enterprise applications? This project tries to build a proof of concept of ideas discussed in linkedin posts [post1](https://www.linkedin.com/feed/update/urn:li:activity:7222769633836089344/) and [post2](https://www.linkedin.com/feed/update/urn:li:activity:7272455370579537920/).  We look at the following two use cases:

1. An agent providing a natural language interface for exploratory analysis using the REST API. 
2. An agent that can help a user craft complex solutions as a task list that can be submitted for asynchronous execution. The ability to build an entire task list before submitting for execution is very useful whan each task in the task list could be a long running operation with some tasks taking hours to complete execution. 

# Domain

Supply Chain Planning domain is used to explore these use cases. The entities or REST resources in our example are Items, Suppliers, Orders, Locations, Plans and Scenarios. Location is used to denote the city where a factory or distribution center is located. Items are things like Keyboard, Mouse and Displays that this fictitious company KM&D sells.  KM&D buys raw materials and finished goods from Suppliers. Each supplier has a daily capacity for each item they supply, which is the maximum amount of  the item that the supplier can make and ship on that day. Orders or Sales Orders represent the details of orders placed by Customers. Due to supplier capacity constraints it is not always possible to meet all the customer's sales orders on time or for the full quantity. Plans are created to match customer sales orders to available supplier capacity.Global events can disrupt supply chain operations. Often there is uncertainty when such disruptions occur and multiple scenarios are created to model possible outcomes.  

# Dataset

Our focus was on building an agent that can effectively use function calling for the two use cases. The data used is minimal and hardcoded as python dictionaries. The implementations of the api/functions are also very basic and in some cases just a print statement and a timer.sleep(10) to simulate a long running process like generating a feasible plan.

# Approach

A triage agent takes the user's natural language query and redirect to other agents. We have created a separate agent for each Entity or REST resource. We have used a separate agent items_agent, suppliers_agent, orders_agent to answer queries about Items, Suppliers and Orders respectively. We have used the function calling capabilities of the llm to do the heavy lifting. By having a separate agent for each entity, we have a reasonable number of functions per agent. The functions also broadly follow the REST pattern for CRUD operations like post, get, put and delete. 

A task_agent was used to create task lists, add tasks to task lists and submit task lists for execution. This was mainly to support the second use case where a users wants to craft a solution to a complex problem using a sequence of steps for the agent to execute synchronously or submit for asynchronous execution. 


# Usage

Some example queries to try.

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
- Show all items
```
User: show all items
Items Agent: get_items("plan_name"= "planA", "scenario_name"= "ScenarioB", "display_fields"= "*")
Items Agent: Here are the items in the plan "planA" and scenario "ScenarioB":

1. **Item ID:** 123
   - **Description:** Keyboard
   - **Location:** Oakland
   - **Cost:** $19.99
   - **Discount Percentage:** 5%

2. **Item ID:** 426
   - **Description:** Mouse
   - **Location:** Oakland
   - **Cost:** $9.99
   - **Discount Percentage:** 7%

3. **Item ID:** 178
   - **Description:** 24 Inch Display
   - **Location:** Oakland
   - **Cost:** $201.33
   - **Discount Percentage:** 10%

4. **Item ID:** 195
   - **Description:** 24 Inch Display
   - **Location:** Bangkok
   - **Cost:** $201.33
   - **Discount Percentage:** 10%

5. **Item ID:** 546
   - **Description:** 24 Inch Display
   - **Location:** Tokyo
   - **Cost:** $201.33
   - **Discount Percentage:** 10%
User: 
```
- get suppliers
```
User: get suppliers
Suppliers Agent: get_suppliers("plan_name"= "planA", "scenario_name"= "ScenarioB", "display_fields"= "*")
Suppliers Agent: Here are the suppliers for the plan "planA" and scenario "ScenarioB":

1. **Supplier ID:** 345
   - **Supplier Name:** Thai Pictures
   - **Item ID:** 195
   - **Item Description:** 24 Inch Display
   - **Location:** Bangkok
   - **Capacity:** 40
   - **Lead Time:** 10 days

2. **Supplier ID:** 987
   - **Supplier Name:** Japan Display
   - **Item ID:** 546
   - **Item Description:** 24 Inch Display
   - **Location:** Tokyo
   - **Capacity:** 60
   - **Lead Time:** 5 days
User: 
```

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

