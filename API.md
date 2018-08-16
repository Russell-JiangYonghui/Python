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





### 3 错误码

> 150000-150499

| 错误码    | 错误描述      |
| ------ | --------- |
| 150001 | page未在范围内 |

### 4 api详情

#### ListAgent

> Request

```json
{
  "cmd":"ListAgent",
  "request_id":"xxxxx",
  "body":"",
  "page":1,
  "page_size":10,
  "region_int_id":1,
  "vm_str_id":001-0001-10_1_0_135
}
```

+ parameters

| 字段名称          | 类型     | 必须   | 描述                                  |
| ------------- | ------ | ---- | ----------------------------------- |
| page          | int    | 是    | 查询数据开始页码                            |
| page_size     | int    | 是    | 每页最大条目数                             |
| region_int_id | int    | 否    | 选择机房时显示该机房下Agent信息，不选择机房时所有Agent都显示 |
| vm_str_id     | string | 否    | 搜索时模糊匹配筛选显示Agent信息，不搜索时不做筛选         |

> Response

```json
{
 	"code":0,
 	"request_id":"xxxxx",
 	"trace_id": "xxxx",
 	"code_msg":"",
 	"body":[{
 		"agent_id":"001-0001-10-1-0-1",
 		"status":"存活（异常）",
		"private_ip":"10.1.0.135",
      	"region_int_id":1
  	}],
  	"count":2
}
```

| 字段名称          | 类型     | 描述                       |
| ------------- | ------ | ------------------------ |
| agent_id      | string | Agent的ID号，有vm-hostname决定 |
| status        | int    | Agent当前的状态，存活异常          |
| private_ip    | string | Agent的私有ip地址             |
| region_int_id | int    | Agent所在机房信息根据其来查找显示      |

#### ListHub

> Request

```json
{
  "cmd":"ListHub",
  "request_id":"xxxxx",
  "body":"",
  "page":1,
  "page_size":10，
  "region_int_id":1,
  "hub_id":"0001"
}
```

+ parameters

| 字段名称          | 类型     | 必须   | 描述                              |
| ------------- | ------ | ---- | ------------------------------- |
| page          | int    | 是    | 查询数据开始页码                        |
| page_size     | int    | 是    | 每页最大条目数                         |
| region_int_id | int    | 否    | 选择机房时显示该机房下Hub信息，不选择机房时所有Hub都显示 |
| hub_id        | string | 否    | 搜索时模糊匹配筛选显示Hub信息，不搜索时不做筛选       |

> Response

```json
{
 	"code":0,
 	"request_id":"xxxxx",
 	"trace_id": "xxxx",
 	"code_msg":"",
 	"body":[{
 		"hub_id":"0001",
 		"status":"存活（异常）"，
      	"region_int_id":1
  	}],
  	"count":2
}
```

| 字段名称          | 类型     | 描述                |
| ------------- | ------ | ----------------- |
| hub_id        | string | Hub的ID，由所处的网段决定   |
| status        | int    | Hub当前的状态，存活/异常    |
| region_int_id | int    | Hub所在机房信息根据其来查找显示 |

#### ListRegion

> Request 

```json
{
  "cmd":"ListRegion",
  "request_id":"xxxxx",
  "body":"",
}
```

> Response

```json
{
 	"code":0,
 	"request_id":"xxxxx",
 	"trace_id": "xxxx",
 	"code_msg":"",
 	"body":[{
 		"region_int_id":1,
 		"region_str_id":"aliyun"
  	}],
  	"count":2
}
```

| 字段名称          | 类型     | 描述                |
| ------------- | ------ | ----------------- |
| region_int_id | int    | Region的ID，由机房名称决定 |
| region_str_id | string | 机房名称，例如aliyun     |

