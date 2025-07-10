# %% word split function


def get_num_words(book_contents):
    book_split = book_contents.split()
    return len(book_split)


# %% character count function


def get_num_chars(book_contents):
    # converting contents to lower
    book_lower = book_contents.lower()

    # creating empty dictionary
    character_dictionary = {}
    
    # looping through count
    for c in book_lower:
        if c in character_dictionary:
            character_dictionary[c] += 1
        else:
            character_dictionary[c] = 1

    # returning
    return character_dictionary


# %% sorting function


# sort dictionary
def sort_on(items):
    return items["num"]


# %% splitting the dictionary


# splitting dictionary
def dict_split(character_dictionary):
    # list of dictionaries
    dict_list = [{"char":key, "num":value} for key, value in character_dictionary.items()]

    # sorting list by num
    dict_list.sort(key=sort_on, reverse=True)

    # returning
    return dict_list