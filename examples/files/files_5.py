import pickle
import os.path
from vehicle import Vehicle

# Save custom data types (serialized) to a file in binary format

# Seraialization
# common when we stream data from one location to another
# memory to network
# over the network
# Pickle does serialization for us

# Exception handling
# file may be locked by another process
# disk space full
# no permission for the location

def get_path():
    path = os.path.expanduser("~/files-example")
    if not os.path.exists(path): os.makedirs(path)
    path += "/"

    return path

# list of vehicles
vehicles = []
vehicles.append(Vehicle("Datsun", "160J SSS", 1598, 68))
vehicles.append(Vehicle("BMW", "650i", 4799, 315))
vehicles.append(Vehicle("Toyota", "Crown", 1999, 52))
vehicles.append(Vehicle("Plymouth", "DEATHFISH 2", 6382, 721))

# print vehicles
for vehicle in vehicles: print(vehicle)

filename = "vehicles.dat" # the naming is completely up to you. the extenion affects how you deal with them. this will be a binary file so we called it .dat, you can call it whatever

try:
    file = open(get_path() + filename, "wb") # wb means write binary (raw bytes, no processing)
    pickle.dump(vehicles, file, pickle.HIGHEST_PROTOCOL) # HIGHEST_PROTOCOL = maximum shrinkage of data, produce as small a file as possible. smallest, most efficient file pickle library can do
except Exception as e:
    print("Failed to write file:", filename)
    print("Exception:", e)
finally:
    file.close()

# objects are now saved, clear the list and read them back
vehicles.clear()

try:
    file = open(get_path() + filename, "rb")
    vehicles = pickle.load(file)
except Exception as e:
    print("Failed to write file:", filename)
    print("Exception:", e)
finally:
    file.close()

# print the vehicles
for vehicle in vehicles: print(vehicle)

# can check internet
# do it by yourself, no chatting with freinds

# library simulations
# database of games you have played and completion data
