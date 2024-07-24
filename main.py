import csv
from datetime import timedelta
from hashtable import HashTable
from packageinfo import PackageInfo
from truck import Truck

# Loading the address.csv file
with open("address.csv") as address_file:
    address_reader = csv.reader(address_file)
    address_list = []
    for row in address_reader:
        address_list.append(row)

# Loading the distance.csv file
with open("distance.csv") as distance_file:
    distance_reader = csv.reader(distance_file)
    distance_list = []
    for row in distance_reader:
        distance_list.append(row)

# Function to find the address ID by going through the address_list
def find_address_id(next_address):
    for row in address_list:
        if next_address in row[2]:
            return int(row[0])
    return None

# Function to find the distance between two addresses using the distance_list
def distance_between_address(address1, address2):
    distance = distance_list[address1][address2]
    if distance == '':
        distance = distance_list[address2][address1]
    return float(distance)

# Creates an instance of the HashTable class
package_hash_table = HashTable()

# Loads the package.csv file
with open('package.csv', newline='') as package_file:
    package_reader = csv.reader(package_file)
    next(package_reader)
    # This loop reads from the file and stores information appropriately
    for pack in package_reader:
        packID = int(pack[0])
        packStreet = pack[1]
        packCity = pack[2]
        packState = pack[3]
        packZip = pack[4]
        packTimeDeadline = pack[5]
        packWeight = pack[6]
        packNote = pack[7]

        # Creates an object of the PackageInfo class and inserts it into the hash table
        package = PackageInfo(packID, packStreet, packCity, packState, packZip, packTimeDeadline, packWeight, packNote)
        package_hash_table.insert(package)

# Creates 3 Truck objects and passing values to the attributes 15,14,13,16,17,19,20,23,24,26,27,29,30
truck1 = Truck("4001 South 700 East", timedelta(hours=8), [15,1,14,13,16,34,20,37,40,29,30,19,31])
truck3 = Truck("4001 South 700 East", timedelta(hours=9, minutes=5), [25,6,26,27,28,8,32,11,12,21,22,5,33])
truck2 = Truck("4001 South 700 East", timedelta(hours=10, minutes=20), [2,3,4,7,9,18,10,17,35,36,23,38,39,24])

def truck_delivery(truck):
    currently_enroute = []
    # This loop adds packages to the currently_enroute list
    for package_ID in truck.truckPackages:
        package = package_hash_table.lookup(package_ID)
        currently_enroute.append(package)

    while len(currently_enroute) > 0:
        next_dest = float('inf')
        next_package = None
        # This loop finds the distance using the method distance_between_address
        for package in currently_enroute:
            # prioritize packages 25 and 6 to meet deadline
            if package.ID in [25, 6]:
                next_package = package
                next_dest = distance_between_address(find_address_id(truck.truckLocation),
                                                     find_address_id(package.address))
                break
            # else find the next closest package
            dist = distance_between_address(find_address_id(truck.truckLocation), find_address_id(package.address))
            if dist < next_dest:
                next_dest = dist
                next_package = package

        truck.miles += next_dest # Update total miles traveled by the truck
        truck.truckLocation = next_package.address # Update the truck's current location
        truck.currentTime += timedelta(hours=next_dest / truck.truckSpeed) # Update the truck's current time
        next_package.delivery_time = truck.currentTime # Set the delivery time of the next package to the truck's current time
        next_package.departure_time = truck.departureTime # Set the departure time of the next package to the truck's departure time
        currently_enroute.remove(next_package) # Remove the delivered package from the list of packages en route
        truck.deliveredPackages.append(next_package.ID) # Add the delivered package's ID to the list of delivered packages

# Passing the Truck objects into the delivery method to complete the calculations
truck_delivery(truck1)
truck_delivery(truck3)
# Truck 2 doesn't leave until either truck 1 or 3 comes back
truck2.departureTime = min(truck1.currentTime, truck3.currentTime)
truck_delivery(truck2)

# This method displays the info for all the packages
def display_all_packages_status(time_input_delta):
    for packageID in range(1, 41):
        package = package_hash_table.lookup(packageID)
        if package:
            package.package_Status(time_input_delta)
            truck_info = ""
            if packageID in truck1.deliveredPackages:
                truck_info = " 1"
            elif packageID in truck2.deliveredPackages:
                truck_info = " 2"
            elif packageID in truck3.deliveredPackages:
                truck_info = " 3"

            print(f"ID: {package.ID}, Address: {package.address}, {package.city}, {package.state}, {package.zip}, Status: {package.status}, Deadline: {package.time_deadline}, Delivery Time: {package.delivery_time}, Truck: {truck_info}, Weigh: {package.weight}")

# main method
print("Western Governors University Parcel Service")
total_miles = truck1.miles + truck2.miles + truck3.miles
print("The Total miles for all Trucks is: {:.2f}".format(total_miles))

while True:
    userTime = input("Please enter a time for which you'd like to see the status of each package (HH:MM): ")
    h, m = map(int, userTime.split(":"))
    time_input_delta = timedelta(hours=h, minutes=m)  # Convert time_input to timedelta

    view_all = input("Do you want to see the status for all packages? (Y/N): ").strip().lower()
    if view_all == 'y':
        print("Information for all Packages \n")
        display_all_packages_status(time_input_delta)
    else:
        try:
            singleEntry = [int(input("Enter the ID for the package to receive information: "))]
        except ValueError:
            singleEntry = range(1, 41)
        for packageID in singleEntry:
            package = package_hash_table.lookup(packageID)
            if package:
                package.package_Status(time_input_delta)
                print("---Package Info---")
                print(package)  # Print the package info including the status

                # Determine which truck is carrying the package and print its info
                if packageID in truck1.deliveredPackages:
                    print("----Truck 1----")
                    print(truck1)
                elif packageID in truck2.deliveredPackages:
                    print("----Truck 2----")
                    print(truck2)
                elif packageID in truck3.deliveredPackages:
                    print("----Truck 3----")
                    print(truck3)
            else:
                print(f"Package ID {packageID} not found.")
