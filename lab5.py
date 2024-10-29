import data
from data import Time
from data import Point
import math


# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
#function time_add takes two Time arguments and returns a new Time object that is the sum of the 2 input objects
# - this new object needs the number of seconds to be below 60

def time_add(time_1:Time, time_2:Time)->Time:
    time_1_total_secs = time_1.second + time_1.minute * 60 + time_1.hour * 60**2
    time_2_total_secs = time_2.second + time_2.minute * 60 + time_2.hour * 60**2
    total_secs = time_1_total_secs + time_2_total_secs
    new_hour = (total_secs//60**2) % 24
    new_minute = (total_secs % 3600) // 60
    new_second = total_secs % 60
    return Time(new_hour, new_minute, new_second)


# Part 4
#function is_descending takes one parameter of type list[float] and returns the Boolean True if elements in list are
# in descending

def is_descending(list_one:list[float])->bool:
    new_list = []
    for i in range(len(list_one)):
        new_list.append(list_one[i])

    for i in range(len(new_list) - 1):
        for j in range(len(new_list) - 1 - i):
            if new_list[j] < new_list[j + 1]:
                temp = new_list[j]
                new_list[j] = new_list[j + 1]
                new_list[j + 1] = temp
    if new_list == list_one:
        return True
    else:
        return False

# Part 5
#function largest_between takes three parameters: one is of type list[int], one names lower and one named
# upper(these two are ints to represent indexes). It returns the index of the largest value in the input list that
# appears between lower and upper. lower and upper are inclusive.If lower>upper then function should return None.
# If the indexes provided are out of range(negative), the function will also return None.

def largest_between(list_one:list[int], upper:int, lower:int):
    if lower > upper:
        return None
    if upper <= 0 or lower <= 0:
        return None

    largest_idx = lower
    for i in range(lower, upper + 1):
        if list_one[i] > list_one[largest_idx]:
            largest_idx = i
    return largest_idx

# Part 6
#function furthest_from_origin takes one parameter of type list[Point] and returns the index of the point that is
# furthest away from the origin(0,0). If the list is empty then the return will be None
def furthest_from_origin(list_one:list[Point]):
    distance_list = []
    if not list_one:
        return None
    else:
        for i in range(len(list_one)):
            distance_from_origin = math.sqrt((0 - list_one[i].x)**2 + (0 - list_one[i].y)**2)
            distance_from_origin = round(distance_from_origin)
            distance_list.append(distance_from_origin)
        furthest_idx = 0
        for i in range(len(distance_list)):
            if distance_list[i] > distance_list[furthest_idx]:
                furthest_idx = i
    return furthest_idx

