🇮🇪 Irish Retail Market Simulator: End-to-End Data & AI Pipeline

📌 Executive Summary
This project is a high-fidelity simulation of the Irish Retail Landscape, specifically focusing on the hubs of Dublin, Cork, and Galway.

Faced with the lack of granular, public regional data, I engineered a Synthetic Data Engine using Python to generate over 50,000 transaction records. This pipeline transitions from raw data generation to a highly optimized Star Schema architecture, culminating in an executive-level Power BI Dashboard designed for ROI-driven decision-making.

🚀 Business Value & Impact
40% Reduction in Manual Data Prep: Automation of the ETL process using Python scripts.

Regional Granularity: Simulated market penetration and customer behavior across Ireland’s key economic counties.

Executive UX: Implemented the Z-Pattern design and Off-Black typography to minimize cognitive load for stakeholders.

🛠️ The Tech Stack
1. Data Engineering (Python/Pandas/NumPy)
Synthetic Engine: Built a custom logic to simulate realistic sales trends, seasonality, and customer demographics.
<p align="center">
  <img height="400" alt="Python Script Snippet" src="https://github.com/user-attachments/assets/42cd22a1-548b-4043-8816-33206b045925" />
</p>

ETL Pipeline: Automated cleaning and transformation of raw CSVs into structured relational tables.

2. Data Modeling (SQL / Power BI)
Star Schema Optimization: Developed a robust 1:N relationship model between Fact tables (Sales) and Dimensions (Calendar, Product, Geography, Customer).

Advanced DAX: Created complex measures for YTD (Year-to-Date), Growth WoW/MoM, and Customer Lifetime Value (CLV).

3. Advanced UI/UX Features
Report-Page Tooltips: Interactive hover-over insights for individual Irish counties (Dublin, Cork, Galway).

Drill-through Actions: Allows stakeholders to navigate from high-level KPIs to granular transactional data seamlessly.

📊 Dashboard Preview

<p align="center">
  <img height="350" alt="Dashboard Preview 1" src="https://github.com/user-attachments/assets/d16b213c-78de-4dd9-9a81-9147d32098da" />
  <img height="350" alt="Dashboard Preview 2" src="https://github.com/user-attachments/assets/bd62ca3c-88c2-48b4-971c-1dd009a62917" />
</p>

   * 👉 **[Click Here to Open the Live Interactive Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZDJkYjJkYmYtMGY2ZS00YzZhLWEwMzAtMmRlN2Y5YzY4MThhIiwidCI6IjUxYmEzOWRiLWRkYjAtNDQ3YS04MTU0LTgzNGEwYTZmZDJlOCJ9)**

🏗️ Data Architecture (The "Star Schema")
The model was designed for performance and scalability, following industry best practices:

Fact_Sales: ~50,000 rows of transactional data.

Dim_Geography: Mapped to Ireland's regional NUTS-3 classification.

Dim_Product: Categorized by retail sectors (Clothing, Groceries, Electronics).

👨‍💻 About the Author
Mateus - Business & Data Analyst

Focus: Data Engineering, BI, and AI Process Automation.

Education: Bachelor of Business Administration (NFQ Level 8 equivalent).

Status: Ready to relocate to Ireland (Dublin/Cork/Galway/Limerick) under the Critical Skills Employment Permit (CSEP).






