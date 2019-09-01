import sys


class ParkingLot(object):
    def __init__(self, n):
        ''' Initializing the parking lot with slots avalable'''
        self.availability = [str(i) for i in range(1, n+1)]
        self.slots_reg_mapping = {}
        self.reg_slot_mapping = {}
        self.colors_mapping = {}
        print("Created a parking lot with {} slots".format(n))

    def parkvehicle(self, registartion_no, color=None):
        ''' Updating the availability and alloting  them to vehicle'''
        if len(self.availability) > 0:
            slot = self.availability.pop(0)
            self.slots_reg_mapping[slot] = (registartion_no, color)
            self.reg_slot_mapping[registartion_no] = (slot, color)
            if color not in self.colors_mapping:
                self.colors_mapping[color] = {registartion_no: slot}
            else:
                self.colors_mapping[color][registartion_no] = slot
            print("Allocated slot number: {}".format(slot))
            return
        print("Sorry, parking lot is full")
        return

    def vacate(self, slot_no):
        ''' Making the slot available and updating in corresponding regn_slot,slot_regn,color mapping'''
        if slot_no not in self.slots_reg_mapping:
            print("Slot no {} not having any vehicle atready".format(slot_no))
        regn_no, color = self.slots_reg_mapping[slot_no]
        self.colors_mapping[color].pop(regn_no, None)
        self.reg_slot_mapping.pop(regn_no, None)
        self.slots_reg_mapping.pop(slot_no, None)
        self.availability.append(slot_no)
        print("Slot number {} is free".format(slot_no))

    def registratin_nos_of_color(self, color):
        ''' Showing regn no of cars of particular color'''
        if color not in self.colors_mapping:
            print("No Vehicle of color {}".format(color))
        else:
            if len(self.colors_mapping[color].keys()) <= 0:
                print("No Vehicle of color {}".format(color))
            else:
                res = ""
                for regn_no in sorted(self.colors_mapping[color].keys()):
                    res += regn_no + ", "
                print(res[:-2])

    def slot_numbers_for_cars_with_colour(self, color):
        ''' Showing slot no of cars of particular color'''
        if color not in self.colors_mapping:
            print("No Vehicle of color {}".format(color))
        else:
            if len(self.colors_mapping[color].values()) <= 0:
                print("No slots of color {}".format(color))
            else:
                res = ""
                for val in sorted(self.colors_mapping[color].values()):
                    res += val[0] + ", "
                print(res[:-2])

    def slot_number_for_registration_number(self, reg_no):
        ''' Showing slot no of a registration number'''
        if reg_no in self.reg_slot_mapping:
            print(self.reg_slot_mapping[reg_no][0])
        else:
            print("Not found")


if __name__ == "__main__":
    parking_lot = None
    with open(sys.argv[1]) as fp:
        for line in fp:
            sp = line.split()
            # if len(sp) > 0:
            try:
                command = sp[0]
                if command.lower() == "create_parking_lot":
                    parking_lot = ParkingLot(int(sp[1]))
                elif command.lower() == "park":
                    parking_lot.parkvehicle(sp[1], sp[2])
                elif command.lower() == "leave":
                    parking_lot.vacate(sp[1])
                elif command.lower() == "status":
                    print("Slot No.\t Registration No\tColour")
                    for key in sorted(parking_lot.slots_reg_mapping.items()):
                        print("{}\t{}\t{}".format(
                            key[0], key[1][0], key[1][1]))
                elif command.lower() == "registration_numbers_for_cars_with_colour":
                    parking_lot.registratin_nos_of_color(sp[1])
                elif command.lower() == "slot_numbers_for_cars_with_colour":
                    parking_lot.slot_numbers_for_cars_with_colour(sp[1])
                elif command.lower() == "slot_number_for_registration_number":
                    parking_lot.slot_number_for_registration_number(sp[1])
            except:
                print("empty input exception")
