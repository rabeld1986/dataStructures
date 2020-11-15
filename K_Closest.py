
"""We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)"""


from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
            d = {}
            for i in range(len(points)):
                eu = round(math.sqrt(((0-points[i][0])**2) + ((0-points[i][1])**2)),6)
                if eu in d:
                    d[eu+0.1] = points[i]
                else:
                    
                    d[eu] = points[i]
                
            key = sorted(d.keys())
            for k in range(len(d)):
                points[k] = d[key[k]]
                
            return points[:K] 
