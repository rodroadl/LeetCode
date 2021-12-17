''' https://leetcode.com/problems/open-the-lock/
    752. Open the Lock
    You have a lock in front of you with 4 circular wheels. 
    Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
    The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. 
    Each move consists of turning one wheel one slot.

    The lock initially starts at '0000', a string representing the state of the 4 wheels.

    You are given a list of deadends dead ends, meaning if the lock displays any of these codes, 
    the wheels of the lock will stop turning and you will be unable to open it.

    Given a target representing the value of the wheels that will unlock the lock, 
    return the minimum total number of turns required to open the lock, or -1 if it is impossible.'''

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        grid = []
        queue = [(int(target),0)]
        min_turns = 40000
        turns = 0
        target = int(target)

        if '0000' in deadends:
            return -1

        for i in range(len(deadends)):
            deadends[i] = int(deadends[i])

        for i in range(10000):
            if i in deadends:
                grid.append(0)
            else:
                grid.append(1)
        
        grid[target] = 0
        while queue and turns < min_turns:
            curr, turns = queue.pop(0)
            

            if curr == 0:
                if turns < min_turns:
                    min_turns = turns
            
            if grid[(curr // 10) * 10 + ((curr % 10) + 1) % 10] == 1:
                queue.append(((curr // 10) * 10 + ((curr % 10) + 1) % 10, turns + 1))
                grid[(curr // 10) * 10 + ((curr % 10) + 1) % 10] = 0
            if grid[(curr // 10) * 10 + ((curr % 10) - 1) % 10] == 1:
                queue.append(((curr // 10) * 10 + ((curr % 10) - 1) % 10, turns + 1))
                grid[(curr // 10) * 10 + ((curr % 10) - 1) % 10] = 0
            if grid[(curr // 100) * 100 + ((curr % 100) - (curr % 10) + 10) % 100 + curr % 10] == 1:
                queue.append(((curr // 100) * 100 + ((curr % 100) - ((curr % 100) % 10) + 10) % 100 + curr % 10, turns + 1))
                grid[(curr // 100) * 100 + ((curr % 100) - (curr % 10) + 10) % 100 + curr % 10] = 0
            if grid[(curr // 100) * 100 + ((curr % 100) - (curr % 10) - 10) % 100 + curr % 10] == 1:
                queue.append(((curr // 100) * 100 + ((curr % 100) - ((curr % 100) % 10) - 10) % 100 + curr % 10, turns + 1))
                grid[(curr // 100) * 100 + ((curr % 100) - (curr % 10) - 10) % 100 + curr % 10] = 0
            if grid[(curr // 1000) * 1000 + ((curr % 1000) - (curr % 100) + 100) % 1000 + curr % 100] == 1:
                queue.append(((curr // 1000) * 1000 + ((curr % 1000) - (curr % 100) + 100) % 1000 + curr % 100, turns + 1))
                grid[(curr // 1000) * 1000 + ((curr % 1000) - (curr % 100) + 100) % 1000 + curr % 100] = 0
            if grid[(curr // 1000) * 1000 + ((curr % 1000) - (curr % 100) - 100) % 1000 + curr % 100] == 1:
                queue.append(((curr // 1000) * 1000 + ((curr % 1000) - (curr % 100) - 100) % 1000 + curr % 100, turns + 1))
                grid[(curr // 1000) * 1000 + ((curr % 1000) - (curr % 100) - 100) % 1000 + curr % 100] = 0
            if grid[(curr // 1000 + 1) % 10 * 1000 + curr % 1000] == 1:
                queue.append(((curr // 1000 + 1) % 10 * 1000 + curr % 1000, turns + 1))
                grid[(curr // 1000 + 1) % 10 * 1000 + curr % 1000] = 0
            if grid[(curr // 1000 - 1) % 10 * 1000 + curr % 1000] == 1:
                queue.append(((curr // 1000 - 1) % 10 * 1000 + curr % 1000, turns + 1))
                grid[(curr // 1000 - 1) % 10 * 1000 + curr % 1000] = 0

        if min_turns == 40000:
            return -1
        else:
            return min_turns

def main():     
    sol = Solution()
    print(sol.openLock(['8888'], '0009'))
    print(sol.openLock(["0201","0101","0102","1212","2002"], '0202'))
    print(sol.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))
    print(sol.openLock(deadends = ["0000"], target = "8888"))
    print(sol.openLock(["1131","1303","3113","0132","1301","1303","2200","0232","0020","2223"],"3312"))
if __name__ == '__main__':
    main()
