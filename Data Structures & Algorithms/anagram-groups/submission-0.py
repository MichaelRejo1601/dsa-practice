class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {} 
        for string in strs:
            hash_count = 0
            for letter in string: 
                hash_count += hash(letter)
            if hash_count in hmap:
                hmap[hash_count].append(string) 
            else: 
                hmap[hash_count] = [string] 
        return list(hmap.values())