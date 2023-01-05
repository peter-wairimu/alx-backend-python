#!/usr/bin/env python3
'''
Augment the following code with the correct duck-typed annotations:
'''


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Code anotated
    '''
    if lst:
        return lst[0]
    else:
        return None
