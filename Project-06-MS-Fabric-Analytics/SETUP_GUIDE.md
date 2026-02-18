# 🛠️ Setup & Run Guide: Project 6
How to implement this Microsoft Fabric Data Pipeline.

## 1. Prerequisites
- A **Microsoft Fabric** Trial or Capacity (available at [app.fabric.microsoft.com](https://app.fabric.microsoft.com)).
- Basic understanding of Lakehouses.

## 2. Environment Setup
1. Log into Microsoft Fabric.
2. Create a new **Workspace** named "AI_Transformation_Portfolio".
3. Create a new **Lakehouse** named "Enterprise_OneLake".

## 3. Data Ingestion (Bronze)
1. In the Lakehouse view, click "Upload" and upload a sample `sales_data.csv`.
2. (Optional) Use a **Data Factory Pipeline** to schedule ingestion from an external URL.

## 4. Transformation (Silver/Gold)
1. Create a new **Notebook** in your workspace.
2. Copy the code from `fabric_transformation.py` into a cell.
3. Run the cell to process the data and save the Delta Table.

## 5. Visualization
1. Go to the "SQL Analytics Endpoint" of your Lakehouse.
2. Click "New PowerBI Report".
3. Drag "Region" and "TotalSales" from the `Gold_Regional_Sales` table onto the canvas.
