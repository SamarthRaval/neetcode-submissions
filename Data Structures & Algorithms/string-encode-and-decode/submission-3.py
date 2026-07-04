class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string

        return output

    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            string = str(s[j+1: j+1+length])

            output.append(string)

            i = j+1+length

        return output
