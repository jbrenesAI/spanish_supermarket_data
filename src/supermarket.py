

class Supermarket:
    def __init__(self, supermarket_element: dict):
        self.name = supermarket_element.get("name")
        self.base_url = supermarket_element.get("base_url")
        self.available_segments = supermarket_element.get("available_segments")