class Solution:
    def car_fueling(self, total_dist, max_dist, gas_station_pos):
        curr_pos, last_refill_pos = 0, 0
        gas_station_pos = [0] + gas_station_pos
        gas_station_pos.append(total_dist)
        size = len(gas_station_pos)
        res = 0

        while curr_pos < size - 1:
            last_refill_pos = curr_pos
            while curr_pos < size - 1 and gas_station_pos[curr_pos + 1] - gas_station_pos[last_refill_pos] <= max_dist:
                curr_pos += 1
            if last_refill_pos == curr_pos:
                return -1
            elif curr_pos < size - 1:
                res += 1
        
        return res




        
        return res

total_dist = int(input().strip())
max_dist = int(input().strip())
gas_station_pos = [int(i) for i in input().split()]
sol = Solution()
print(sol.car_fueling(total_dist, max_dist, gas_station_pos))
    
