

# can convert to a list then pop off each item of the list
# this is equivalent to a stack
def reverse_string(in_str):
    in_list = [char for char in in_str]
    len_in_list = len(in_list)
    return "".join([in_list.pop() for i in range(0, len_in_list)])

def reverse_string2(in_str):
    lenght_str = len(in_str)
    return "".join([in_str[i] for i in range(lenght_str -1, -1, -1)])

