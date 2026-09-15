# This model calculates the annual usage value of inventory items and classifies them into A, B and C categories.


# This list contains the inventory items, their annual demand and their unit cost.
skus = [
    {"sku": "BRK-100", "demand": 2000, "cost": 45},
    {"sku": "GSK-220", "demand": 1500, "cost": 30},
    {"sku": "BLT-010", "demand": 10000, "cost": 2},
    {"sku": "BRG-330", "demand": 800, "cost": 60},
    {"sku": "SEAL-500", "demand": 3000, "cost": 5},
    {"sku": "MTR-700", "demand": 50, "cost": 800},
    {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
    {"sku": "CBL-900", "demand": 400, "cost": 25},
    {"sku": "PMP-800", "demand": 1000, "cost": 10},
    {"sku": "NUT-600", "demand": 5000, "cost": 1},
]


# This function calculates the annual usage value by multiplying demand by cost.
def classify_inventory(skus):

    # This function calculates the usage value of one inventory item.
    def usage_value(demand, cost):
        return demand * cost

    # This calculates and stores the annual usage value for every inventory item.
    for item in skus:
        item["value"] = usage_value(item["demand"], item["cost"])

    # This sorts the inventory items from the highest usage value to the lowest.
    skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

    # This calculates the total usage value of all the inventory items.
    total_value = sum(item["value"] for item in skus_sorted)

    # This starts the running total at zero for calculating cumulative value.
    running_total = 0

    # This calculates the cumulative percentage of the total inventory value.
    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100

    # This function assigns each inventory item to A, B or C based on its cumulative percentage.
    def assign_tier(cum_pct):
        if cum_pct <= 70:
            return "A"
        elif cum_pct <= 90:
            return "B"
        else:
            return "C"

    # This assigns an A, B or C classification to each inventory item.
    for item in skus_sorted:
        item["tier"] = assign_tier(item["cum_pct"])

    # This returns the sorted inventory list with the calculated values and classifications.
    return skus_sorted


# This runs the classification function using the inventory data.
classified_skus = classify_inventory(skus)


# This prints the inventory items together with their value, cumulative percentage and classification.
for item in classified_skus:
    print(item["sku"], "| value:", item["value"],
          "| cum %:", round(item["cum_pct"], 1),
          "| tier:", item["tier"])


# This creates counters to keep track of how many items are in each classification.
tier_counts = {"A": 0, "B": 0, "C": 0}


# This counts the number of inventory items classified as A, B and C.
for item in classified_skus:
    tier_counts[item["tier"]] += 1


# This displays the final number of items in each classification.
print(tier_counts)


#5.1 Adding two more SKUs changed the tier split because there were now 10 inventory items instead of 8.The additional items affected the cumulative value and classifications.
#5.2 Changing the threshold to 70% and 90% resulted in A:3 ,B:3 ,C:4 items
#5.3 The classify_inventory(skus) function combines Step 2-6 by calculating usage values,sorting the SKUs,calculating cumulative percentages ,assigning A/B/C tiers and returning the sorted and classified list.