import math
class distance_Solver:
    def __init__(self, coordinates, start, end):
        self.past_paths = {}
        self.coordinates = coordinates
        self.start = start
        self.end = end
        best_distance = self.solve((start,), start, 0)
        print("Shortest total distance:", round(best_distance, 2))

    def distances(self, x1, x2, y1, y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def solve(self, visited, current, total_distance):
        
        if len(visited) == len(self.coordinates) - 1:
            return total_distance + self.distances(self.coordinates[current][0], self.coordinates[city][0], self.coordinates[current][1], self.coordinates[city][1])

        path = (visited, current)
        if path in self.past_paths:
            return self.past_paths[path]

        best = float('inf')

        for city in self.coordinates:
            if city not in visited and city != self.end:
                dist = self.distances(self.coordinates[current][0], self.coordinates[city][0], self.coordinates[current][1], self.coordinates[city][1])

                new_visited = visited + (city,)
                result = self.solve(new_visited, city, total_distance + dist)

                if result < best:
                    best = result

        self.past_paths[path] = best
        return best


dictionary_of_coords = {
    1: (26,19),
    2: (90,28),
    3: (30,37),
    4: (12,46),
    5: (18,55),
    6: (44,64),
    7: (61,73),
    8: (74,82),
    9: (43,91),
    10: (21,100)
}

start, end = 2, 10
distance_Solver(dictionary_of_coords, start, end)
