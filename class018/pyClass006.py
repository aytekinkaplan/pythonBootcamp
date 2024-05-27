def merge_shopping_lists(*lists):
    # If no arguments are passed, return an empty set
    if not lists:
        return set()

    # Use set union to merge all sets into one, ensuring no duplicates
    merged_set = set().union(*lists)
    return merged_set


# Example usage
list1 = {"apples", "bananas", "cherries"}
list2 = {"bananas", "dates", "eggs"}
list3 = {"cherries", "dates", "figs"}

print(merge_shopping_lists(list1, list2, list3))
# Output: {"apples", "bananas", "cherries", "dates", "eggs", "figs"}

list4 = {"bread", "milk"}
list5 = {"milk", "eggs", "juice"}
print(merge_shopping_lists(list4, list5))
# Output: {"bread", "milk", "eggs", "juice"}
