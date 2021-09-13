from itertools import combinations
# Determine start time
import time
start = time.time()

# Data Set 1:
items = (
    ("Item 1", 1, 1), ("Item 2", 1, 2), ("Item 3", 1, 3), ("Item 4", 1, 4), ("Item 5", 1, 5)
    )
cap = 4
#
# # Data Set 2:
# items = (
#     ("Item 1", 2, 5), ("Item 2", 2, 5), ("Item 3", 2, 5), ("Item 4", 2, 5), ("Item 5", 2, 5), ("Item 6", 2, 5), ("Item 7", 2, 5), ("Item 8", 2, 5), ("Item 9", 3, 6),
#     )
# cap = 17
#
# # Data Set 3:
# items = (
#     ("Item 1", 23, 92), ("Item 2", 31, 57), ("Item 3", 29, 49), ("Item 4", 44, 68), ("Item 5", 53, 60), ("Item 6", 38, 43), ("Item 7", 63, 67), ("Item 8", 85, 84), ("Item 9", 89, 87), ("Item 10", 82, 72),
#     )
# cap = 165
#
# # Data Set 4:
# items = (
#     ("Item 1", 12, 24), ("Item 2", 7, 13), ("Item 3", 11, 23), ("Item 4", 8, 15), ("Item 5", 9, 16),
#     )
# cap = 26
#
# # Data Set 5:
# items = (
#     ("Item 1", 56, 50), ("Item 2", 59, 50), ("Item 3", 80, 64), ("Item 4", 64, 46), ("Item 5", 75, 50), ("Item 6", 17, 5),
#     )
# cap = 190
#
# # Data Set 6:
# items = (
#     ("Item 1", 31, 70), ("Item 2", 10, 20), ("Item 3", 20, 39), ("Item 4", 19, 37), ("Item 5", 4, 7), ("Item 6", 3, 5), ("Item 7", 6, 10),
#     )
# cap = 50
#
# # Data Set 7:
# items = (
#     ("Item 1", 25, 350), ("Item 2", 35, 400), ("Item 3", 45, 450), ("Item 4", 5, 20), ("Item 5", 25, 70), ("Item 6", 3, 8), ("Item 7", 2, 5), ("Item 8", 2, 5),
#     )
# cap = 104
#
# # Data Set 8:
# items = (
#     ("Item 1", 41, 442), ("Item 2", 50, 525), ("Item 3", 49, 511), ("Item 4", 59, 593), ("Item 5", 55, 546), ("Item 6", 57, 564), ("Item 7", 60, 617),
#     )
# cap = 170

# Data Set 9:
# items = (
#     ("Item 1", 70, 135), ("Item 2", 73, 139), ("Item 3", 77, 149), ("Item 4", 80, 150), ("Item 5", 82, 156), ("Item 6", 87, 163), ("Item 7", 90, 173), ("Item 8", 94, 184), ("Item 9", 98, 192), ("Item 10", 106, 201), ("Item 11", 110, 210), ("Item 12", 113, 214), ("Item 13", 115, 221), ("Item 14", 118, 229), ("Item 15", 120, 240),
#     )
# cap = 750

# Data Set 10:
# items = (
#     ("Item 1", 382745, 825594), ("Item 2", 799601, 1677009), ("Item 3", 909247, 1676628), ("Item 4", 729069, 1523970), ("Item 5", 467902, 943972), ("Item 6", 44328, 97426), ("Item 7", 34610, 69666), ("Item 8", 698150, 1296457), ("Item 9", 823460, 1679693), ("Item 10", 903959, 1902996), ("Item 11", 853665, 1844992), ("Item 12", 551830, 1049289), ("Item 13", 610856, 1252836), ("Item 14", 670702, 1319836), ("Item 15", 488960, 953277), ("Item 16", 951111, 2067538), ("Item 17", 323046, 675367), ("Item 18", 446298, 853655), ("Item 19", 931161, 1826027), ("Item 20", 31385, 65731), ("Item 21", 496951, 901489), ("Item 22", 264724, 577243), ("Item 23", 224916, 466257), ("Item 24", 169684, 369261),
#     )
# cap = 6404180


from operator import itemgetter


def knapsack(items,cap):
    # Calculate the total value and check feasibility of a combination of items.
    maxindex = temp = []
    # items = sorted(items, key=itemgetter(2))
    it, wt, val = [list(item) for item in zip(*items)]
    K = [[0 for x in range(cap + 1)] for x in range(len(val) + 1)]
    print(wt,'\n',val)
    for i in range(1,len(val)+1):
        temp = []
        for w in range(cap+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            if wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],K[i-1][w])
                temp.append(val[i-1])
            else:
                K[i][w] = K[i-1][w]
        # print(temp)
    # prev=0
    # for i in K[len(items)][1:]:
    #     if i == 0:
    #         prev = 0
    #         continue
    #     else:
    #         print(it_l[val_l.index(i-prev)])
    #         prev = i
    # print(K)
    print(K[len(items)][cap])
    # return K[len(items)]

print(knapsack(items,cap))

# for x in range(cap+1):
#     print(x)
#
# for x in range(len(items)+1):
#     print(x)

# from operator import itemgetter
# items = sorted(items, key=itemgetter(2))
# it, wt, val = [list(item) for item in zip(*items)]
# print(val)


# Determine ending time
end = time.time()

# Print total time.
print("For a total time in seconds of ")
print(end - start)