class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, countT = dict(), dict()
        countT = Counter(t)
        have, need = 0, len(countT)
        left, right = 0, 0
        result = [-1, -1]
        resultLength = float("inf")

        for right in range(len(s)): #O(N)
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1

            while have == need: #O(M)
                if right - left + 1 < resultLength:
                    resultLength = right - left + 1
                    result = [left, right]

                window[s[left]] -= 1

                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

        l, r = result
        return s[l:r+1] if resultLength else ""

        # O(N+M) -> Time complexity
        # O(K) -> Space Complexity
