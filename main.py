import pandas as pd
import matplotlib.pyplot as plt

# Pandas operations

df= pd.read_csv("data/salesdaily.csv")

df["datum"]=pd.to_datetime(df["datum"])

drugs=["M01AB","M01AE","N02BA","N02BE","N05B","N05C","R03","R06"]

Drug_sales=df[drugs].sum() #1

print("\n 1. Drug sales: \n" )
print(Drug_sales)

max_sales=Drug_sales.sort_values(ascending=False) #2

Drug_sales.plot(kind="bar",title="Total Drug sales")
plt.xlabel("drugs")
plt.ylabel("Sales")
plt.savefig("plot2.png")
plt.show()


print(f"\n 2. Maximum total sales: \n {max_sales} \n")

monthly=df.groupby(["Year","Month"])[drugs].sum() #3

Jan_2015=monthly.loc[(2015,1)]
top_3_J2015=Jan_2015.sort_values(ascending=False).head(3)

monthly.loc[(2015,1)].plot(kind="bar",title="Drugs with highest sales in January 2015")
plt.ylabel("Sales")
plt.xlabel("drugs")
plt.savefig("plot3A.png")
plt.show()

July_2016=monthly.loc[(2016,7)]
top_3_JL2016=July_2016.sort_values(ascending=False).head(3)

monthly.loc[(2016,7)].plot(kind="bar",title="Drugs with highest sales in July 2016")
plt.ylabel("Sales")
plt.xlabel("drugs")
plt.savefig("plot3B.png")
plt.show()

Sept_2017=monthly.loc[(2017,9)]
top_3_S2017=Sept_2017.sort_values(ascending=False).head(3)

monthly.loc[(2017,9)].plot(kind="bar",title="Drugs with highest sales in September 2017")
plt.ylabel("Sales")
plt.xlabel("drugs")
plt.savefig("plot3C.png")
plt.show()

print("\n 3. Drug with highest sales in Jan 2015, July 2016 and Sept 2017: \n") 
print(f"A. \n {top_3_J2015} \n" )
print(f"B. \n  {top_3_JL2016} \n")
print(f"C. \n {top_3_S2017} \n")


df_2017=df[df["datum"].dt.year==2017] #4
peak_2017=df_2017.set_index("datum")[drugs].sum().idxmax()

df_2017.set_index("datum")[drugs].sum().plot(kind="bar",title="Drugs with highest sales in 2017")
plt.ylabel("Sales")
plt.xlabel("drugs")
plt.savefig("plot4.png")
plt.show()

print(f" 4. Most drug sales in 2017: \n {peak_2017} \n") 

daily=df.groupby(["datum"])[drugs].sum().mean() #5
daily_peak=daily.idxmax()

df.groupby(["datum"])[drugs].sum().mean().plot(kind="bar",title="Drugs with Highest Average daily sales")
plt.ylabel("sales")
plt.xlabel("drugs")
plt.savefig("plot5.png")
plt.show()


print(f"5. Highest average daily sales: \n {daily_peak} \n") 

R03_months=df.groupby(["Month"])["R03"].sum().sort_values(ascending=False).head(3) #6

df.groupby(["Month"])["R03"].sum().plot(kind="bar",title="Months with highest sales of R03")
plt.ylabel("Sales")
plt.xlabel("Month")
plt.savefig("plot6.png")
plt.show()

print(f"6. Months with highest sales of R03: \n \n {R03_months} \n ")








