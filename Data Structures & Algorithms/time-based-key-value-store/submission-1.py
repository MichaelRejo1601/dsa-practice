"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.

void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.

String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

stores timestamp (maximum timestamp)

maximum timestamp

returns value with the largest timestamp_prev (work backwards and pick first)
returns "" if nothing

1 <= key.length, value.length <= 100 small amount
key and value only include lowercase English letters and digits.
0 <= timestamp <= 10^7 large timestamps
All the timestamps of set are strictly increasing. timestamps are increasing as they are added

At most 2 * 10^5 calls will be made to set and get. lots of calls, needs to low time

hmap = {
key: [(timestamp, value), (timestamp+1, value)]
}

minheeap
[lowest time, largest times at the end, and we can simply append the items to the end of the heap because we know they are the largest]

"""

class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.hmap[key]
        min = 0
        max = len(lst)-1
        
        if len(lst) == 0:
            return ""
        if lst[0][0] > timestamp:
            return "" 
        while min < max:
            i = (min + max + 1)//2
            if timestamp >= lst[i][0]:
                min = i
            else:
                max = i - 1
        
        return lst[min][1]
