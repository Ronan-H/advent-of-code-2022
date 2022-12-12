
def get_visualisation(nums, space='.', solid='*'):
    return '\n' + '\n'.join([
        space * (r[0] - 1) + solid * (r[1] - r[0] + 1) for r in nums
    ])


with open('./input') as file:
    count = 0
    for line in file:
        line = line.rstrip()
        nums = [[int(y) for y in x.split('-')] for x in line.split(',')]
        overlaps = nums[1][0] <= nums[0][0] <= nums[1][1] or nums[1][0] <= nums[0][1] <= nums[1][1] \
                or nums[0][0] <= nums[1][0] <= nums[0][1] or nums[0][0] <= nums[1][1] <= nums[0][1]
        # print(f'Range: {nums} - Overlaps: {overlaps} - Visualised: {get_visualisation(nums)}')
        if overlaps:
            count += 1
    print(count)
