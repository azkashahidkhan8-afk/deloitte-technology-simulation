# Deloitte Technology Job Simulation - Data Transformation Engine

A data engineering and parsing solution completed as part of the **Deloitte Technology Job Simulation** via Forage. This project showcases the ability to design data parsing pipelines, manage disparate telemetry inputs, and implement automated verification tests.

## 📋 Project Overview
Industrial devices generate logs in unpredictable layouts depending on firmware versions. This engine harmonizes incoming unstructured data formats into a uniform target schema optimized for downstream computational analysis and database warehousing.

### Key Implementation Capabilities:
* **Format-1 Parsing:** Deconstructed structured path strings via slice mapping logic.
* **Format-2 Parsing:** Normalised ISO-8601 string-based timestamps into absolute system milliseconds.
* **Algorithmic Routing:** Configured dynamic routing using safe class getters (`.get()`) to identify data payloads dynamically without running into system KeyErrors.
* **Automated Quality Checks:** Implemented regression unit test assertions (`unittest`) to guarantee data integrity across diverse pipelines.

## 🚀 Execution & Testing
To spin up the script and run the integrated test framework locally, execute the following command in your terminal:

```bash
python main.py
```

## 📜 Verification & Credentials
* **Issued By:** Deloitte (via Forage)
* **Recipient:** Azka Shahid Khan
* **Completion Date:** October 23, 2026
* **Verification Code:** 6adb31c2d4a81158c3a93e98
