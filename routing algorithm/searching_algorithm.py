import heapq
from heuristic_function import heuristic_cost_estimate as hf

def a_star_algorithm(start_node, end_node, adjacency_list, heuristic_func):
    # Initialize start and end nodes
    start_node.g = 0
    start_node.h = heuristic_func(start_node, end_node)
    start_node.f = start_node.h
    end_node.g = float('inf')

    # Initialize the open and closed sets
    open_set = []
    closed_set = set()

    # Push the start node into the open set
    heapq.heappush(open_set, start_node)

    # Loop until the open set is empty
    while open_set:
        # Pop the node with the lowest f value from the open set
        current_node = heapq.heappop(open_set)

        # Check if we have reached the end node
        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        # Add the current node to the closed set
        closed_set.add(current_node)

        # Loop through the neighbors of the current node
        for neighbor_node in adjacency_list[current_node]:
            # Check if the neighbor node is already in the closed set
            if neighbor_node in closed_set:
                continue

            # Calculate the tentative g score for the neighbor node
            tentative_g_score = current_node.g + neighbor_node.cost

            # Check if the neighbor node is not in the open set
            if neighbor_node not in open_set:
                neighbor_node.g = tentative_g_score
                neighbor_node.h = heuristic_func(neighbor_node, end_node)
                neighbor_node.f = neighbor_node.g + neighbor_node.h
                neighbor_node.parent = current_node
                heapq.heappush(open_set, neighbor_node)
            elif tentative_g_score < neighbor_node.g:
                neighbor_node.g = tentative_g_score
                neighbor_node.f = neighbor_node.g + neighbor_node.h
                neighbor_node.parent = current_node
                heapq.heapify(open_set)

    # No path found
    return None



def rank_routes(routes, start, end, heuristic_func):
    # initialize heap and visited set
    heap = [(0, start)]
    visited = set()

    # initialize dictionary to store costs
    costs = {start: 0}

    # initialize dictionary to store paths
    paths = {}

    # while heap is not empty
    while heap:
        # get node with lowest cost so far
        curr_cost, curr_node = heapq.heappop(heap)

        # if node is end node, return path
        if curr_node == end:
            path = []
            while curr_node in paths:
                path.append(curr_node)
                curr_node = paths[curr_node]
            path.append(start)
            path.reverse()
            return path

        # add node to visited set
        visited.add(curr_node)

        # get all neighbors of current node
        neighbors = get_neighbors(curr_node)

        # for each neighbor
        for neighbor in neighbors:
            # check if neighbor has already been visited
            if neighbor in visited:
                continue

            # calculate new cost to reach neighbor from current node
            new_cost = costs[curr_node] + get_cost(curr_node, neighbor)

            # if neighbor is not in heap or new cost is lower than old cost
            if neighbor not in (x[1] for x in heap) or new_cost < costs[neighbor]:
                # update cost and path dictionaries
                costs[neighbor] = new_cost
                priority = new_cost + heuristic_func(neighbor, end)
                heapq.heappush(heap, (priority, neighbor))
                paths[neighbor] = curr_node

    # if end node is not found, return None
    return None
