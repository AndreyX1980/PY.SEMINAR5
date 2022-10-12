# программа-фильтр

file_result = """
абвер
кабве
крабв
кабво
"""
simbol = ('абв',)
 
for string in file_result.split('\n'):
    for i in simbol:
        string = string.replace(i, '')
    if string:
        print(string)