import pandas as pd

data = pd.read_csv("it_assets.csv")

data["HealthScore"] = 100 - (
    data["CPU_Usage"] +
    data["Memory_Usage"] +
    data["Disk_Usage"]
) / 3

data["RiskScore"] = (
    data["Incidents_30d"] * 5 +
    data["Days_Since_Patch"]
)

important_assets = data[
    (data["Environment"] == "Prod") &
    (data["Criticality"] == "High")
]

important_assets = important_assets.sort_values(
    "RiskScore", ascending=False
)

print("\nTop High-Risk Production Assets:\n")
print(
    important_assets[
        ["AssetID", "AssetType", "HealthScore", "RiskScore"]
    ].head(5)
)

print("\nAverage Health Score:", round(data["HealthScore"].mean(), 2))
print("Average Risk Score:", round(data["RiskScore"].mean(), 2))
