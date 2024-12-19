from swarm import Agent
import json
import datetime


horizon_start = datetime.date(2025, 1, 1)
horizon_end   = datetime.date(2025, 12, 31)
week1 = horizon_start  + datetime.timedelta(days=7)
week2 = week1 + datetime.timedelta(days=7)
week3 = week2 + datetime.timedelta(days=7)
week4 = week3 + datetime.timedelta(days=7)
week5 = week4 + datetime.timedelta(days=7)

orders = [
        { "order_id" : 744,
          "customer" : "Walmart",
          "item_desc" : "24 inch display",
          "requested_date": week3.isoformat(),
          "requested_quantity": 25,
          "planned_date": week3.isoformat(),
          "planned_quantity": 25,
          "days_late": 0
        },
        { "order_id" : 879,
          "customer" : "Costco",
          "item_desc" : "Keyboard",
          "requested_date": week1.isoformat(),
          "requested_quantity": 100,
          "planned_date": week3.isoformat(),
          "planned_quantity": 100,
          "days_late": 14
        },
        { "order_id" : 245,
          "customer" : "Best Buy",
          "item_desc" : "24 inch display",
          "requested_date": week2.isoformat(),
          "requested_quantity": 15,
          "planned_date": week2.isoformat(),
          "planned_quantity": 15,
          "days_late": 0
        }
    ]

def get_orders(plan_name: str, scenario_name: str, display_fields: str = "*") -> str:
    """Get a list of orders or sales orders in a scenario of a supply chain plan. 
       Call this whenever you need to query orders or sales orders in a plan or scenario, 
       for example when a user asks 'List the orders in my plan?'.
       Always ask the user for a plan name and a scenario name and display_fields as a list of field names
       to display in the output. The user can specify "*" if they want to display all fields.
       If the user does not supply a value for display_fields please use "*" as the value for the display_fields.
    """
    
    values = []
    if display_fields == "*":
        values = orders
    else:
        fields = display_fields.split(",")
        for order in orders:
            new_dict = {key: order[key] for key in fields if key in order}
            values.append(new_dict)
    
    return json.dumps(values)


orders_agent = Agent(
    name="Orders Agent",
    model='gpt-4o-mini',
    instructions="Help the user with questions about orders or sales orders in a plan or scenario",
    functions=[get_orders],
)