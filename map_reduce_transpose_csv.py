"""
Map and reduce functions aiming to transpose a csv file
For this work we assume that the csv file has been splitted into the different 
lines and that each line is short enough to be handled by a single map node
"""

def map(key, value):
    '''
    Return a list of (new_key, new_value) as a dictionary 
    with new_value as being a tuple containing the value of a cell in the csv line
    and its new column index, and new_key as being the new line index of the cell

    @type value: string
    @param value: a line in the csv
    @type key: integer
    @param key: initial index of the line

    @rtype: dictionary
    @return: transposed line indexes as new key, and transposed column index along with value of cell as new value
    '''
    dict_output = dict()
    # We assume that the csv is in a comma separated format
    tokens = value.split(",")
    for i in range(0, len(tokens)):
        dict_output[i] = (key, tokens[i])
    
    return dict_output
    
dict_output = map(0, "Garry, 22, ECE Paris, SI, Big Data & Analytics")
print(dict_output)


def reduce(key, list_of_values):
    '''
    Return a list of (new_key, new_value) with new_value as being the value of a cell in the csv line
    and new_key as being the transposed coordinates of the cell (new_line_index, new_column_index)

    @type list_of_values: list of tuples
    @param list_of_values: each tuple in the list contain the cell value and its new column index
    @type key: integer
    @param key: new index of the line

    @rtype: list
    @return: transposed line (vector)
    '''
    reduced_list = []
    intermediate_dict = dict()
    for value in list_of_values:
        intermediate_dict[key, value[0]] = value[1]
    
    reduced_list = sorted(intermediate_dict.items())
    return reduced_list
    
reduced_list = reduce(0, [(1, 'Rick'), (0, 'Morty'), (2, 'NoobNoob')])
print(reduced_list)