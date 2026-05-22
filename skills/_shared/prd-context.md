# 秒账 PRD 共享前置上下文

凡执行秒账 PRD 生成相关 skill（`search-history-docs`、`generate-final-prd`、`refine-prd-detail`），必须先读取以下文件：

## 必读规则
- @.cursor/rules/miaozhang-prd-global.mdc
- @.cursor/rules/miaozhang-product-knowledge.mdc

## 必读数据
- @data/modules/秒账新功能影响模块模板.md

## 共享约定
- MCP 检索规则：@skills/_shared/mcp-retrieval.md
- 输出路径与命名：@skills/_shared/output-convention.md

## 权威来源优先级
1. 用户当前对话中已确认的需求、边界、规则
2. `秒账新功能影响模块模板.md`（影响模块关联补漏）
3. 本地历史 PRD（`data/prd/*/*.md`）
4. MCP `user-mzfileserver` 历史记录
5. `data/modules/功能.md`（联动索引，非完整模块定义）

冲突时：优先采用更接近当前版本、当前业务形态、当前需求场景的内容；仍无法判断时标记为 `待确认项`。
