## bc(基础组件,Basic components)

[TOC]

> Api Url:https://localhost:8080/api/xxxxxxxxxxxxxxxxx

### 1 页面url划分

| url   | mark       |
| ----- | ---------- |
| #/admin | Administrator操作页 |
| #/fm  | FundManager操作页   |
| #/report  | Report操作页
| #/portfolio  | Portfolio操作页   |
| #/position  | Position操作页   |
| #/price  | Price操作页   |
| #/rate  | Rate操作页   |

### 2 api列表

| 接口名        | 接口描述                    | 参数   |
| :--------- | ----------------------- | ---- |
| createAdmin  | [创建新的Admin](#createAdmin) | soeid,name |
| copyPortfolio    | [Copy一个portfolio到另外一个fundManger](#copyPortfolio)     | portfolioID,fundManagerID |
| createFundManager | [创建新的FundManager](#createFundManager) | soeid,name |
| updateFundManager | [更新FundManager](#updateFundManager) | soeid,name |
| deleteFundManager | [删除FundManager](#deleteFundManager) | soeid,name  |
| deleteFundManagers | [删除多个FundManager](#deleteFundManagers) | fundManagerIDList |
| queryFundManager | [查询某个FundManager](#queryFundManager) | soeid |
| getBestFundManager | [获取最好的FundManager](#getBestFundManager) | / |
| getBestPorfolio | [获取最好的Portfolio](#getBestPorfolio) | / |
| queryPortfolioById | [查询某个Portfolio](#queryPortfolioById) | id |
| queryPortfolio | [查询某个FundManager下的所有Porfolio](#queryPortfolio) | fund_manager_id |
| queryPortfolioAll | [查询所有Portfolio](#queryPortfolioAll) | / |
| deletePortfolio | [删除某个Portfolio](#deletePortfolio) | portfolio_id |
| updatePortfolio |[更新某个Portfolio](#updatePortfolio) | id,name,fund_manager_id,cash |
| deletePortfolios | [删除多个 Portfolio](#deletePortfolios) | ids |
| createPortfolio |[创建Portfolio](#createPortfolio) |name,fund_manager_id,cash |
| queryPositionById |[查询Position](#queryPositionById) | id |
| queryPosition |[查询某个Portfolio的所有Position](#queryPosition) | portfolio_id |
| queryPositionAll |[查询所有Position](#queryPositionAll) | / |
| deletePosition |[删除Position](#deletePosition) | position_id |
| deletePositions |[删除多个Position](#deletePositions) | ids |
| updatePosition |[更新Position](#updatePosition) | id,symbol,quantity ,price,portfolio_id,base_currency,term_currency,date |
| createPosition |[创建Position](#createPosition) | symbol,quantity ,portfolio_id,term_currency,base_currency,date |
| createPricesData |[创建Price](#createPricesData) | symbol,date,price,base_currency |
| queryPricesDataAll |[查询所有Price](#queryPricesDataAll) | / |
| queryPricesDataBySymbolAndDateAndBase |[通过Symbol,Date,Base_currency查询Price](#queryPricesDataBySymbolAndDateAndBase) | symbol,date,base_currency |
| deletePricesDataBySymbol |[通过symbol删除Price](#deletePricesDataBySymbol) | symbol |
| deletePricesDataBySymbols |[通过Symbol删除多个Price](#deletePricesDataBySymbols) | symbols |
| updatePricesData |[更新Price](#updatePricesData) | symbol,date,price,base_currency |
| createRate |[创建Rate](#createRate) | TC, rate,date,BC |
| queryRatesDataAll |[查询所有Rate](#getRatesDataAll) | /|
| queryRatesDataByTCBCDate |[根据Term_currency,Base_currency,Date查询Rate](#getRatesDataByTCBCDate) | TC, BC, date|
| deleteRatesDataByTC |[根据Term_currency删除Rate](#deleteRatesDataByTC) | TC|
| deleteMultiRatesDataByTCs |[通过Term_currency删除Rate](#deleteMultiRatesDataByTCs) | TCs|
| updateRatesData |[更新Rate](#updateRatesData) | TC, rate, date, BC|

