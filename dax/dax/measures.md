DAX measures used in the Power BI dashboard.


## GDP Growth YoY (%)

```DAX
GDP Growth YoY (%) =
VAR CurrentYear = MAX(gdp_powerbi[Year])
VAR PreviousYearGDP =
    CALCULATE(
        SUM(gdp_powerbi[GDP_USD_Millions]),
        FILTER(
            ALL(gdp_powerbi),
            gdp_powerbi[Year] = CurrentYear - 1
        )
    )
RETURN
DIVIDE(
    SUM(gdp_powerbi[GDP_USD_Millions]) - PreviousYearGDP,
    PreviousYearGDP
)
Economic Trend =
VAR AvgGrowth = [Average GDP Growth (%)]
RETURN
IF(
    AvgGrowth > 0,
    "Expansion",
    "Contraction"
)
