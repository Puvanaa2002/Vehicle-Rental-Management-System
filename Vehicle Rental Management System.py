#### ----------------------- VEHICLE RENTAL SYSTEM ------------------------

class Vehicle:
    def __init__(self, name, number, rent_per_day):
        self.name = name
        self.number = number
        self.__rent_per_day = rent_per_day

    def calculate_rent(self, days):
        return self.__rent_per_day * days

    def get_rent_per_day(self):
        return self.__rent_per_day

    def display_info(self):
        print(f"{self.name} | Number: {self.number} | Rent/day: ₹{self.__rent_per_day}")


class Car(Vehicle):
    def __init__(self, name, number, rent_per_day, fuel_type):
        super().__init__(name, number, rent_per_day)
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Car: {self.name} | No: {self.number} | Fuel: {self.fuel_type} | Rent/day: ₹{self.get_rent_per_day()}")


class Bike(Vehicle):
    def __init__(self, name, number, rent_per_day, engine_cc):
        super().__init__(name, number, rent_per_day)
        self.engine_cc = engine_cc

    def display_info(self):
        print(f"Bike: {self.name} | No: {self.number} | Engine: {self.engine_cc}cc | Rent/day: ₹{self.get_rent_per_day()}")


class Truck(Vehicle):
    def __init__(self, name, number, rent_per_day, load_capacity):
        super().__init__(name, number, rent_per_day)
        self.load_capacity = load_capacity

    def display_info(self):
        print(f"Truck: {self.name} | No: {self.number} | Load: {self.load_capacity} tons | Rent/day: ₹{self.get_rent_per_day()}")


class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_list = []

    def rent_vehicle(self, vehicle, days):
        total = vehicle.calculate_rent(days)

        # Discount logic
        if days >= 7:
            discount = 0.15 * total
        elif days >= 3:
            discount = 0.10 * total
        else:
            discount = 0

        final = total - discount
        self.rented_list.append((vehicle, days, final))

        print("\n--- RENT SUCCESSFUL ---")
        print(f"Customer: {self.name}")
        print(f"Vehicle rented: {vehicle.name}")
        print(f"Days: {days}")
        print(f"Original cost: ₹{total}")
        print(f"Discount: ₹{discount:.2f}")
        print(f"Final amount: ₹{final}\n")

    def return_vehicle(self, vehicle_name):
        for entry in self.rented_list:
            if entry[0].name.lower() == vehicle_name.lower():
                self.rented_list.remove(entry)
                print(f"\n{vehicle_name} returned successfully!\n")
                return
        print("\nVehicle not found in your rented list.\n")

    def show_rented(self):
        if not self.rented_list:
            print("\nYou have not rented any vehicle.\n")
            return
        print("\n--- YOUR RENTED VEHICLES ---")
        for v, d, cost in self.rented_list:
            print(f"{v.name} | Days: {d} | Total Cost: ₹{cost}")
        print()


# ----------------------- MENU SYSTEM -----------------------

def main():
    # Vehicles
    vehicles = [
        Car("Hyundai i20", "TN09AB1234", 1500, "Petrol"),
        Bike("Royal Enfield", "TN07CD5678", 800, 350),
        Truck("Tata 407", "TN10EF9876", 3000, 4.5)
    ]
    print("----------- VEHICLE RENTAL SYSTEM -----------")
    username = input("Enter your name: ")
    customer = Customer(username)
    print(f"\nWelcome, {username}!\n")

    while True:
        print("Enter the service you need:")
        print("1. View list of vehicles")
        print("2. Rent a vehicle")
        print("3. Return a vehicle")
        print("4. View rented vehicles")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n--- AVAILABLE VEHICLES ---")
            for v in vehicles:
                v.display_info()
            print()
        elif choice == "2":
            print("\nSelect Vehicle to Rent:")
            for i, v in enumerate(vehicles):
                print(f"{i+1}. {v.name}")
            select = int(input("Enter choice: ")) - 1

            if 0 <= select < len(vehicles):
                days = int(input("Enter number of days: "))
                customer.rent_vehicle(vehicles[select], days)
            else:
                print("Invalid option.\n")
        elif choice == "3":
            if not customer.rented_list:
                print("\nYou have not rented any vehicle.\n")
                continue
            print("\nSelect Vehicle to Return:")
            for i, (v, d, cost) in enumerate(customer.rented_list):
                print(f"{i+1}. {v.name} (Days: {d}, Paid: ₹{cost})")
        
            select = int(input("Enter choice: ")) - 1
        
            if 0 <= select < len(customer.rented_list):
                vehicle_name = customer.rented_list[select][0].name
                customer.return_vehicle(vehicle_name)
            else:
                print("\nInvalid option.\n")
        elif choice == "4":
            customer.show_rented()

        elif choice == "5":
            print("\nThank you for using the Vehicle Rental System!")
            break
        else:
            print("\nInvalid choice, try again!\n")

main()