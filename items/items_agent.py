from swarm import Agent
import random
import json
from typing import List

items = [
        { "item_id": 123,
          "item_desc": "keyboard",
          "location": "Oakland",
          "cost": 19.99,
          "discount_pct": 5
        },
        { "item_id": 426,
          "item_desc": "mouse",
          "location": "Oakland",
          "cost": 9.99,
          "discount_pct": 7
        },
        { "item_id": 178,
          "item_desc": "24 inch display",
          "location": "Oakland",
          "cost": 201.33,
          "discount_pct": 10
        },
        { "item_id": 195,
          "item_desc": "24 inch display",
          "location": "Bangkok",
          "cost": 201.33,
          "discount_pct": 10
        },
        { "item_id": 546,
          "item_desc": "24 inch display",
          "location": "Tokyo",
          "cost": 201.33,
          "discount_pct": 10
        }
    ]


def get_items_count(plan_name: str, scenario_name: str) -> int:
    """Get the number of items in a scenario of a supply chain plan. 
       Call this whenever you need to know the count of items in a plan or scenario, 
       for example when a user asks 'How many items are in my plan?'.
       Always ask the user for a plan name and a scenario name."""
    count = len(items) # random.randint(0,10000)
    print(f'[mock] There are {count} items in plan {plan_name} and scenario {scenario_name}')
    return count

def get_items(plan_name: str, scenario_name: str, display_fields: str = "*") -> str:
    """Get a list of items in a scenario of a supply chain plan. 
       Call this whenever you need to query items in a plan or scenario, 
       for example when a user asks 'List items are in my plan?'.
       Always ask the user for a plan name and a scenario name and display_fields as a list of field names
       to display in the output. The user can specify "*" if they want to display all fields.
    """
    
    values = []
    if display_fields == "*":
        values = items
    else:
        fields = display_fields.split(",")
        for item in items:
            new_dict = {key: item[key] for key in fields if key in item}
            values.append(new_dict)
    
    return json.dumps(values)

def get_item(plan_name: str, scenario_name: str, item_id: int) -> str:
    """Get the details for an item given the item id and in a scenario of a supply chain plan. 
       Call this whenever you need to get details or properties of an item in a plan or scenario, 
       for example when a user asks 'show item or get details for item or properties of an item?'.
       Always ask the user for a plan name and a scenario name and the item id.
    """
    # Create Dictionary
    values = []
    for item in items:
        if item["item_id"] == item_id:
            values.append(item)   
    return json.dumps(values)

def delete_item(plan_name: str, scenario_name: str, item_id: int) -> str:
    """Delete an item given the item id and in a scenario of a supply chain plan. 
       Call this whenever you need to delet an item in a plan or scenario, 
       for example when a user asks 'how do I delete an item?'.
       Always ask the user for a plan name and a scenario name and the item id.
    """
    # Create Dictionary
    for item in items:
        if item["item_id"] == item_id:
            items.remove(item)   
    return json.dumps(items)



items_agent = Agent(
    name="Items Agent",
    model='gpt-4o-mini',
    instructions="Help the user with questions about items in a plan or scenario",
    functions=[get_items_count, get_items, get_item, delete_item],
)