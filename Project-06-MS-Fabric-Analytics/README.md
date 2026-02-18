# Project 6: Enterprise Data Factory (Microsoft Fabric) 💎
> **Category:** Data Engineering / Unified Analytics

## 💼 Business Use Case
Enterprise data is often fragmented across SQL databases, CRM exports, and local spreadsheets, making real-time AI reporting impossible. This project demonstrates how to unify these silos using **Microsoft Fabric**. By centralizing data in **OneLake**, we eliminate the need for expensive ETL (Extract, Transform, Load) processes and prepare the data for AI-driven insights via PowerBI.

## 🛠️ Tech Stack
- **Platform:** Microsoft Fabric
- **Storage:** OneLake (Delta Lake format)
- **Ingestion:** Data Factory (Pipelines)
- **Transformation:** Spark Notebooks (PySpark)
- **BI:** PowerBI (Direct Lake Mode)

## 🏗️ Technical Architecture
1. **Bronze Layer:** Raw data ingestion from various sources into OneLake.
2. **Silver Layer:** Using PySpark to clean data, handle null values, and standardize date formats.
3. **Gold Layer:** Creating business-ready tables (Star Schema) that PowerBI can query instantly without data movement (Direct Lake).

## 🎯 Consultant's Strategic Impact
- **Zero-Copy Architecture:** Data stays in one place, reducing storage costs and security risks.
- **AI Readiness:** Grounding LLMs or Fabric Copilot in a clean, unified data source.
- **Executive Visibility:** Real-time dashboards that update the moment data hits the Lake.
