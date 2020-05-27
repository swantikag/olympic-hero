# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={"Total":"Total_Medals"}, inplace = True)
data.head()



# --------------
#Code starts here
data["Better_Event"]=np.where(data["Total_Summer"]==data["Total_Winter"],"Both",
np.where(data["Total_Summer"]>data["Total_Winter"], "Summer", "Winter"))
better_event = data["Better_Event"].value_counts().argmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[["Country_Name","Total_Summer","Total_Winter", "Total_Medals"]]
top_countries.drop(top_countries.tail(1).index,inplace=True)
def top_ten(df, col):
    country_list = []
    country_list = list((df.nlargest(10,col)["Country_Name"]))
    return country_list
top_10_summer = top_ten(top_countries, "Total_Summer")
top_10_winter = top_ten(top_countries, "Total_Winter") 
top_10 = top_ten(top_countries, "Total_Medals")
common = list(set(top_10_summer).intersection(set(top_10_winter).intersection(set(top_10))))
print(common)


# --------------
#Code starts here
summer_df = data[data["Country_Name"].isin(top_10_summer)]
winter_df = data[data["Country_Name"].isin(top_10_winter)]
top_df = data[data["Country_Name"].isin(top_10)]
summer_df.plot.bar()


# --------------
#Code starts here
summer_df["Golden_Ratio"]=summer_df["Gold_Summer"]/summer_df["Total_Summer"]
im_table=(summer_df[summer_df["Golden_Ratio"]==summer_df["Golden_Ratio"].max()])[["Golden_Ratio","Country_Name"]]
summer_max_ratio = im_table["Golden_Ratio"].values[0].round(2)
summer_country_gold = im_table["Country_Name"].values[0]

winter_df["Golden_Ratio"]=winter_df["Gold_Winter"]/summer_df["Total_Winter"]
im_table=(winter_df[winter_df["Golden_Ratio"]==winter_df["Golden_Ratio"].max()])[["Golden_Ratio","Country_Name"]]
winter_max_ratio = im_table["Golden_Ratio"].values[0].round(2)
winter_country_gold=im_table["Country_Name"].values[0]

top_df["Golden_Ratio"]=winter_df["Gold_Total"]/summer_df["Total_Medals"]
im_table=(top_df[top_df["Golden_Ratio"]==top_df["Golden_Ratio"].max()])[["Golden_Ratio","Country_Name"]]
top_max_ratio = im_table["Golden_Ratio"].values[0].round(2)
top_country_gold="China"
# im_table["Country_Name"].values[0]


# --------------
#Code starts here
data_1 = data[:-1]
data_1["Total_Points"] = data_1["Gold_Total"]*3 + data_1["Silver_Total"]*2 + data_1["Bronze_Total"]*1
most_points = data_1["Total_Points"].max()
best_country = data_1.loc[data_1["Total_Points"].idxmax(),"Country_Name"]


# --------------
#Code starts here
best = data.loc[data["Country_Name"]==best_country,:]
best = best[["Gold_Total","Silver_Total","Bronze_Total"]]
best.plot.bar(stacked=True)
plt.xlabel("United States")
plt.ylabel("Medal Tally")
plt.xticks(rotation=45)


