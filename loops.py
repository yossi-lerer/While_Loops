# # part 1
# # step 1
# num = 1
# while num <=5:
#     print(num)
#     num += 1
# # step 2
# num_s = 10
# while num_s >= 0:
#     print(num_s)
#     num_s -= 1
# # step 3
# num_tot = 1
# total = 0
# while num_tot <= 10:
#     total += num_tot
#     num_tot += 1 
# print(total)
# # step 4
# items = [2, 4, 6, 8]
# item_i = 0
# while item_i < len(items):
#     if items[item_i] > 5:
#         print(items[item_i])
#         break
#     item_i += 1
# # step 5
# i_even = 0
# while i_even <= 10:
#     if i_even % 2 == 0:
#         print(i_even)
#     i_even += 1
# # step 6
# agents = ['Alpha', 'Bravo', 'Charlie']
# i = 0
# while i < len(agents):
#     print(agents[i])
#     i += 1
# step 7
scores = {'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
print(scores.items())
item = scores.items()
for x in item:
    for y in x:
        print(y)