def generate_planner(attractions, days):
    
    itinerary  = []

    total_places = len(attractions)

    places_per_day = max(1, total_places//days)

    current_index = 0

    for day in range(days):
        day_plan = []

        for _ in range(places_per_day):

            if current_index<total_places:
                day_plan.append(attractions[current_index])

                current_index+=1
        itinerary.append(day_plan)

    while current_index < total_places:
        itinerary[-1].append(attractions[current_index])

        current_index+=1
    
    return itinerary