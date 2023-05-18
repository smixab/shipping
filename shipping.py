"""Module for Sal's Shipping."""
#Baxter Smith

WEIGHT = 4.8

#Ground shipping

if WEIGHT <= 2:
    COST_GROUND = WEIGHT * 1.5 + 20
elif WEIGHT > 2 and WEIGHT <= 6:
    COST_GROUND = WEIGHT * 3 + 20
elif WEIGHT > 6 and WEIGHT <= 10:
    COST_GROUND = WEIGHT * 4 + 20
else:
    COST_GROUND = WEIGHT * 4.75 + 20

print("Ground Shipping $", COST_GROUND)

#Ground Shipping Premium

COST_PREMIUM_GROUND = 125.00

print("Ground Shipping Premium $",COST_PREMIUM_GROUND)

#Drone Shipping

if WEIGHT <= 2:
    COST_DRONE = WEIGHT * 4.5
elif WEIGHT > 2 and WEIGHT <= 6:
    COST_DRONE = WEIGHT * 9
elif WEIGHT > 6 and WEIGHT <= 10:
    COST_DRONE = WEIGHT * 12
else:
    COST_DRONE = WEIGHT * 14.25

print("Drone Shipping $", COST_DRONE)
