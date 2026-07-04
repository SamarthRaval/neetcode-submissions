class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        #s->  5#Hello5#World

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            output.append(s[j+1:j+1+length])
            i = j+1+length

        return output
