class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} #hash_count -> [words that match]

        for word in strs: 
            hash_count = 0 
            for letter in word:
                hash_count += hash(letter)
            
            if hash_count in groups:
                groups[hash_count].append(word)
            else: 
                groups[hash_count] = [word]
        
        return list(groups.values())
