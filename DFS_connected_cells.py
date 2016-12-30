class longest_connected_region:
    
    def __init__(self,grid):
       
        self.grid = grid
        self.visited = []
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        
        for row in range(self.rows):
            self.visited.append([])

            for col in range(self.cols):
                self.visited[row].append(False)
        
        self.max_length = 0
    
    def check_is_within_bounds_and_filled(self,row,col):
        
        return row >= 0 and row < self.rows and col >= 0 and col < self.cols and self.grid[row][col] == 1
    
    def get_longest_connected_region(self):
        
        for row in range(self.rows):
            for col in range(self.cols):
                val = self.grid[row][col]
                if val == 0 or self.visited[row][col]:
                    continue
                self.max_length = max(
                    self.max_length,  self.get_longest_connected_region_impl(row,col))
                
        
        return self.max_length
        
    def get_longest_connected_region_impl(self, row, col):
        
        if self.visited[row][col]:
            return 0
        
        self.visited[row][col] = True
        
        cur_length = 1
        
        # [i-1][j-1]
        if self.check_is_within_bounds_and_filled(row-1,col-1):
            cur_length += self.get_longest_connected_region_impl(row-1,col-1)
            
        # [i-1][j]
        if self.check_is_within_bounds_and_filled(row-1,col):
            cur_length += self.get_longest_connected_region_impl(row-1,col)
            
        # [i-1][j+1]
        if self.check_is_within_bounds_and_filled(row-1,col+1):
            cur_length += self.get_longest_connected_region_impl(row-1,col+1)
            
            
        # [i][j-1]
        if self.check_is_within_bounds_and_filled(row,col-1):
            cur_length += self.get_longest_connected_region_impl(row,col-1)
            
        # [i][j+1]
        if self.check_is_within_bounds_and_filled(row,col+1):
            cur_length += self.get_longest_connected_region_impl(row,col+1)
            
        # [i+1][j-1]
        if self.check_is_within_bounds_and_filled(row+1,col-1):
            cur_length += self.get_longest_connected_region_impl(row+1,col-1)
            
        # [i+1][j]
        if self.check_is_within_bounds_and_filled(row+1,col):
            cur_length += self.get_longest_connected_region_impl(row+1,col)
            
        # [i+1][j+1]
        if self.check_is_within_bounds_and_filled(row+1,col+1):
            cur_length += self.get_longest_connected_region_impl(row+1,col+1)
            
            
        return cur_length
            
        
        
        
            
    
        

def get_biggest_region(grid):
    
    lcr = longest_connected_region(grid)
    return lcr.get_longest_connected_region()    
    
    
    

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)

