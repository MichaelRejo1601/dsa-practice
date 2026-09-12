# n cars traveling to the same destination on a high

# you are given two int array position and speed of same length 
# position of speed of the ith car

# desination is a t target miles


# a car cannot pass the car ahead of it, it can onyl drive up to another car and then drive at the same speed as it 

# a car fleet is a non empty set of cars driving at the same position and same speed a single car is also considered a fleet

# if a car catches up to the fleet the moment the fleet reaches the destination, it is considered part of the fleet

#return the number of different car fleets that will arrive at the destination

# number of cars is medium 
# target is medium
# speed is medium

# speed is never 0 

# speed can be greater than target


#Input: target = 10, position = [1,4], speed = [3,2]

# time to destination < time of next to destination, then it is part of the fleet 

# sort the array first 

# go backwards through it





class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(key=lambda car: -car[0])
        counter = 0
        last_fleet_time_to_arrival = 0

        for car in cars:
            time_to_arrive = (target-car[0])/car[1]
            if time_to_arrive > last_fleet_time_to_arrival:
                counter += 1 
                last_fleet_time_to_arrival = time_to_arrive

        return counter
