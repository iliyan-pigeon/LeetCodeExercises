# Solution 1
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        total_tank = 0
        current_tank = 0
        start_index = 0

        for i in range(n):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                start_index = i + 1
                current_tank = 0

        return start_index if total_tank >= 0 else -1


# Solution 2
class Solution(object):
    def canCompleteCircuit(gas, cost):
        result = -1
        gas_tank = 0
        start_index = 0
        full_circle = False

        while start_index < len(gas) and full_circle is not True:

            for i in range(len(gas)):
                gas_tank += gas[0]
                gas_tank -= cost[0]
                gas.append(gas.pop(0))
                cost.append(cost.pop(0))

                if gas_tank < 0:
                    gas_tank = 0
                    break
                elif i == len(gas) - 1:
                    full_circle = True

            if full_circle is not True:
                start_index += 1

        if full_circle:
            result = start_index

        return result
