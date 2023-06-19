class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0  # Initialize the highest altitude to 0
        current_altitude = 0  # Initialize the current altitude to 0

        for net_gain in gain:
            current_altitude += net_gain  # Update the current altitude
            highest_altitude = max(highest_altitude, current_altitude)  # Update the highest altitude if necessary

        return highest_altitude
