def two_sum(nums, target):
    ### initiation
    ref = dict({})
    result = []
    new_target = target

    for i in range(len(nums)):
        ref.update({i:nums[i]})

    new_ref = ref.copy()

    ###
    for key in ref.keys():
        new_target -= new_ref.get(key)
        result.append(key)
        new_ref.pop(key)
        if new_target in new_ref.values():
            result.append(list(new_ref.keys())[list(new_ref.values()).index(new_target)])
            break
        else:
            new_target = target
            new_ref = ref.copy()
            result = []
    result.sort()
    return result

def test():
    # print(two_sum([2,7,11,15], 9))
    # print(two_sum([3,2,4], 6))
    # print(two_sum([3,3], 6))
    # print(two_sum([0,4,3,0], 0))
    # print(two_sum([-3, 4, 3, 90], 0))
    print(two_sum([-1,-2,-3,-4,-5], -8))
if __name__ == '__main__':
    test()
