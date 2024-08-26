# Convert procecssing code to function
def process_results(data):
    # Create blank dictionary  
    flattened_data = {}
    # Loop through each video
    for idx, value in enumerate(data['data']['videos']):
        flattened_data[idx] = {}
        # Loop through each property in each video
        for prop_idx, prop_value in value.items():
            #print(prop_idx)
            flattened_data[idx][prop_idx] = prop_value

    return flattened_data