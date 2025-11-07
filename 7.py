# Colletion -> Abstract Data Type -> Implementation Set
# Python -> list, tuple, dict, set 

def get_total_avg(x: int, y: int) -> tuple:
    total = x + y
    avg = total / 2
    return total, avg

x_tuple: tuple = (1, 2, 3)

x_list:list = [1, 2, 3]

x_dict: dict = {1:2, 3:4}

x_set:set = {1, 2, 3}

x_range:range = range(2)

x_list_int: list[int] = [1, 2, 3]
x_list_int = ["1", 2, 3]

x_dic_str_float: dict[str, float] = {"ki":2.0, "k2":3.0}
x_dic_str_float = {1:2.0}

x_set_bool: set[bool] = {True, False}
x_set_bool = {True, False}