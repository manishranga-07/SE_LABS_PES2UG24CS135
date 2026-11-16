import math

def parse_transit_corridor(corridor_code):
    """
    Parses corridor code in format 'ORIG-DEST-ZONES' (e.g. 'DT-UP-3').
    Hardened against invalid types, malformed strings, and out-of-range zones.
    """
    if not isinstance(corridor_code, str):
        return None
    try:
        parts = corridor_code.strip().split('-')
        if len(parts) != 3:
            return None
        orig, dest, zones_str = parts
        orig = orig.strip()
        dest = dest.strip()
        if not orig or not dest:
            return None
        zones = int(zones_str.strip())
        if zones < 0 or zones > 1000:
            return None
        base_fare = 2.50 + (zones * 0.75)
        return f"Route {orig.upper()}->{dest.upper()}: {zones} Zones, Fare ${base_fare:.2f}"
    except (ValueError, TypeError, AttributeError, OverflowError):
        return None

def lookup_concession_discount(category_name):
    """
    Looks up concession discount multiplier for a passenger category.
    Hardened against invalid types, unknown categories, and unexpected whitespace.
    """
    if not isinstance(category_name, str):
        return None
    try:
        category = category_name.strip().upper()
        discounts = {
            "STANDARD": 1.00,
            "STUDENT": 0.50,
            "SENIOR": 0.35,
            "MILITARY": 0.20,
            "CHILD": 0.00
        }
        return discounts.get(category, None)
    except (AttributeError, TypeError):
        return None

def compute_passenger_density(occupancy_ratio_str):
    """
    Computes passenger density from 'passengers/km' (e.g. '50/10.0').
    Hardened against division by zero, negative values, NaNs, and non-numeric inputs.
    """
    if not isinstance(occupancy_ratio_str, str):
        return None
    try:
        parts = occupancy_ratio_str.strip().split('/')
        if len(parts) != 2:
            return None
        passengers_str, km_str = parts
        passengers = float(passengers_str.strip())
        km = float(km_str.strip())
        if math.isnan(passengers) or math.isnan(km) or math.isinf(passengers) or math.isinf(km):
            return None
        if km <= 0 or passengers < 0:
            return None
        density = passengers / km
        return round(density, 2)
    except (ValueError, TypeError, AttributeError, ZeroDivisionError, OverflowError):
        return None

def main():
    print("==== Running parse_transit_corridor ====")
    c_input = input("Enter corridor (e.g. DT-UP-3): ")
    print(parse_transit_corridor(c_input))

    print("\n==== Running lookup_concession_discount ====")
    cat_input = input("Enter concession category (e.g. STUDENT, SENIOR): ")
    print("Multiplier:", lookup_concession_discount(cat_input))

    print("\n==== Running compute_passenger_density ====")
    d_input = input("Enter passengers/km (e.g. 50/10.0): ")
    print("Density:", compute_passenger_density(d_input))

if __name__ == "__main__":
    main()
