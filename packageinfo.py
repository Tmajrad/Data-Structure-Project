from datetime import timedelta

class PackageInfo:
    # Init method initializes a package with its attributes
    def __init__(self, ID, address, city, state, zip, time_deadline, weight, note):
        self.ID = ID
        self.address = address
        self.original_address = address  # Store the original address
        self.city = city
        self.state = state
        self.zip = zip
        self.original_zip = zip  # Store the original zip code
        self.time_deadline = time_deadline
        self.weight = weight
        self.note = note
        self.departure_time = None
        self.delivery_time = None
        self.status = "at the Hub"

    # Str method returns string information of a package
    def __str__(self):
        return (
            f"ID: {self.ID}\n"
            f"Address: {self.address}, {self.city}, {self.state}, {self.zip}\n"
            f"Weight: {self.weight} kg\n"
            f"Note: {self.note}\n"
            f"Departure Time: {self.departure_time}\n"
            f"Deadline: {self.time_deadline}\n"
            f"Delivery Time: {self.delivery_time}\n"
            f"Status: {self.status}\n"
        )
    #source: zyBooks String formatting

    # This method calculates the status of the package based off the time input
    # and departure/delivery time
    def package_Status(self, time_input):
        if self.ID == 9:
            if time_input < timedelta(hours=10, minutes=20):
                self.address = self.original_address
                self.zip = self.original_zip
            else:
                self.address = "410 S. State St."
                self.zip = "84111"

        if self.departure_time is None or self.delivery_time is None:
            self.status = "At the Hub"
        elif time_input < self.departure_time:
            self.status = "At the Hub"
        elif time_input < self.delivery_time:
            self.status = "En Route"
        else:
            self.status = "Delivered"
