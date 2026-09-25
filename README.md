# Region Performance

**Track:** Data Analytics — Veda Technology Internship
**Task:** Compare sales across regions
**Objective:** Practice grouping and comparison
**Tools:** Excel (SUMIF / COUNTIF / RANK) and Python (pandas, matplotlib) — Power BI-style grouped comparison
**Dataset:** Superstore sales dataset (9,994 orders, 4 regions)

## What's in this repo

| File | Description |
|---|---|
| `Region_Performance.xlsx` | `Sales_Data` sheet (raw Region/Sales/Profit) and `Summary` sheet (SUMIF/COUNTIF region summary, RANK by Sales, manual cross-check, native bar chart) |
| `region_performance.py` | Python script — reproduces the same regional aggregation with pandas and plots the comparison with matplotlib |
| `region_summary.csv` | Output of the Python script — one row per region |
| `region_performance_chart.png` | Sales vs Profit bar chart (also embedded in the PDF report) |
| `Region_Performance_Report.pdf` | Project report: approach, region summary table, chart, key insights, interview-question notes |

## Approach

1. Grouped every order by `Region` (South, West, Central, East).
2. Computed, per region: Total Sales, Total Profit, Profit Margin % (Profit ÷ Sales), and line-item count.
   - **Excel:** `SUMIF` for totals, `COUNTIF` for line items, `RANK` for ordering.
   - **Python:** `df.groupby('Region').agg(...)`.
3. Ranked regions two ways — by Sales and by Profit Margin — to see whether the two rankings agree.
4. Cross-checked the four regional totals against the dataset's grand total (Excel `SUM` formula) — difference = $0.00.
5. Plotted Sales vs Profit side by side as a grouped bar chart (Excel native chart + matplotlib PNG).

## Key results

- **West** is the top region on every measure: highest Sales ($725,457.82), highest Profit ($108,418.45), best Profit Margin (14.94%).
- **Central** sells more than **South** ($501,239.89 vs $391,721.91) but is the *least* profitable region (7.92% margin vs South's 11.93%) — Sales rank and Profit-Margin rank disagree for these two regions.
- **East** is a consistent #2 across Sales, Profit, and Margin.

## How to run the Python version

```bash
pip install pandas matplotlib
python region_performance.py
```

Requires `superstore.csv` (Superstore dataset) in the same folder.
