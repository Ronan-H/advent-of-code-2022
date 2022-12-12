
def get_visualisation(nums, space='.', solid='*'):
    return '\n' + '\n'.join([
        space * (r[0] - 1) + solid * (r[1] - r[0] + 1) for r in nums
    ])


with open('./input') as file:
    count = 0
    for line in file:
        line = line.rstrip()
        nums = [[int(y) for y in x.split('-')] for x in line.split(',')]
        a_in_b = nums[0][0] >= nums[1][0] and nums[0][1] <= nums[1][1]
        b_in_a = nums[1][0] >= nums[0][0] and nums[1][1] <= nums[0][1]
        fully_contains = a_in_b or b_in_a
        # print(f'Range: {nums} - Contains: {fully_contains} - Visualised: {get_visualisation(nums)}')
        if fully_contains:
            count += 1
    print(count)
