import random
 
def objective_function(x):
    return -(x - 3) ** 2 + 9
 
def hill_climbing(start, step_size=0.1, max_iterations=1000):
    current_x = start
    current_value = fun(current_x)
 
    for _ in range(max_iterations):
        neighbors = [current_x - step_size, current_x + step_size]
        next_x = max(neighbors, key=fun)
        next_value = objective_function(next_x)
 
        if next_value <= current_value:
            break
 
        current_x, current_value = next_x, next_value
 
    return current_x, current_value
 

start_x = random.uniform(0, 6)
optimal_x, optimal_value = hill_climbing(start_x)
 
print(f"Optimal x: {optimal_x}")
print(f"Function value at optimal x: {optimal_value}")
 








