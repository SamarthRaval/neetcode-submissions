import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        deque = collections.deque()
        deque.append((beginWord, 1))
        seen = set(wordList)

        while deque:
            for _ in range(len(deque)):
                word, level = deque.popleft()

                if word == endWord:
                    return level

                for i in range(len(word)):
                    for ch in list(string.ascii_lowercase):
                        if ch != word[i]:
                            new_word = word[:i]+ ch + word[i+1:]
                            if new_word in seen:
                                seen.remove(new_word)
                                deque.append((new_word, level+1))

        return 0
