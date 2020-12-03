class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        hour_seen = set()
        minute_seen = set()
        def backtrace(num:int,hour:int,minute:int,which:int)->None:
            if hour > 11 or minute > 59:
                return
            if num ==0:
                res.append(f'{hour}:{minute:02}')
                return
            for h in range(which,4):
                if h not in hour_seen:
                    hour_seen.add(h)
                    backtrace(num-1,hour+int(pow(2,h)),minute,h+1)
                    hour_seen.remove(h)
            for m in range(max(which,4),10):
                if m not in minute_seen:
                    minute_seen.add(m)
                    backtrace(num-1,hour,minute+int(pow(2,m-4)),m+1)
                    minute_seen.remove(m)
        backtrace(num,0,0,0)
        return res
