class Solution:
    # Time Complexity - O(m) - where m is the number of logs
    # Space Complexity - O(n) - where n is the number of processes
    def exclusiveTime(self, n: int, logs):
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn, typ, time = log.split(":")
            fn, time = int(fn), int(time)

            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fn)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return ans