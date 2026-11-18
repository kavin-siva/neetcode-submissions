class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair positions and speeds, then sort from closest to target to furthest
        cars = sorted(zip(position, speed), reverse=True)
        stack = []  # Stores arrival times of distinct fleets

        for pos, spd in cars:
            time = (target - pos) / spd
            # Only push if this car is slower than the fleet ahead (won't catch up)
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)

        