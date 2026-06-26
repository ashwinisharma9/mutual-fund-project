# Mutual Fund Data Dictionary

## Overview

This document describes the datasets used in the Bluestock Mutual Fund Analytics Capstone Project. It includes column definitions, data types, and business meanings.

---

## 1. fund_master

| Column             | Description                    |
| ------------------ | ------------------------------ |
| amfi_code          | Unique AMFI scheme code        |
| fund_house         | Mutual fund company            |
| scheme_name        | Name of the mutual fund scheme |
| category           | Fund category                  |
| sub_category       | Fund sub-category              |
| plan               | Direct or Regular plan         |
| launch_date        | Scheme launch date             |
| benchmark          | Benchmark index                |
| expense_ratio_pct  | Expense ratio (%)              |
| exit_load_pct      | Exit load (%)                  |
| min_sip_amount     | Minimum SIP investment         |
| min_lumpsum_amount | Minimum lump sum investment    |
| fund_manager       | Fund manager name              |
| risk_category      | Risk level                     |
| sebi_category_code | SEBI category code             |

---

## 2. nav_history

| Column    | Description     |
| --------- | --------------- |
| amfi_code | Scheme code     |
| date      | NAV date        |
| nav       | Net Asset Value |

---

## 3. aum_by_fund_house

Contains Assets Under Management (AUM) grouped by fund house.

---

## 4. monthly_sip_inflows

Contains monthly SIP inflow values.

---

## 5. category_inflows

Contains category-wise mutual fund inflows.

---

## 6. industry_folio_count

Contains folio count statistics across the industry.

---

## 7. scheme_performance

Contains performance metrics such as returns, AUM, alpha, beta, Sharpe ratio, Sortino ratio, expense ratio, and risk grade.

---

## 8. investor_transactions

Contains investor transaction details including transaction type, investment amount, state, payment mode, and KYC status.

---

## 9. portfolio_holdings

Contains portfolio holdings for each mutual fund scheme.

---

## 10. benchmark_indices

Contains historical benchmark index values.

---

## Data Source

Bluestock Mutual Fund Analytics Capstone Dataset

## Database

SQLite Database: `bluestock_mf.db`
