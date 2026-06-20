def get_budget_tips(budget_type):

    if budget_type == "Low":

        return [
            "Use public transport",
            "Stay in hostels",
            "Prefer local food",
            "Visit free attractions"
        ]

    elif budget_type == "Medium":

        return [
            "Use metro/scooty",
            "Stay in budget hotels",
            "Visit popular attractions",
            "Try local cafes"
        ]

    else:

        return [
            "Use cab services",
            "Stay in premium hotels",
            "Book guided tours",
            "Try premium restaurants"
        ]