#source: zyBooks Class and instance object types
class Truck:
    # This method initializes the Truck attributes
    def __init__(self, truckLocation, departureTime, truckPackages, truckSpeed=18, miles=0.0):
        self.truckLocation = truckLocation
        self.departureTime = departureTime
        self.currentTime = departureTime
        self.truckPackages = truckPackages
        self.deliveredPackages = []
        self.truckSpeed = truckSpeed
        self.miles = miles

    # This method returns info about the truck in string format
    def __str__(self):
        return (
            #f"Truck Location: {self.truckLocation}\n"
            f"Departure Time: {self.departureTime}\n"
            f"Packages: {self.truckPackages}\n"
            #f"Delivered Packages: {self.deliveredPackages}\n"  # Include delivered packages
            f"Speed: {self.truckSpeed} mph\n"
            f"Miles Traveled: {self.miles:.2f} miles\n"
        )
