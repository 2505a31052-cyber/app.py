# ==========================================
# MECHANICAL ENGINEERING CALCULATOR
# ==========================================

# ---------- 1. MECHANICS ----------

def force():
    m = float(input("Enter mass (kg): "))
    a = float(input("Enter acceleration (m/s^2): "))
    print("Force =", m * a, "N")


def work():
    f = float(input("Enter force (N): "))
    d = float(input("Enter distance (m): "))
    print("Work =", f * d, "J")


def power():
    w = float(input("Enter work (J): "))
    t = float(input("Enter time (s): "))
    print("Power =", w / t, "W")


def kinetic_energy():
    m = float(input("Enter mass (kg): "))
    v = float(input("Enter velocity (m/s): "))
    print("Kinetic Energy =", 0.5 * m * v * v, "J")


# ---------- 2. STRENGTH OF MATERIALS ----------

def stress():
    f = float(input("Enter force (N): "))
    area = float(input("Enter area (m^2): "))
    print("Stress =", f / area, "Pa")


def strain():
    change = float(input("Enter change in length (m): "))
    original = float(input("Enter original length (m): "))
    print("Strain =", change / original)


def youngs_modulus():
    stress_value = float(input("Enter stress (Pa): "))
    strain_value = float(input("Enter strain: "))
    print("Young's Modulus =", stress_value / strain_value, "Pa")


# ---------- 3. THERMODYNAMICS ----------

def heat_transfer():
    m = float(input("Enter mass (kg): "))
    cp = float(input("Enter specific heat (J/kg-K): "))
    change_temp = float(input("Enter change in temperature (K): "))
    print("Heat Transfer =", m * cp * change_temp, "J")


def thermo_work():
    pressure = float(input("Enter pressure (Pa): "))
    volume_change = float(input("Enter change in volume (m^3): "))
    print("Work Done =", pressure * volume_change, "J")


def thermal_efficiency():
    work_output = float(input("Enter work output (J): "))
    heat_input = float(input("Enter heat input (J): "))
    print("Thermal Efficiency =",
          (work_output / heat_input) * 100, "%")


# ---------- 4. FLUID MECHANICS ----------

def pressure():
    force_value = float(input("Enter force (N): "))
    area = float(input("Enter area (m^2): "))
    print("Pressure =", force_value / area, "Pa")


def reynolds_number():
    density = float(input("Enter density (kg/m^3): "))
    velocity = float(input("Enter velocity (m/s): "))
    diameter = float(input("Enter diameter (m): "))
    viscosity = float(input("Enter dynamic viscosity (Pa.s): "))

    re = (density * velocity * diameter) / viscosity
    print("Reynolds Number =", re)


def flow_velocity():
    flow_rate = float(input("Enter flow rate (m^3/s): "))
    area = float(input("Enter area (m^2): "))
    print("Flow Velocity =", flow_rate / area, "m/s")


def discharge():
    area = float(input("Enter area (m^2): "))
    velocity = float(input("Enter velocity (m/s): "))
    print("Discharge =", area * velocity, "m^3/s")


# ---------- 5. THERMAL ENGINEERING ----------

def heat_conduction():
    k = float(input("Enter thermal conductivity (W/m-K): "))
    area = float(input("Enter area (m^2): "))
    temp_difference = float(input("Enter temperature difference (K): "))
    thickness = float(input("Enter thickness (m): "))

    heat = (k * area * temp_difference) / thickness
    print("Heat Conduction =", heat, "W")


def cop():
    cooling_effect = float(input("Enter cooling effect (J): "))
    work_input = float(input("Enter work input (J): "))
    print("COP =", cooling_effect / work_input)


def heat_engine_efficiency():
    work_output = float(input("Enter work output (J): "))
    heat_input = float(input("Enter heat input (J): "))
    print("Heat Engine Efficiency =",
          (work_output / heat_input) * 100, "%")


# ---------- 6. MACHINE DESIGN ----------

def torque():
    force_value = float(input("Enter force (N): "))
    radius = float(input("Enter radius (m): "))
    print("Torque =", force_value * radius, "N-m")


def shaft_power():
    torque_value = float(input("Enter torque (N-m): "))
    speed = float(input("Enter speed (RPM): "))

    power_value = (2 * 3.14159 * speed * torque_value) / 60
    print("Shaft Power =", power_value, "W")


def shaft_diameter():
    torque_value = float(input("Enter torque (N-m): "))
    shear_stress = float(input("Enter allowable shear stress (Pa): "))

    # T = (pi/16) * tau * d^3
    import math
    diameter = ((16 * torque_value) /
                (math.pi * shear_stress)) ** (1 / 3)

    print("Shaft Diameter =", diameter, "m")


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n========================================")
    print("   MECHANICAL ENGINEERING CALCULATOR")
    print("========================================")
    print("1. Mechanics")
    print("2. Strength of Materials")
    print("3. Thermodynamics")
    print("4. Fluid Mechanics")
    print("5. Thermal Engineering")
    print("6. Machine Design")
    print("7. Exit")

    main_choice = input("Enter your choice: ")

    # ---------- MECHANICS ----------
    if main_choice == "1":

        print("\n--- MECHANICS ---")
        print("1. Force")
        print("2. Work")
        print("3. Power")
        print("4. Kinetic Energy")

        choice = input("Enter your choice: ")

        if choice == "1":
            force()
        elif choice == "2":
            work()
        elif choice == "3":
            power()
        elif choice == "4":
            kinetic_energy()
        else:
            print("Invalid choice!")

    # ---------- STRENGTH ----------
    elif main_choice == "2":

        print("\n--- STRENGTH OF MATERIALS ---")
        print("1. Stress")
        print("2. Strain")
        print("3. Young's Modulus")

        choice = input("Enter your choice: ")

        if choice == "1":
            stress()
        elif choice == "2":
            strain()
        elif choice == "3":
            youngs_modulus()
        else:
            print("Invalid choice!")

    # ---------- THERMODYNAMICS ----------
    elif main_choice == "3":

        print("\n--- THERMODYNAMICS ---")
        print("1. Heat Transfer")
        print("2. Work Done")
        print("3. Thermal Efficiency")

        choice = input("Enter your choice: ")

        if choice == "1":
            heat_transfer()
        elif choice == "2":
            thermo_work()
        elif choice == "3":
            thermal_efficiency()
        else:
            print("Invalid choice!")

    # ---------- FLUID MECHANICS ----------
    elif main_choice == "4":

        print("\n--- FLUID MECHANICS ---")
        print("1. Pressure")
        print("2. Reynolds Number")
        print("3. Flow Velocity")
        print("4. Discharge")

        choice = input("Enter your choice: ")

        if choice == "1":
            pressure()
        elif choice == "2":
            reynolds_number()
        elif choice == "3":
            flow_velocity()
        elif choice == "4":
            discharge()
        else:
            print("Invalid choice!")

    # ---------- THERMAL ENGINEERING ----------
    elif main_choice == "5":

        print("\n--- THERMAL ENGINEERING ---")
        print("1. Heat Conduction")
        print("2. COP")
        print("3. Heat Engine Efficiency")

        choice = input("Enter your choice: ")

        if choice == "1":
            heat_conduction()
        elif choice == "2":
            cop()
        elif choice == "3":
            heat_engine_efficiency()
        else:
            print("Invalid choice!")

    # ---------- MACHINE DESIGN ----------
    elif main_choice == "6":

        print("\n--- MACHINE DESIGN ---")
        print("1. Torque")
        print("2. Shaft Power")
        print("3. Shaft Diameter")

        choice = input("Enter your choice: ")

        if choice == "1":
            torque()
        elif choice == "2":
            shaft_power()
        elif choice == "3":
            shaft_diameter()
        else:
            print("Invalid choice!")

    # ---------- EXIT ----------
    elif main_choice == "7":
        print("\nThank you for using the calculator!")
        break

    else:
        print("Invalid choice! Please try again.")
