# 秒账 PRD 共享前置上下文

凡执行秒账 PRD 生成相关 skill（`search-history-docs`、`generate-final-prd`、`refine-prd-detail`），必须先读取以下文件：

## 必读规则
- @.cursor/rules/miaozhang-prd-global.md
- @.cursor/rules/miaozhang-product-knowledge.md

## 必读数据（L2 — 秒账 ERP 系统内）
- @data/modules/秒账核心功能.md — 全局能力校验清单（L2a）
- @data/modules/秒账功能关联关系.md — 主功能关联展开与补漏规则（L2b）

## 跨系统知识（L0/L2c — 涉及云仓/WMS/BSS 时必读）

**触发条件**（满足任一即视为跨系统需求）：需求或影响模块涉及 `[ERP]云仓出/入库单`、云仓库存/费用、货主/签约/月账单/账期、WMS 作业、运营系统/BSS、或 `秒账功能关联关系.md` 全局补漏提示需查 WMS/BSS。

**L0 上下文（先定边界，再展开关联）**
- @data/modules/系统定位-三系统.md — 主系统判定、生命周期、端能力
- @data/modules/_模块词典.md — 三系统模块规范名；影响模块输出不得自造别名
- @data/modules/用户角色-三系统.md — 用户/角色与端（按需）
- @data/modules/用户场景矩阵.md — 场景 ID 与 CS 映射（按需）

**L2c 跨系统关联（与 L2b 叠加，不替代）**
- @data/modules/跨系统功能关联关系.md — ERP↔WMS↔BSS 触发条件与关联规则（CS-01～CS-18）

**证据下钻（规则细节不明时）**
- @data/modules/_跨系统语料索引.md — 本地 PRD / MCP `user-wmsfileserver` 优先阅读清单

纯 ERP、无云仓货主、不涉及 WMS/BSS 的需求：**不读**本节，仅用 L2a+L2b。

## 可选深度资料（L3，按需读取）
- @data/modules/员工权限.md
- @data/modules/20220816智能记录更新.md
- @data/modules/0701上次单价记录规则.md
- 用户或核心功能条目中引用的其他模块文档

## 共享约定
- MCP 检索规则：@skills/_shared/mcp-retrieval.md
- 输出路径与命名：@skills/_shared/output-convention.md

## 权威来源优先级
1. 用户当前对话中已确认的需求、边界、规则
2. **跨系统**：`跨系统功能关联关系.md` + `系统定位-三系统.md`（命中 L0/L2c 触发时）
3. `秒账功能关联关系.md`（ERP 系统内关联展开 + 补漏规则）
4. `秒账核心功能.md`（全局能力校验清单）
5. 本地历史 PRD（`data/prd/*/*.md`；跨系统优先见 `_跨系统语料索引.md` P0）
6. MCP：`user-mzfileserver`（秒账）；跨系统/WMS/BSS 用 `user-wmsfileserver`（见 @skills/_shared/mcp-retrieval.md）
7. L3 模块知识卡片 / 独立规则文档

冲突时：优先采用更接近当前版本、当前业务形态、当前需求场景的内容；仍无法判断时标记为 `待确认项`。
