import pandas as pd
data={
"Item":["Pizza","Burger","Fried rice","Parotta","Parotta","Pizza","Juice","Parotta","Briyani","Pizza","Fried rice","Briyani","Fried rice"],
"Location":["Chennai","Madurai","Trichy","Madurai","Karaikudi","Chennai","Coimbatore","Chennai","Madurai","Trichy","Karaikudi","Karaikudi","Coimbatore"],
"Time":["1 pm","2 pm","5 pm","7 pm","9 am","10 am","12 pm","7 pm","1 pm","4 pm","5 pm","1 pm","5 pm"]
}
df=pd.DataFrame(data)
Time_analyze=df.Time
print("Time_analyze\n",Time_analyze)
Item_order=df.Item
print("Item\n",Item_order)
Ordered_location=df.Location
print("Location\n",Ordered_location)

import pandas as pd
data={
"Item":["Pizza","Burger","Fried rice","Parotta","Parotta","Pizza","Juice","Parotta","Briyani","Pizza","Fried rice","Briyani","Fried rice"],
"Location":["Chennai","Madurai","Trichy","Madurai","Karaikudi","Chennai","Coimbatore","Chennai","Madurai","Trichy","Karaikudi","Karaikudi","Coimbatore"],
"Time":["1 pm","2 pm","5 pm","7 pm","9 am","10 am","12 pm","7 pm","1 pm","4 pm","5 pm","1 pm","5 pm"]

}
df=pd.DataFrame(data)
Peak_ordertime=df.Time.value_counts()
print(Peak_ordertime)

import pandas as pd
data={
"Item":["Pizza","Burger","Fried rice","Parotta","Parotta","Pizza","Juice","Parotta","Briyani","Pizza","Fried rice","Briyani","Fried rice"],
"Location":["Chennai","Madurai","Trichy","Madurai","Karaikudi","Chennai","Coimbatore","Chennai","Madurai","Trichy","Karaikudi","Karaikudi","Coimbatore"],
"Time":["1 pm","2 pm","5 pm","7 pm","9 am","10 am","12 pm","7 pm","1 pm","4 pm","5 pm","1 pm","5 pm"]

}
df=pd.DataFrame(data)
popular_dish=df["Item"].value_counts()
print("Popular dish", popular_dish)

import matplotlib.pyplot as plt
from collections import Counter

Item = ["Pizza","Burger","Fried rice","Parotta","Parotta","Pizza",
        "Juice","Parotta","Briyani","Pizza","Fried rice",
        "Briyani","Fried rice"]

Location = ["Chennai","Madurai","Trichy","Madurai","Karaikudi",
            "Chennai","Coimbatore","Chennai","Madurai",
            "Trichy","Karaikudi","Karaikudi","Coimbatore"]

# Bar Chart
plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
item_count = Counter(Item)
plt.bar(item_count.keys(), item_count.values(), color="green")
plt.title("Food Order Details")
plt.xlabel("Item")
plt.ylabel("Count")

# Line Chart
plt.subplot(1,3,2)
plt.plot(list(item_count.keys()),
         list(item_count.values()),
         color="green",
         linestyle="--",
         marker="o")
plt.title("Food Order Details")
plt.xlabel("Item")
plt.ylabel("Count")

# Pie Chart
plt.subplot(1,3,3)
plt.pie(item_count.values(),
        labels=item_count.keys(),
        autopct="%1.1f%%")
plt.title("Food Order Details")

plt.tight_layout()
plt.show()