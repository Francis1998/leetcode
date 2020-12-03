class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        mem_dict = {}
        for word in words:
            mem_dict[word] = mem_dict.get(word, 0) + 1
        num_of_words = len(words)
        len_of_word = len(words[0])
        res = []
        for i in range(len(s) - num_of_words * len_of_word + 1):
            temp = mem_dict.copy()
            flag = 1
            for j in range(num_of_words):
                word = s[i + j * len_of_word:i + (j + 1) * len_of_word]
                if word not in temp:
                    flag = 0
                    break
                temp[word] -= 1
            if flag and not any(list(temp.values())):
                res.append(i)
        return res


print