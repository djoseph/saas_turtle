from swarm import Agent
from items.items_agent import items_agent
from suppliers.suppliers_agent import suppliers_agent
from orders.orders_agent import orders_agent
from tasks.tasks_agent import tasks_agent



triage_agent = Agent(
    name="Triage Agent",
    model='gpt-4o-mini',
    instructions="Determine which agent is best suited to handle the user's request, and transfer the conversation to that agent.",
)


def transfer_back_to_triage():
    """Call this function if a user is asking about a topic that is not handled by the current agent."""
    return triage_agent


def transfer_to_suppliers():
    return suppliers_agent


def transfer_to_orders():
    return orders_agent

def transfer_to_items():
    return items_agent

def transfer_to_tasks():
    return tasks_agent


triage_agent.functions = [transfer_to_suppliers, transfer_to_orders, transfer_to_items, transfer_to_tasks]
suppliers_agent.functions.append(transfer_back_to_triage)
orders_agent.functions.append(transfer_back_to_triage)
items_agent.functions.append(transfer_back_to_triage)
tasks_agent.functions.append(transfer_back_to_triage)