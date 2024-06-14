
# keep track of previously computed values
memoization_dic = {}

# 
# This function finds all the possible combinations of
# coins that will pay for the cost
# 
#
def findAllCombinations(coins, cost, idx, currPath, paths):

    state_key = (cost, idx)

    if state_key in memoization_dic:
        return

    # base cases
    if currPath in paths:
        return

    if idx == (len(coins)):
        return
    
    if cost <= 0.000000001:
        return

    new_cost = cost - coins[idx]
    currPath.append(coins[idx])

    if new_cost <= 0.000000001:
        paths.append(currPath.copy())

    # include current coin
    findAllCombinations(coins, new_cost, idx+1, currPath, paths)
    
    currPath.pop()

    # don't include current coin
    findAllCombinations(coins, cost, idx+1, currPath, paths)

    memoization_dic[state_key] = True


#
# Returns a list of coins that retrieves the most optimal combination of
# coins to maximize the amount of coins you give away. Returns an empty list
# if the coins are insufficient
#  
# Takes in a list of coins in increasing order and the cost
#
def calculateMaxChange(coins, cost):
    currPath = []
    paths = []
    bestPath = []

    coins.sort(reverse = True)

    findAllCombinations(coins, cost, 0, currPath, paths)

    if len(paths) == 0:
        return bestPath

    bestPath = paths[0]
    print("ALL PATHS:" + str(paths))

    for path in paths:
        if len(path) > len(bestPath):
            bestPath = path

    memoization_dic.clear()

    return bestPath
