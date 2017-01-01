import sys

class Graph:
    
    def __init__(self, numV):
        self.numVertexes = numV
        
        self.adjMat = [[0 for col in range(self.numVertexes)] for row in range(self.numVertexes)]
        
        
    def connect(self, vert1, vert2):
        self.adjMat[vert1][vert2] = self.adjMat[vert2][vert1] = 1
        
    def find_min(self, dist, visited):
        
        minDistVertex = -1
        minDist = sys.maxint
        for v in range(self.numVertexes):
            if visited[v]:
                continue
            if dist[v] == -1:
                continue
            if minDistVertex == -1 or dist[v] < minDist:
                minDistVertex = v
                minDist = dist[v]
        
        return minDistVertex
                
            
        
        
    def find_all_distances(self, src):
        
        dist = []
        visited = []
        
        for v in range(self.numVertexes):
            dist.append(-1)
            visited.append(False)
            
        dist[src] = 0
        
        while True:
            minDistVertex = self.find_min(dist, visited)
            
            if minDistVertex == -1:
                break
            
            for neighbor in xrange(len(self.adjMat[minDistVertex])):
                if self.adjMat[minDistVertex][neighbor] == 0:
                    continue
                if neighbor == minDistVertex:
                    continue
                    
                new_dist = dist[minDistVertex] + 6
                if dist[neighbor] == -1 or new_dist < dist[neighbor] :
                    dist[neighbor] = new_dist
                    continue
           
            visited[minDistVertex] = True
            
        dist_string = ''
        for v in range(self.numVertexes):
            if v == src:
                continue
            if v == self.numVertexes - 1:
                dist_string += str(dist[v])
            else:
                dist_string += str(dist[v]) + ' '
                
        return dist_string
                 
        


t = input()
isFirstLine = True
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1) 
    s = input()
    dist_string = graph.find_all_distances(s-1)
    
    if not isFirstLine:
        sys.stdout.write('\n')
    isFirstLine = False
    sys.stdout.write(dist_string)
