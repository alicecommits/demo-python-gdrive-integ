JONS_DB = [{
      "name": "Jon",
      "price": 123456789,
      "is_cute": True,
      "id": 1
    },
    {
      "name": "Sarah",
      "price": 9999999999,
      "is_cute": True,
        "id": 4
    },
    {
      "name": "Alice",
      "price": 12345,
      "is_cute": True,
      "id": 99
    }]

def find_index_by_id(array, target_id):
    """
    Find the index of an element in an array by its ID.
    
    Args:
        array (list): List of dictionaries, each containing an 'id' key
        target_id: The ID to search for
    
    Returns:
        int: Index of the element with matching ID, or -1 if not found
    """
    for index, element in enumerate(array):
        if element.get('id') == target_id:
            return index
    return -1