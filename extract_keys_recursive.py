

def get_keys(sample_dict, keys=[]):
    """
        Recursively retrieves all keys from a nested dictionary.
    """
    for key, value in sample_dict.items():
        keys.append(key.replace(' ', '').strip())
        if isinstance(value, dict):
            get_keys(value, keys)
    return keys

