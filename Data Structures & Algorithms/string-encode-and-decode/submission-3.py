class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}\xff" + word
        print(encoded)
        return encoded 
    def decode(self, s: str) -> List[str]:
        decoded = []
        letters_left = 0 # reading word = x letters left
        counting = 1 # 1 if counting , 0 if not
        word = ""

        for char in s:
            
            if counting == 1:
                if char == "\xff":
                    if letters_left > 0: 
                        counting = 0 #end counting if \xff
                    else:
                        decoded.append("")
                else:
                    letters_left *= 10 
                    letters_left += int(char) #add to count
            else:
                word += char #add char to the word until letters_left = 0 
                letters_left -= 1 
                
                if letters_left == 0:
                    decoded.append(word)
                    counting = 1 #add word, start counting
                    word = ""
                
            
            print(f"char: {char}")
            print(decoded)
            print(letters_left)
            print(counting)
            print(word)
            print()

        return decoded
        
            
                



