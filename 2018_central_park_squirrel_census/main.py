import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = squirrel_data[squirrel_data["Primary_Fur_Color"] == "Gray"]
cinnamon_squirrels = squirrel_data[squirrel_data["Primary_Fur_Color"] == "Cinnamon"]
black_squirrels = squirrel_data[squirrel_data["Primary_Fur_Color"] == "Black"]

gray_squirrels_count = len(squirrel_data[squirrel_data["Primary_Fur_Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary_Fur_Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary_Fur_Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

data = pd.DataFrame(data_dict)
data.to_csv("squirrels_count.csv")
