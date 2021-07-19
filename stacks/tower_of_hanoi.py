class Solution:
    def __init__(self, n):
        self.n = n
    
    def required_sequence(self, n, source, destination, helper):
        if n == 1:
            print(f"Move plate from {source} to {destination}.")
            return

        self.required_sequence(n - 1, source, helper, destination)
        print(f"Move plate from {source} to {destination}.")
        self.required_sequence(n - 1, helper, destination, source)
        return


    def tower_of_hanoi(self):
        n = self.n
        self.required_sequence(n, source = 1, destination = 3, helper = 2)

ht_tower = int(input().strip())
tower1 = Solution(ht_tower)
tower1.tower_of_hanoi()