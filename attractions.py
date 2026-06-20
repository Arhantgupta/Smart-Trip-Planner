from destinations import destinations

def get_attractions(city):

    if city in destinations:

        return destinations[city]

    return []