def ride_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result:
            print("Ride booked successfully!")

        return result

    return wrapper