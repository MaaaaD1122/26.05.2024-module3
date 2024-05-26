def calculate_structure_sum(*args):
    total = 0
    for arg in args:
        if isinstance(arg, int):
            total += arg
        elif isinstance(arg, str):
            total += len(arg)
        elif isinstance(arg, tuple) or isinstance(arg, list):
            total += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            total += calculate_structure_sum(*arg.keys()) + calculate_structure_sum(*arg.values())
    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [(2, 'Urban', ('Urban2', 35))])
]
result = calculate_structure_sum(*data_structure)
print(result)

