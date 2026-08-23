class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        hmap = {s[0]: 0}

        i = 0
        j = 1

        while j < len(s):

            if s[j] in hmap:
                duplicate_index = hmap[s[j]]

                while i <= duplicate_index:
                    del hmap[s[i]]
                    i += 1

            hmap[s[j]] = j

            maxCount = max(maxCount, j - i + 1)

            j += 1

        return maxCount
