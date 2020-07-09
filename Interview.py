def minimumCost(CostList, People):
    CostList = sorted(CostList)
    totalCost = 0
    for person in range(People - 1, 1, -2):
        if (person == 2):
            totalCost += CostList[2] + CostList[0]
        else:
            price_first = CostList[person] + CostList[0] + 2 * CostList[1]
            price_second = CostList[person] + CostList[person - 1] + 2 * CostList[0]
            totalCost += min(price_first, price_second)
    if (People == 1):
        totalCost += CostList[0]
    else:
        totalCost += CostList[1]
    return totalCost
TestCases = int(input("Enter the number of test cases"))
for testCases in range(TestCases):
    CostList = [int(cost) for cost in input("Enter the prices").split(",")]  # [30, 40, 60, 70]
    People = len(CostList)
    print("Total Minimum Cost is " , minimumCost(CostList, People))

