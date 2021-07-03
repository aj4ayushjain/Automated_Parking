from Vehicle import Vehicle
from utils import comma_sep

class Slot():
    def __init__(self, number, available):
        self.number = number
        self.available = available
        self.car = None
    

class ParkingLot():
    def __init__(self, total):
        self.slots = []
        for num in range(total):
            self.slots.append(Slot(num + 1, True))
        print("Parking Lot initialized with {} Slots".format(total))

    def park(self, reg_no, driver_age):
        '''
        1. Pick the nearest free slot(Parking strategy)
        2. Assign the slot to Vehicle and mark it unavailable
      '''
        free_slot = self.parking_strategy()

        if free_slot is not None:
            free_slot.car = Vehicle(reg_no, driver_age)
            free_slot.available = False

        return free_slot

    def parking_strategy(self):
    
        for slot in self.slots:
            if slot.available:
                return slot
        
        return None

    def slot_with_age(self, age):

        result = []
        for slot in self.slots:
            if not slot.available and slot.car.drivers_age == age:
                result.append(str(slot.number))

        return comma_sep(result)

    def slot_with_reg_no(self, reg_no):

        for slot in self.slots:
            if not slot.available and slot.car.registration_no == reg_no:
                return slot.number

        return None

    def exit(self, slot_no):
        for slot in self.slots:
            if int(slot.number) == slot_no and not slot.available:
              slot.available = True
              return slot
        return None

    def reg_no_with_age(self, age):
        result = []
        for slot in self.slots:
            if not slot.available and slot.car.drivers_age == age:
                result.append(str(slot.car.reg_no))

        return comma_sep(result)

    