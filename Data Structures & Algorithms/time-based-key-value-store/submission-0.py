class TimeMap:

    def __init__(self):
        self.hmap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hmap.get(key,[])
        l = 0
        r = len(arr)-1
        result = None

        if arr == [] or timestamp < arr[0][1]:
            return ""

        while l<=r:
            i = (l+r)//2
            if arr[i][1] > timestamp:
                r = i - 1
            elif arr[i][1] <= timestamp:
                l = i + 1
                result = i

        return arr[result][0]