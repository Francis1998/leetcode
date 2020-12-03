class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack1 = [] #descending stack
        mark = [0 for _ in range(len(T))]
        for i in range(len(T)):
            while stack1 and T[stack1[-1]]<T[i]: 
                mark[stack1[-1]] = i - stack1[-1]
                stack1.pop()
            stack1.append(i)                
        return mark