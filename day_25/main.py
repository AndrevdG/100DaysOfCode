import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# Get the unique fur colors (drop n.a. records)
fur_colors = data['Primary Fur Color'].dropna().unique()

# translate some colors for english people
color_translation = {
    "gray": "grey",
    "cinnamon": "red",
}

color_export = []

for color in fur_colors:
    total = len(data[data['Primary Fur Color'] == color])
    color = color.lower()
    if color in color_translation.keys():
        color_name = color_translation[color]
    else:
        color_name = color
    color_export.append(
        {
            "Fur Color": color_name,
            "Count": total
        }
    )

export = pandas.DataFrame(color_export)
export.to_csv("./squirrel_count.cvs")
