"""
Problem Summary:
We have to check for a given rectangle and circle if they are ovrelapping,
 based on their representation in a coordinate system.

Approach1: 
Representing the distance parallel to the X and Y axes as a triangle,
such that the distance from the point on the rectangle closest to the center of the circle-
forms the hypotenuse of the triangle.
If that dictance smaller than the radius they overlap.

Approach2: 
We find the exact coordinates (X, Y) of the point on the rectangle that is closest 
to the circle's center.
We do this by "clamping" the circle's center coordinates so they don't exceed the rectangle's boundaries. 
Then, we calculate the distance between this point and the circle's center.

"""

# If the circle center's x-coordinate is to the left of the rectangle's left side, 
# the distance parallel to the x-axis is the difference between the side and the center;
# otherwise, if it is greater than the right side,
# the distance is the difference between the center and the right side;
# and if it lies between the right and left sides, the distance is 0.
# The same applies to the y-coordinate.
# Time Complexity: O(1)
# Space Complexity: O(1) - constant number of extra variables.
class Solution1:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the shortest horizontal distance to the rectangle
        x = x1 - xCenter if xCenter < x1 else xCenter - x2 if xCenter > x2 else 0
        # Find the shortest vertical distance to the rectangle
        y = y1 - yCenter if yCenter < y1 else yCenter - y2 if yCenter > y2 else 0

        # Check if the squared distance is within the squared radius (Pythagorean theorem)
        return x ** 2 + y ** 2 <= radius ** 2

# # # # # # # # # # # # # # # # # # 


# Find the closest point (x, y) on the rectangle to the circle's center.
# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution2:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # min(xCenter, x2) ensures the point doesn't go past the right edge.
        # max(x1, ...) ensures the point doesn't go past the left edge.
        #same for y
        x = max(x1,min(xCenter, x2)) #the nearest X
        y = max(y1,min(yCenter, y2)) #the nearest Y

        return (xCenter - x) ** 2 + (yCenter - y)* 2 <= radius ** 2 #distance formmula *