from vehicles import Bike, Car
from decorators import ride_logger


@ride_logger
def book_ride(vehicle, distance):

    if distance < 0:
        raise ValueError("Distance cannot be negative")

    fare = vehicle.fare_calculation(distance)

    try:
        with open("ride_history.txt", "a") as file:
            file.write(f"Driver: {vehicle.driver_name}\n")
            file.write(f"Vehicle: {vehicle.vehicle_type}\n")
            file.write(f"Rating: {vehicle.rating}\n")
            file.write(f"Distance: {distance} km\n")
            file.write(f"Fare: Rs. {fare}\n")
            file.write("-------------------------\n")

    except OSError:
        print("Error writing ride history!")

        return False

    print(f"Driver: {vehicle.driver_name}")
    print(f"Vehicle: {vehicle.vehicle_type}")
    print(f"Distance: {distance} km")
    print(f"Fare: Rs. {fare}")

    return True


def main():

    try:
        vehicle_type = input("Enter Vehicle Type: ").lower()

        driver_name = input("Enter Driver Name: ")

        rating = float(input("Enter Rating: "))

        distance = float(input("Enter Distance: "))

        if vehicle_type == "bike":
            vehicle = Bike(driver_name, "Bike", rating)

        elif vehicle_type == "car":
            vehicle = Car(driver_name, "Car", rating)

        else:
            print("Invalid vehicle type!")
            return

        book_ride(vehicle, distance)

    except ValueError as e:
        print("Error:", e)

    except OSError:
        print("File operation error!")


if __name__ == "__main__":
    main()