###
def reverse(nums):

    start_index = 0 
    end_index = len(nums) - 1

    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index],nums[start_index]
        start_index += 1 
        end_index -= 1

    return nums

def reverse_string(data):
    data = list(data)

    start_index = 0 
    end_index = len(data) - 1 

    while end_index>start_index:
        data[start_index],data[end_index] = data[end_index],data[start_index]
        start_index += 1
        end_index -= 1
    
    return ''.join(data)
    


if __name__ == '__main__':
    print("this my proof")
    print(reverse([1,2,3,4]))
