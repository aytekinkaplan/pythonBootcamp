all_us_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California",
                 "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
                 "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
                 "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
                 "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
                 "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                 "New Mexico", "New York", "North Carolina", "North Dakota",
                 "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
                 "South Carolina", "South Dakota", "Tennessee", "Texas",
                 "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
                 "Wisconsin", "Wyoming"]


# use of enumerate
def search_state(all_us_states, state):
    for index, value in enumerate(all_us_states):
        if value == state:
            return index

    return -1


print(search_state(all_us_states, "Missouri"))
print(search_state(all_us_states, "Vermont"))
print(search_state(all_us_states, "Florida"))
print(search_state(all_us_states, "California"))
print(search_state(all_us_states, "Alaska"))
print(search_state(all_us_states, "Nebraska"))
