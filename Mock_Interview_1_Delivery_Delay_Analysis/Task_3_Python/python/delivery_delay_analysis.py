# Delivery Delay Analysis - Task 3 

import pandas as pd
import matplotlib.pyplot as plt


# 1. Read CSV files
folder = __file__.replace("\\", "/").rsplit("/", 1)[0]

deliveries = pd.read_csv(folder + "/deliveries.csv")
routes = pd.read_csv(folder + "/routes.csv")


# 2. Convert days columns into numbers
deliveries["promised_days"] = pd.to_numeric(deliveries["promised_days"])
deliveries["actual_days"] = pd.to_numeric(deliveries["actual_days"])


# 3. Remove duplicate rows
deliveries = deliveries.drop_duplicates()


# 4. Combine both files using route_id
df = pd.merge(deliveries, routes, on="route_id")


# 5. Calculate delay
df["delay_days"] = df["actual_days"] - df["promised_days"]


# If delay is negative, make it 0
df["delay_days"] = df["delay_days"].apply(lambda x: 0 if x < 0 else x)


# 6. Service type summary
summary = df.groupby("service_type")["delay_days"].sum().reset_index()
summary.columns = ["service_type", "total_delay_days"]


# Count total records
records = df.groupby("service_type").size().reset_index(name="records")


# Count delayed records
delayed = df[df["actual_days"] > df["promised_days"]]
delayed_records = delayed.groupby("service_type").size().reset_index(name="delayed_records")


# Add the counts to summary
summary = pd.merge(summary, records, on="service_type")
summary = pd.merge(summary, delayed_records, on="service_type", how="left")


# Empty values become 0
summary["delayed_records"] = summary["delayed_records"].fillna(0)


# 7. Calculate delay percentage
summary["delay_incidence_rate"] = (
    summary["delayed_records"] / summary["records"] * 100
)


# 8. Find route with highest delay
route_delay = df.groupby(["route_id", "route"])["delay_days"].sum().reset_index()
route_delay = route_delay.sort_values("delay_days", ascending=False)

# No iloc used
top_route = route_delay.head(1)


# 9. Calculate total delay
overall_delay = df["delay_days"].sum()


# Calculate top route percentage
top_route_share = top_route["delay_days"].sum() / overall_delay * 100


# 10. Display results
print("Service Type Summary:")
print(summary)

print()
print("Route with greatest delay:")
print(top_route)

print()
print("Overall total delay days:", overall_delay)
print("Top route share:", round(top_route_share, 2), "%")


# 11. Monthly delay
monthly = df.groupby("month")["delay_days"].sum()

month_order = ["Jan", "Feb", "Mar"]
monthly = monthly.reindex(month_order)


# 12. Create bar chart
plt.figure(figsize=(7, 4))
plt.bar(monthly.index, monthly.values)

plt.title("Monthly Total Delay Days")
plt.xlabel("Month")
plt.ylabel("Total Delay Days")

plt.tight_layout()
plt.savefig(folder + "/python_chart.png")
plt.show()


# 13. Save output files
df.to_csv(folder + "/clean_data.csv", index=False)
summary.to_csv(folder + "/python_summary.csv", index=False)

print()
print("Files saved successfully.")
