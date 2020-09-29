import random
import time
start_time = time.time()
start_number = 0
end_number = 10000000
# # start_number = int(input('put the start number: '))
# # end_number = int(input('put the end number: '))
# my_list = list(range(start_number, end_number, 2))
# #print(my_list)
# start_numbers_sum = sum(my_list)
# num = random.randint((start_number + 1), (len(my_list)-1))
# my_list.pop(num)
# #print(my_list)
# end_num_sum = sum(my_list)
# print(f'The lost number is: {start_numbers_sum - end_num_sum}')
# print("--- %s seconds ---" % (time.time() - start_time))

start_number = int(input('put the start number: '))
end_number = int(input('put the end number: '))
start_step = int(input('put the step: '))
start_list = list(range(start_number, end_number, start_step))
print(start_list)
print(len(start_list))
num = random.randint(1, (len(start_list) - 1))
start_list.pop(num)
print(start_list)

if ((start_list[1])-(start_list[0])) == ((start_list[2])-(start_list[1])):
    step = ((start_list[1])-(start_list[0]))
    print(f'step: {step}')
elif ((start_list[-1])-(start_list[-2])) == ((start_list[-2])-(start_list[-3])):
    step = ((start_list[-1]) - (start_list[-2]))
    print(f'step: {step}')

new_full_list = list(range((start_list[0]), (start_list[-1]+1), step))
print(new_full_list)
