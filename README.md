# Sales Dashboard Project

##  Overview
This project demonstrates an interactive **Sales Dashboard** built in **Power BI**.  
It provides key business insights through KPIs, trend analysis, customer segmentation, and cohort tracking.

---

##  Objectives
- Track overall sales performance.
- Monitor profitability and customer behavior.
- Identify customer segments using clustering.
- Enable dynamic filtering with slicers for deeper analysis.

---

##  Key Features
### 1. KPI Cards
- **Average Order Value (AOV)**  
- **Profit Margin (%)**  
- **Average Quantity per Order**

### 2. Trend Analysis
- Line chart showing **Average Order Value by Month/Year**.

### 3. Cohort Analysis
- Matrix heatmap showing **customer retention by cohort month**.

### 4. Customer Segmentation
- Scatter plot with **Amount vs Quantity**, color‑coded by **Segment** (K‑Means clustering).

### 5. Interactive Filters
- Slicers for **State**, **Category**, and **Payment Mode**.

---

##  Tools & Technologies
- **Power BI** for dashboard creation.  
- **Python (Pandas, Scikit‑Learn)** for data cleaning and clustering.  
- **Excel/CSV** for dataset storage.  

---

##  Dataset
- Source: `dashboard_data.csv`  
- Columns include: `order_id`, `amount`, `profit`, `quantity`, `state`, `category`, `paymentmode`, `Segment`, etc.  

---

##  Insights
- High‑value customers identified through segmentation.  
- Profit margin trends highlight seasonal variations.  
- Cohort analysis reveals retention patterns across months.  
- Slicers allow flexible exploration by geography, category, and payment type.  

---

##  How to Use
1. Open `Sales_Dashboard_Final.pbix` in Power BI Desktop.  
2. Explore KPI cards, charts, and slicers interactively.  
3. Apply filters to view insights for specific states, categories, or payment modes.  

---

##  Conclusion
This dashboard provides a **comprehensive view of sales performance** and helps in **data‑driven decision making**. It combines KPIs, trends, segmentation, and retention analysis into a single interactive report.
