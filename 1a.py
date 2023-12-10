with open("input") as f:
    sum = 0
    for line in f:
       nums = [c for c in line if c.isdigit()]
       sum += int(nums[0] + nums[-1])
    print(sum)