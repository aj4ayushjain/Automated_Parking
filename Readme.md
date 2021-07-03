# Automated Parking Lot 
## Setup
 + Instructions to Run

    1. In Terminal

      `python3 main.py`
    2. If new file is to be given input

      `python3 main.py /location_of_file`
  
  + Instructions to run test

    1. `python test.py `
    
## Design
1. Object Oriented Design

      + **ParkingLot**(Total_slot) - parking lot related configurations,operationa functions

      + **Slot**(availability, Vehicle) - small unit in big parking lot and stores Vehicle and slot functions
      + **Vehicle**(registration_no, driver_age) - Handle driver and vehicle related functions and info  
      + utils - to handle all the utility functions
2. Assumptions:

    + Single entry and exit of     Vehicle and a single operation at a time
    + Input given is uniform and parking lot creation happens initally at beginning only
3. Base Logic:
    +  Initalize the **ParkingLot** by creating **n** **Slot** and making them available.

    +  When the vehicle enters check for freeslots (available=True) and assign it to the Vehicle. - O(n)

    + When the vehicle exits, update the Slot with availability to True and on next entry to slot the details would be updated.