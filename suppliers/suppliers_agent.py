from swarm import Agent
import json

suppliers = [
        { "supplier_id" : 345,
          "supplier_name" : "Thai Pictures",
          "item_id": 195,
          "item_desc": "24 inch display",
          "location": "Bangkok",
          "capacity": 40,
          "lead_time": 10
        },
        { "supplier_id" : 987,
          "supplier_name" : "Japan Display",
          "item_id": 546,
          "item_desc": "24 inch display",
          "location": "Tokyo",
          "capacity": 60,
          "lead_time": 5
        }
    ]

def get_suppliers(plan_name: str, scenario_name: str, display_fields: str = "*") -> str:
    """Get a list of suppliers in a scenario of a supply chain plan. 
       Call this whenever you need to query suppliers or item_suppliers in a plan or scenario, 
       for example when a user asks 'List the suppliers in my plan?'.
       Always ask the user for a plan name and a scenario name and display_fields as a list of field names
       to display in the output. The user can specify "*" if they want to display all fields.
       If the user does not supply a value for display_fields please use "*" as the value for the display_fields.
    """
    
    values = []
    if display_fields == "*":
        values = suppliers
    else:
        fields = display_fields.split(",")
        for supplier in suppliers:
            new_dict = {key: supplier[key] for key in fields if key in supplier}
            values.append(new_dict)
    
    return json.dumps(values)

def update_supplier_capacity_for_location(plan_name: str, scenario_name: str, location: str, pct_change: float) -> str:
    """Update or mass update the capacity of suppliers at a particular location.
       Call this whenever you need to update the capacity of multiple suppliers at a location to a percentage of their current capacity.
       for example when a user asks 'how do I update supplier capacities by location?'.
       Always ask the user for a plan name, scenario name, location and percentage change.
    """
    for supplier in suppliers:
        if supplier["location"] == location:
            supplier["capacity"] += supplier["capacity"] * (pct_change/100)
    return json.dumps(suppliers)



suppliers_agent = Agent(
    name="Suppliers Agent",
    model='gpt-4o-mini',
    instructions="Help the user with questions about suppliers or item_suppliers in a plan or scenario",
    functions=[get_suppliers, update_supplier_capacity_for_location],
)