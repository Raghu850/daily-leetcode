class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0
            
        
        points.sort(key=lambda x: x[1])
        
        arrows = 0
        arrow_position = None
        
        for start, end in points:
           
            if arrow_position is None or start > arrow_position:
                arrows += 1
                arrow_position = end
                
        return arrows
        