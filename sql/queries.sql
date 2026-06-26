-- =====================================================
-- Query 1: Top 5 Funds by AUM
-- =====================================================

SELECT scheme_name, fund_house, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- =====================================================
-- Query 2: Average NAV per Month
-- =====================================================

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS average_nav
FROM nav_history
GROUP BY month
ORDER BY month;


-- =====================================================
-- Query 3: Total SIP Investment by Year
-- =====================================================

SELECT
strftime('%Y', transaction_date) AS year,
SUM(amount_inr) AS total_sip_amount
FROM investor_transactions
WHERE transaction_type='SIP'
GROUP BY year
ORDER BY year;


-- =====================================================
-- Query 4: Transactions by State
-- =====================================================

SELECT
state,
COUNT(*) AS total_transactions,
SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- =====================================================
-- Query 5: Funds with Expense Ratio below 1%
-- =====================================================

SELECT
scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- =====================================================
-- Query 6: Average 3-Year Return by Fund House
-- =====================================================

SELECT
fund_house,
AVG(return_3yr_pct) AS avg_return
FROM scheme_performance
GROUP BY fund_house
ORDER BY avg_return DESC;


-- =====================================================
-- Query 7: Number of Schemes in each Category
-- =====================================================

SELECT
category,
COUNT(*) AS total_schemes
FROM scheme_performance
GROUP BY category
ORDER BY total_schemes DESC;


-- =====================================================
-- Query 8: Average Transaction Amount by Payment Mode
-- =====================================================

SELECT
payment_mode,
AVG(amount_inr) AS avg_transaction
FROM investor_transactions
GROUP BY payment_mode;


-- =====================================================
-- Query 9: Highest NAV Recorded for each Fund
-- =====================================================

SELECT
amfi_code,
MAX(nav) AS highest_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY highest_nav DESC;


-- =====================================================
-- Query 10: Number of Investors by KYC Status
-- =====================================================

SELECT
kyc_status,
COUNT(*) AS investors
FROM investor_transactions
GROUP BY kyc_status;