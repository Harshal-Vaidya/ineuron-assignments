# l1=['x','y','z']
# l2=[]
# l3=[]
# for i in l1:
#     str=""
#     for j in range(4):
#         str+=i
#         l2.append(str)
        
# # print(l2)

list1 = [i * j for j in ['x', 'y', 'z'] for i in range(1, 5)]
print(list1)

list2 = [i * j for j in range(1, 5) for i in ['x', 'y', 'z']]
print(list2)

list3 = [[i + j] for j in [0, 1, 2] for i in range(2, 5)]
print(list3)

list4 = [[i + j for j in [0, 1, 2, 3]] for i in range(2, 6)]
print(list4)

l6=list3+list4
print(l6)

list5 = [(i,j) for j in [1, 2, 3] for i in [1, 2, 3]]
print(list5)



