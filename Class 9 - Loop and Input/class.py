# # sys.argv is only supported on abc.py file type
# # 
# import sys

# print("line 1")
# print("line 2")
# print(type(sys.argv))
# if sys.argv == '-g' :
#     print('I will install this package globally')
# print(sys.argv) # iterative data type list[str] 0 =

import sys

# Print the script name
print("Script name:", sys.argv[0])

# Print the command-line arguments
if len(sys.argv) > 1:
    print("Command-line arguments:")
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"Argument {i}: {arg}")
                                                                