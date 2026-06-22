#https://www.geeksforgeeks.org/python/deque-in-python/
# We use the collections module to implement queue in code
from collections import deque

# Creates an empty queue
helpdesk_tickets = deque()

# Add tickets
helpdesk_tickets.append("Ticket 01: Forgot password")
helpdesk_tickets.append("Ticket 02: Can't find my keyboard")
helpdesk_tickets.append("Ticket 03: Monitor wont turn on")

# Remove the first ticket that was added
first_ticket = helpdesk_tickets.popleft()
print(first_ticket)

# Shows how many tickets left in queue
print(len(helpdesk_tickets))
