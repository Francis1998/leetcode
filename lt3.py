# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 示例 4:
# 输入: s = ""
# 输出: 0
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # te1232
        lens = len(s)
        if lens ==0:
            return 0
        lookup = set() #每个只能有一次适合set
        left_win = 0
        max_size = 0
        cur_size = 0
        for i in range(lens):
            cur_size +=1
            while s[i] in lookup:
                lookup.remove(s[left_win])
                cur_size-=1
                left_win+=1
            if s[i] not in lookup:
                lookup.add(s[i])
            max_size = max(max_size,cur_size)
        return max_size



