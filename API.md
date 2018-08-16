## bc(Basic components)

[TOC]

> Api Url:https://localhost:8080/api/xxxxxxxxxxxxxxxxx

### 1 urls

| url   | mark       |
| ----- | ---------- |
| #/admin | Administrator pages |
| #/fm  | FundManager pages   |
| #/report  | Report pages
| #/portfolio  | Portfolio pages  |
| #/position  | Position pages   |
| #/price  | Price pages   |
| #/rate  | Rate pages   |

### 2 api list

| API Name   | API Des                   | Params  |
| :--------- | ----------------------- | ---- |
| createAdmin  | [create Admin](#createAdmin) | soeid,name |
| copyPortfolio    | [Copy a portfolio to  another fundManger](#copyPortfolio)     | portfolioID,fundManagerID |
| createFundManager | [create FundManager](#createFundManager) | soeid,name |
| updateFundManager | [update FundManager](#updateFundManager) | soeid,name |
| deleteFundManager | [delete FundManager](#deleteFundManager) | soeid,name  |
| deleteFundManagers | [delete multiple FundManager](#deleteFundManagers) | fundManagerIDList |
| queryFundManager | [query FundManager](#queryFundManager) | soeid |
| getBestFundManager | [get the best FundManager](#getBestFundManager) | / |
| getBestPorfolio | [get the best Portfolio](#getBestPorfolio) | / |
| queryPortfolioById | [query a Portfolio](#queryPortfolioById) | id |
| queryPortfolio | [query the Porfolio by FundManager](#queryPortfolio) | fund_manager_id |
| queryPortfolioAll | [query all Portfolio](#queryPortfolioAll) | / |
| deletePortfolio | [delete a Portfolio](#deletePortfolio) | portfolio_id |
| updatePortfolio |[update a Portfolio](#updatePortfolio) | id,name,fund_manager_id,cash |
| deletePortfolios | [delete multiple Portfolios](#deletePortfolios) | ids |
| createPortfolio |[create Portfolio](#createPortfolio) |name,fund_manager_id,cash |
| queryPositionById |[query a Position](#queryPositionById) | id |
| queryPosition |[query all Positions by Portfolio](#queryPosition) | portfolio_id |
| queryPositionAll |[query all Position](#queryPositionAll) | / |
| deletePosition |[delete a Position](#deletePosition) | position_id |
| deletePositions |[delete multiple Positions](#deletePositions) | ids |
| updatePosition |[update a Position](#updatePosition) | id,symbol,quantity ,price,portfolio_id,base_currency,term_currency,date |
| createPosition |[create a Position](#createPosition) | symbol,quantity ,portfolio_id,term_currency,base_currency,date |
| createPricesData |[create a Price](#createPricesData) | symbol,date,price,base_currency |
| queryPricesDataAll |[query all Prices](#queryPricesDataAll) | / |
| queryPricesDataBySymbolAndDateAndBase |[query price by Symbol,Date and Base_currency](#queryPricesDataBySymbolAndDateAndBase) | symbol,date,base_currency |
| deletePricesDataBySymbol |[delete Price by Symbol](#deletePricesDataBySymbol) | symbol |
| deletePricesDataBySymbols |[delete Prices by symbols](#deletePricesDataBySymbols) | symbols |
| updatePricesData |[update Price](#updatePricesData) | symbol,date,price,base_currency |
| createRate |[create a Rate](#createRate) | TC, rate,date,BC |
| queryRatesDataAll |[query all Rate](#getRatesDataAll) | /|
| queryRatesDataByTCBCDate |[query Rate by Term_currency,Base_currency and Date](#getRatesDataByTCBCDate) | TC, BC, date|
| deleteRatesDataByTC |[delete Rate by Term_currency](#deleteRatesDataByTC) | TC|
| deleteMultiRatesDataByTCs |[delete Rates by multiple Term_currencys](#deleteMultiRatesDataByTCs) | TCs|
| updateRatesData |[update Rate](#updateRatesData) | TC, rate, date, BC|

