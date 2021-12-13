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
        curr = '0000'
        min_turns = 40000
        turns = 0
        self.bfs(curr, turns, min_turns, target)
        if min_turns != 40000:
            return min_turns
        else:
            return -1
    
    def bfs(self, curr, turns, min_turns, target):
        if curr == target:
            return turns
        if turns > min_turns:
            return 40000
        else:
            self.bfs(str((int(curr[0]) + 1) % 10) + curr[1:], turns + 1, min_turns, target)
            self.bfs(str((int(curr[0]) - 1) % 10) + curr[1:], turns + 1, min_turns, target)
            self.bfs(curr[0] + str((int(curr[1]) + 1) % 10) + curr[2:], turns + 1, min_turns, target)
            self.bfs(curr[0] + str((int(curr[1]) - 1) % 10) + curr[2:], turns + 1, min_turns, target)
            self.bfs(curr[:2] + str((int(curr[2]) + 1) % 10) + curr[3:], turns + 1, min_turns, target)
            self.bfs(curr[:2] + str((int(curr[2]) - 1) % 10) + curr[3:], turns + 1, min_turns, target)
            self.bfs(curr[:3] + str((int(curr[3]) + 1) % 10), turns + 1, min_turns, target)
            self.bfs(curr[:3] + str((int(curr[3]) - 1) % 10), turns + 1, min_turns, target)
            


def main():
    sol = Solution()
    print(sol.openLock(['9999'], '1000'))
    # print(sol.openLock(["0201","0101","0102","1212","2002"], '0202'))
    

if __name__ == '__main__':
    main()