class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        def is_alphanum(ch):
            return ord('a') <= ord(ch) <= ord('z') or ord('0') <= ord(ch) <= ord('9')

        ss = s.lower()
        length = len(ss)

        start = 0
        end = length - 1    
        
        while start < end:
            if not is_alphanum(ss[start]) and is_alphanum(ss[end]):
                start += 1
            elif is_alphanum(ss[start]) and not is_alphanum(ss[end]):
                end -= 1
            elif not is_alphanum(ss[start]) and not is_alphanum(ss[end]):
                start += 1
                end -= 1
            else:
                if ss[start] == ss[end]:
                    start += 1
                    end -= 1
                else:
                    return False

        return True