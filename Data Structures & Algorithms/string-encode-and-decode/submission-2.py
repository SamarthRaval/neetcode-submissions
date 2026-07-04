class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        print(s)
        output = []
        i = 0
        while i < len(s):
            j = i+1
            while s[j] != "#":
                j += 1
                
            length = int(s[i:j])
            output.append(s[j+1:j+1+length])

            i = j + 1 + length

        return output