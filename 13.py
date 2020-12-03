class Solution:
    def maxPoints(self, points):
        res = 0
        if not points:
            return res
        for i in range(len(points)):
            dic = {}
            same = 0
            curMax = 0
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    same += 1
                    continue
                if (points[i][0] - points[j][0]) == 0:
                    rate = float('inf')
                else:
                    rate = (points[i][1] - points[j][1]) * 1000 / (points[i][0] - points[j][0]) * 1000
                dic[rate] = dic.get(rate, 0) + 1
                curMax = max(curMax, dic[rate])
            res = max(res, curMax+same+1)
        return res