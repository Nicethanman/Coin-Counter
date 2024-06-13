from maxChangeCalculator import calculateMaxChange


testSmall = [0.25, 0.10, 0.10, 0.05]
testSmall2 = [0.25, 0.05, 0.05, 0.05, 0.05, 0.05]
testMedium = [2, 1, 0.25, 0.25, 0.25, 0.10, 0.10, 0.05, 0.05, 0.05, 0.05, 0.05]

testNotExactAmount = [1, 0.25, 0.10, 0.10]
testNotEnoughAmount = [1, 0.25, 0.10, 0.10]

testComplex = [2, 1, 1, 0.25, 0.25, 0.25, 0.10, 0.10, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]

print(calculateMaxChange(testSmall, 0.25))
print("Best Path: " + str(calculateMaxChange(testSmall2, 0.25)))
print("Best Path: " + str(calculateMaxChange(testMedium, 1)))
print("Best Path: " + str(calculateMaxChange(testNotExactAmount, 1.30)))
print("Best Path: " + str(calculateMaxChange(testNotEnoughAmount, 1.50)))
print("Best Path: " + str(calculateMaxChange(testComplex, 2)))
