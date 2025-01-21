

def get_keys(sample_dict, keys=[]):
    """
        Recursively retrieves all keys from a nested dictionary.
    """
    for key, value in sample_dict.items():
        keys.append(key.replace(' ', '').strip())
        if isinstance(value, dict):
            get_keys(value, keys)
    return keys


def search_keys(key_to_search, filename, sample_dict, keys=[]):
    """
        Recursively searches all keys from a nested dictionary.
    """
    for key, value in sample_dict.items():
        keys.append(key.replace(' ', '').strip())
        if key_to_search in key:
            print ("Found in file - {}".format(filename))
        if isinstance(value, dict):
            get_keys(value, keys)
    return keys
