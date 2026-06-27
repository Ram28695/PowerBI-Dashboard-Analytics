
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('Sales_Dataset_Cleaned.csv')


aov = df['amount'].sum() / df['order_id'].nunique()

profit_margin = (df['profit'].sum() / df['amount'].sum()) * 100

avg_quantity = df['quantity'].mean()

print(f"Average Order Value: {aov:.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Average Quantity per Order: {avg_quantity:.2f}")


df['OrderMonth'] = pd.to_datetime(df['order_date']).dt.to_period('M')
cohort = df.groupby(['customername'])['OrderMonth'].min()
df['CohortMonth'] = df['customername'].map(cohort)
cohort_data = df.groupby(['CohortMonth', 'OrderMonth']).agg({'customername':'nunique'}).reset_index()
cohort_pivot = cohort_data.pivot(index='CohortMonth', columns='OrderMonth', values='customername')
print(cohort_pivot)


stages = ['Visited', 'Added_to_Cart', 'Purchased']
counts = [5000, 2000, len(df)]  # last stage = total orders in dataset
funnel_df = pd.DataFrame({'Stage': stages, 'Count': counts})
funnel_df['DropOff_%'] = funnel_df['Count'].pct_change() * -100
print(funnel_df)


features = df[['amount', 'quantity']]
kmeans = KMeans(n_clusters=3, random_state=42)
df['Segment'] = kmeans.fit_predict(features)
print(df.groupby('Segment')[['amount','quantity']].mean())


df.to_csv("dashboard_data.csv", index=False)
