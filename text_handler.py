def get_key_from_line(line):
    key = ""
    #suchen nach dem index von dem ersten Buchstaben
    index = line.find("Sektion") + len("Sektion") + 1
    while line[index] != " ":
        key += line[index]
        index += 1
    return key


def update_value(value, line):
    value += line
    return value

def update_dict(book, key, value):
    if key == "":
        pass
    else:
        book[key] += value
        return book


def take_alt_path(line):
    number_backwards = ''
    number = ''
    for char in line[::-1]:
        if char == "." or char == '\n':
            pass
        elif char != ' ':
            number_backwards += str(char)
        else:
            break
    for char in number_backwards[::-1]:
        number += str(char)
    return number

def append_path(dict, key, path):
    dict['Sections'][key]['path'].append(take_alt_path(path))

def reset_value():
    value = ""
    return value




