'''You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
'''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str: 
        source = set() #keep a track of sources in a hashset
        for path in paths:
            source.add(path[0])
        
        for path in paths:
            if path[1] not in source:#check if the destination is in the source set or notr
                return path[1]
        