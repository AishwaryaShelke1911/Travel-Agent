def calculate_budget(data, travel_type, days):
    return data["budget"][travel_type] * days


def generate_day_plan(data, day_number):
    activities = data["activities"]
    return activities[day_number % len(activities)]