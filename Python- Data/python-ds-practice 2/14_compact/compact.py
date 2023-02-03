def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """


result = []
for my_list in lst:
    if my_list:
        result.append(my_list)
        # return result

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
