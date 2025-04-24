

class GoogleGeocodeError(Exception):
    status_code = 500
    error = "Geocode API Error"
    pass

class DatabaseMutationError(Exception):
    status_code = 500
    pass


