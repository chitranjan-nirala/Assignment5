# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list


original_list = [i for i in range(1,11)]
print("original_list :{}" .format(original_list))
Extracted_list = original_list[0:5]
print("Extracted first five elements:{}".format(Extracted_list))
print("Reversed extracted elements:{}".format(Extracted_list[::-1]))