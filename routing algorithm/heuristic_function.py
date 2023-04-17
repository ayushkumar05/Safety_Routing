import math

def heuristic_cost_estimate(start, end, crime_data, weather_data, road_data):
    # Calculate the straight-line distance between start and end points
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    straight_line_distance = math.sqrt(dx*dx + dy*dy)

    # Calculate the cost based on crime, weather, and road conditions
    crime_cost = crime_data.get_cost(start, end)
    weather_cost = weather_data.get_cost(start, end)
    road_cost = road_data.get_cost(start, end)

    # Combine the costs using some weighting factor
    total_cost = 0.5 * straight_line_distance + 0.2 * crime_cost + 0.2 * weather_cost + 0.1 * road_cost

    return total_cost
