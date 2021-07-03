import unittest
from ParkingLot import ParkingLot

class SampleTest(unittest.TestCase):
   
   def parking_lot(self):
     parking_lot = ParkingLot(3)
     parking_lot.park("KA-01-HH-1234", 21)
     parking_lot.park("PB-01-HH-1234", 21)
     return parking_lot

   def test_parking_lot_full(self):
      parking_lot = self.parking_lot()
      car3 = parking_lot.park("TN-01-HB-1234", 21)
      self.assertEqual(car3.number,3)
      car4 = parking_lot.park("KL-01-AK-3434", 21)
      self.assertEqual(car4,None)

   def test_leave_empty_lot(self):
     parking_lot = ParkingLot(0)
     car_slot = parking_lot.exit(2)
     self.assertEqual(car_slot, None)

   def test_invalid_slot_data(self):
     parking_lot = self.parking_lot()
     slot_data = parking_lot.slot_with_reg_no("RJ-01-HH-1234")
     self.assertEqual(slot_data, None)
   
   def test_slot_for_valid_number(self):
     parking_lot = self.parking_lot()
     slot_data = parking_lot.slot_with_reg_no("PB-01-HH-1234")
     self.assertEqual(slot_data, 2)

   def test_slot_for_invalid_age(self):
      parking_lot = self.parking_lot()
      slot = parking_lot.slot_with_age(18)
      self.assertEqual(slot, "")
    
   def test_slot_valid_age(self):
      parking_lot = self.parking_lot()
      slot = parking_lot.slot_with_age(21)
      self.assertEqual(slot, "1,2")
  
   def test_create_slot(self):
        parking_lot = ParkingLot(4)
        self.assertEqual(len(parking_lot.slots), 4)
        self.assertEqual(parking_lot.slots[3].available,  True)
   
   def test_empty_slot(self):
     parking_lot = self.parking_lot()
     self.assertEqual(parking_lot.slots[2].available, True)

# running the test
unittest.main()