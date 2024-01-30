# use set to erase already existing paths where as priority queue can't 
# there is no explicit improvement in the TC but depending on the cases we can use set or pq
def dijkstraSet(graph,src):
    distances = {vertex : float('inf') for vertex in graph}
    distances[src] = 0
    
    st = set()
    st.add((0,src))
    while st:
        current_distance, current_vertex = st.pop()
        
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance  = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                st.add((distance,neighbor))
    
    return distances



example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(dijkstraSet(example_graph, 'W'))