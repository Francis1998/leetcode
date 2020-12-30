# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
# 示例 1:
# 输入: "()"
# 输出: true
# 示例 2:
# 输入: "()[]{}"
# 输出: true
# 示例 3:
# 输入: "(]"
# 输出: false
# 示例 4:
# 输入: "([)]"
# 输出: false
# 示例 5:
# 输入: "{[]}"
# 输出: true
class Solution:
    def isValid(self, s: str) -> bool:
        list_left = ['{','[','(']
        list_right = ['}',']',')']
        stack = []
        for i in s:
            if i in list_left:
                stack.append(i)
            if i in list_right:
                if len(stack)==0 or list_left.index(stack[-1]) != list_right.index(i):
                    return False
                else:
                    stack.pop(-1)
        if len(stack)!=0:
            return False
        return True

