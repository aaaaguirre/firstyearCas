# Q1
class FurnitureCompany:

    def __init__(self, name_of_company_in, production_run_in):
        self.company_name = name_of_company_in
        self.production_lines = 2
        self.imported_mats = True  # Boolean
        self.total_of_units_produced = 0
        self.total_production_cost = 0
        self.production_run = production_run_in

    def production_run(self, hours_lines_running):
        self.production_lines += 2
        self.total_of_units_produced += hours_lines_running
        self.calculate_production_cost(hours_lines_running)

    def calculate_production_cost(self, cost_current_production):
        if self.total_of_units_produced > 100:
            cost_current_production = 500.0
        else:
            cost_current_production = 0
        if self.total_of_units_produced >= 300:
            cost_current_production = 400.0
        else:
            cost_current_production = 0
        if self.total_of_units_produced < 300:
            cost_current_production = 500.0
        else:
            cost_current_production = 0
        self.total_production_cost += cost_current_production

    def calculate_average_production(self):
        if self.total_of_units_produced == 0:
            return 0
        return round(self.total_of_units_produced / self.production_lines, 2)

    def calculate_importation_charge(self, charge=5):
        if charge >= self.imported_mats:
            self.imported_mats = True
            return True
        else:
            self.imported_mats -= charge
            return False

    def print(self):
        print("******************************************")
        print("*           Furniture Company            *")
        print("******************************************")
        print("Name         :", self.company_name)
        print("Number of Production lines           :", self.production_lines)
        print("Imported Material   :", self.imported_mats)
        print("Total number of units produced to date       :", self.total_of_units_produced)
        print("Total production cost to date      :", self.total_production_cost)


# subclass
class StartupFurnitureCompany(FurnitureCompany):
    def __int__(self, type_of_startup=3, startup_grant=0, imported_mat=False):
        super().__init__(type_of_startup, startup_grant)
        if type_of_startup == 1:
            self.furniture_grant = 1000.0
        elif type_of_startup == 2:
            self.furniture_grant = 3000.0
        elif type_of_startup == 3:
            self.furniture_grant = 5000.0
        else:
            self.furniture_grant = 0

    def calculate_importation_charge(self, charge=5):
        importation = super().calculate_importation_charge()
        if importation > 200:
            print("Additional Charge: 10%")

    def print(self):
        super().print()



# main body of code
company_name = str(input("Enter name of the Company:  "))

l1 = FurnitureCompany(company_name, 4)
l2 = FurnitureCompany(company_name, 5)

l1 = StartupFurnitureCompany(company_name, 5)

print("Average Number of units produced for line 1:" + str(l1.calculate_average_production()))
print("Importation Charge for line 1: €" + str(l1.calculate_importation_charge()))

print("Average Number of units produced for line 2:" + str(l2.calculate_average_production()))
print("Importation Charge for line 2: €" + str(l2.calculate_importation_charge()))

l1.print()
l2.print()
