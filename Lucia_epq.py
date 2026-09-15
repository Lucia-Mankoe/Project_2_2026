# This program calculates the Economic Production Quantity (EPQ)
import math

# Input values
annual_demand = 12000        # units per year 
setup_cost = 50              # cost per production run, in Rand 
holding_cost = 2             # cost per unit per year, in Rand 
daily_demand_rate = 40       # units produced/sold per day 
daily_production_rate = 100000  # units your process can make per day

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate): 
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate))) 
  
epq = calculate_epq(annual_demand, setup_cost, holding_cost, 
                    daily_demand_rate, daily_production_rate) 
print("Optimal production quantity:", round(epq, 2))

# Calculate production runs per year
runs_per_year = annual_demand / epq 

# Calculate length of each production run
run_length_days = epq / daily_production_rate 
  
print("Production runs per year:", round(runs_per_year, 2)) 
print("Length of each run (days):", round(run_length_days, 1))

# Calculate maximum inventory level
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate) 
print("Maximum inventory level:", round(max_inventory, 2)) 

#5.1 When the daily production rate increases from 100 to 150 units per day, the EPQ decreases from 1000 units to 904.53 units.This makes sense because the faster production rate allows inventory to be replenished more quickly, so a smaller production quantity is needed.

#5.2 When the daily production rate is increased to 100,000 units per day, the EPQ decreases to approximately 774.75 units. This is almost the same as the EOQ because the production rate is extremely high compared with the demand rate. Therefore, the effect of gradual production becomes very small and EPQ approaches EOQ.
