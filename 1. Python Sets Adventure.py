my_airline = {"ATL", "MIA", "JIA", "ORD", "DTW"}
others_airline = {"ATL", "MIA", "JIA", "ORD", "LGA"}

def destination_indicator(my_airline, others_airline):
    common_destinations= my_airline.intersection(others_airline)
    print("\nDestinations both airlines fly to:") 
    print(common_destinations)
    my_destinations = my_airline.difference(others_airline)
    print("\nDestinations  only my airlines fly to:")
    print(my_destinations) 
    exclusive_destinations = my_airline.symmetric_difference(others_airline)
    print("\nDestinations exclusive that either airlines fly to:")
    print(exclusive_destinations)


    return common_destinations, my_destinations, exclusive_destinations


destination_indicator(my_airline, others_airline)

