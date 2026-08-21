class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        
        def calculate_checksum(string):
            c = 0
            for letter in string:
                c += hash(letter)

            return c

        if len(s1) > len(s2):
            return False
        
        checksum = calculate_checksum(s1)

        print(checksum, s1)

        for i in range(0,len(s2)-len(s1)+1):
            print(calculate_checksum(s2[i:i+len(s1)]), s2[i:i+len(s1)])
            if calculate_checksum(s2[i:i+len(s1)]) == checksum:
                return True
        
        return False
