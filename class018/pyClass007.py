def unique_colors(palette1, palette2):
    # Find the union of both palettes
    union_colors = palette1 | palette2

    # Find the intersection of both palettes
    intersection_colors = palette1 & palette2

    # Find the unique colors by subtracting the intersection from the union
    unique_colors_set = union_colors - intersection_colors

    # Return the set containing unique colors
    return unique_colors_set


# Examples
print(unique_colors({"red", "blue"}, {"blue", "green"}))
# Output: {"red", "green"}

print(unique_colors({"purple", "yellow"}, {"yellow", "pink"}))
# Output: {"purple", "pink"}

print(unique_colors({"orange", "cyan"}, {"cyan", "magenta"}))
# Output: {"orange", "magenta"}
