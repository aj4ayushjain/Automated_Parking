from ParkingLot import ParkingLot
import sys

def parse_input(content):
  try:
    if content:
      total_count = content[0].strip().split()[1]

      # Initliaze a parking lot 
      parking_lot = ParkingLot(int(total_count))
      
      for line in content[1:]:
        n = line.strip().split()
        #print(n)

        # All the operations to be perfomed in the parking lot
        if n[0] == "Park":
          slot = parking_lot.park(n[1], n[3])
          if slot:
              print("Car with vehicle registration number {0} has been parked at slot number {1}".format(n[1], slot.number))
          else:
              print("EH! Parking lot is full")
        elif n[0] == "Slot_numbers_for_driver_of_age":
          slots = parking_lot.slot_with_age(n[1])
          if slots:
              print(slots)
          else:
              print("No car with driver age {} parked".format(n[1]))
        elif n[0] == "Slot_number_for_car_with_number":
          slot_number = parking_lot.slot_with_reg_no(n[1])
          if slot_number:
              print(slot_number)
          else:
              print("No car with registration number {} parked".format(n[1]))
        elif n[0] == "Leave":
          empty_slot = parking_lot.exit(int(n[1]))

          if empty_slot is not None:
            print("Slot number {} vacated, the car with vehicle registration number {} left space, "
                              "the driver of the car was of age {}".format(n[1], empty_slot.car.registration_no, empty_slot.car.drivers_age))
          else:
            print("Slot vacant")
        elif n[0] == "Vehicle_registration_number_for_driver_of_age":
          reg_no = parking_lot.reg_no_with_age(n[1])
          if reg_no:
              print(reg_no)
          else:
              print("")
        else:
          print("Unknown Command")

    else:
      print("Input file is empty")

  except IndexError:
    print("Please look at input format")


if __name__ == "__main__":
    filename = 'input.txt'
    if len(sys.argv) > 1 :
      filename = sys.argv[1]
    try:
      with open(filename, 'r') as f:
        content = f.readlines()
        #print(content)
        parse_input(content)
    except Exception as e:
      print("Error reading input file - {}".format(e))

    print("Execution completed")