# ===========================================================
#              ELECTRICITY BILL CALCULATOR
# ===========================================================
# This program calculates the electricity bill based on
# the number of units consumed.
#
# Different units have different rates:
# 0 - 100 units   -> ₹5 per unit
# 101 - 300 units  -> ₹7 per unit
# Above 300 units  -> ₹10 per unit
# ===========================================================


# Take electricity consumption as input.
# float() allows decimal values as well.

units = float(input("Enter units consumed: "))


# -----------------------------------------------------------
# SLAB 1: UP TO 100 UNITS
# -----------------------------------------------------------
# If consumption is 100 units or less,
# every unit is charged at ₹5.

if units <= 100:

    bill = units * 5


# -----------------------------------------------------------
# SLAB 2: 101 TO 300 UNITS
# -----------------------------------------------------------
# The first 100 units are charged at ₹5.
# The remaining units are charged at ₹7.

elif units <= 300:

    bill = (100 * 5) + (units - 100) * 7


# -----------------------------------------------------------
# SLAB 3: ABOVE 300 UNITS
# -----------------------------------------------------------
# First 100 units -> ₹5 per unit
# Next 200 units  -> ₹7 per unit
# Remaining units -> ₹10 per unit

else:

    bill = (100 * 5) + (200 * 7) + (units - 300) * 10


# -----------------------------------------------------------
# DISPLAY FINAL BILL
# -----------------------------------------------------------

print("Electricity Bill:", bill)


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ if
#    Checks the first condition.
#
# ✔ elif
#    Checks another condition if the previous one is false.
#
# ✔ else
#    Runs when none of the above conditions are true.
#
# ✔ Electricity billing uses a SLAB SYSTEM.
#
# Example:
# If units = 350
#
# First 100 units:
# 100 × ₹5 = ₹500
#
# Next 200 units:
# 200 × ₹7 = ₹1400
#
# Remaining 50 units:
# 50 × ₹10 = ₹500
#
# Total:
# ₹500 + ₹1400 + ₹500 = ₹2400
# ===========================================================
