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
        if '0000' in deadends:
            return -1

        temp = {str((int(target[0]) + 1) % 10) + target[1:],
        str((int(target[0]) - 1) % 10) + target[1:],
        target[0] + str((int(target[1]) + 1) % 10) + target[2:],
        target[0] + str((int(target[1]) - 1) % 10) + target[2:],
        target[:2] + str((int(target[2]) + 1) % 10) + target[3:],
        target[:2] + str((int(target[2]) - 1) % 10) + target[3:],
        target[:3] + str((int(target[3]) + 1) % 10),
        target[:3] + str((int(target[3]) - 1) % 10)}

        if set(deadends) == temp:
            return -1

        min_turns = 400
        turns = 0
        queue = [(target, 0)]

        while queue and turns < min_turns:
            curr, turns = queue.pop(0)

            if curr == '0000':
                if turns < min_turns:
                    min_turns = turns
                return min_turns

            deadends.append(curr)
            if str((int(curr[0]) + 1) % 10) + curr[1:] not in deadends:
                queue.append((str((int(curr[0]) + 1) % 10) + curr[1:], turns + 1))
            if str((int(curr[0]) - 1) % 10) + curr[1:] not in deadends:
                queue.append((str((int(curr[0]) - 1) % 10) + curr[1:], turns + 1))
            if curr[0] + str((int(curr[1]) + 1) % 10) + curr[2:] not in deadends:
                queue.append((curr[0] + str((int(curr[1]) + 1) % 10) + curr[2:], turns + 1))
            if curr[0] + str((int(curr[1]) - 1) % 10) + curr[2:] not in deadends:
                queue.append((curr[0] + str((int(curr[1]) - 1) % 10) + curr[2:], turns + 1))
            if curr[:2] + str((int(curr[2]) + 1) % 10) + curr[3:] not in deadends:
                queue.append((curr[:2] + str((int(curr[2]) + 1) % 10) + curr[3], turns + 1))
            if curr[:2] + str((int(curr[2]) - 1) % 10) + curr[3:] not in deadends:
                queue.append((curr[:2] + str((int(curr[2]) - 1) % 10) + curr[3], turns + 1))
            if curr[:3] + str((int(curr[3]) + 1) % 10) not in deadends:
                queue.append((curr[:3] + str((int(curr[3]) + 1) % 10), turns + 1))
            if curr[:3] + str((int(curr[3]) - 1) % 10) not in deadends:
                queue.append((curr[:3] + str((int(curr[3]) - 1) % 10), turns + 1))

        print(deadends)
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

if __name__ == '__main__':
    main()
