from A_star_search import graph, weights, heuristic, astar
import time

graph = {
    "Disaneng": {"Mahikeng": 35, "Madibogo": 25},
    "Mahikeng": {"Mmabatho": 10, "Lichtenburg": 60},
    "Mmabatho": {"Slurry": 15},
    "Slurry": {"Zeerust": 50},
    "Zeerust": {"Groot Marico": 20},
    "Groot Marico": {"Bakerville": 25},
    "Bakerville": {"Lichtenburg": 40},
    "Lichtenburg": {"Coligny": 35},
    "Madibogo": {"Ottosdal": 45},
    "Ottosdal": {"Sannieshof": 30},
    "Sannieshof": {"Delareyville": 20},
    "Delareyville": {"Coligny": 25},
    "Coligny": {}
}

heuristic = {
    "Disaneng": 100,
    "Mahikeng": 80,
    "Mmabatho": 70,
    "Slurry": 60,
    "Zeerust": 50,
    "Groot Marico": 40,
    "Bakerville": 30,
    "Lichtenburg": 20,
    "Madibogo": 75,
    "Ottosdal": 60,
    "Sannieshof": 50,
    "Delareyville": 30,
    "Coligny": 0
}

def simulate_path(path):
    print("\n Truck traveling...\n")
    for node in path:
        print(f"Car is now at: {node}")
        time.sleep(1)
    print("\nDestination reached!")
    
    print("\nVisited Order:", visit_order)
    print("Optimal Path:", path)
    print("Total Cost:", tot_cost)
    

path, visit_order, tot_cost = astar(graph, weights, heuristic, "Disaneng", "Coligny")

simulate_path(path)