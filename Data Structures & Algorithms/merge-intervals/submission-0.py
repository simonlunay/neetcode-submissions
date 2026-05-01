class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]
        for start, end in intervals:
            oldEnd = output[-1][1]

            if start <= oldEnd:
                print(oldEnd)
                print(start)
                output[-1][1] = max(end, oldEnd)
            else:
                output.append([start, end])
        return output

