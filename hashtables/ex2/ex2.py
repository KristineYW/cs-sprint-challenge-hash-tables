#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # need to get from source "NONE" to the destination "NONE"
    
    ht = {}

    for element in tickets:
        ht[element.source] = element.destination
    
    current = ht["NONE"] # starting point
    route = [current]

    while current != "NONE":
        current = ht[current]
        route.append(current)

    return route
