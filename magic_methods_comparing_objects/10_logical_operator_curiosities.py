my_list = [
    1,
    0.5,
    'a',
    [1, 2],
    {1},
    (1, 2),
    {'a': 1},

    0,
    .0,
    '',
    [],
    set(),
    (),
    {},
    None
]

for list_item in my_list:
    if list_item:
        print('if 1, list_item: ', list_item)
    if list_item is not None:
        print('if 2, list_item: ', list_item)
