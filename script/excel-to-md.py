import pandas as pd
import os

def excel_to_markdown(
    excel_path: str,
    md_path: str = None,
    sheet_name: str = 0,
    index: bool = False
) -> str:
    """
    将 Excel 文件转换为 Markdown 表格
    
    参数:
        excel_path: Excel文件路径
        md_path: 输出的Markdown文件路径，若为None则仅返回字符串不保存
        sheet_name: 要转换的工作表名称/索引，默认第一个工作表
        index: 是否包含DataFrame的索引列，默认不包含
    
    返回:
        转换后的Markdown格式字符串
    """
    # 检查文件是否存在
    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"Excel文件不存在: {excel_path}")
    
    # 读取Excel文件
    try:
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
    except Exception as e:
        raise ValueError(f"读取Excel文件失败: {str(e)}")
    
    # 处理空数据
    if df.empty:
        raise ValueError("读取的工作表为空")
    
    # 转换为Markdown表格
    # 第一步：生成表头
    headers = list(df.columns)
    if index:
        headers = [df.index.name or "Index"] + headers
    
    # 第二步：生成表头分隔线
    separator = ["---"] * len(headers)
    
    # 第三步：生成数据行
    rows = []
    if index:
        data = df.reset_index().values.tolist()
    else:
        data = df.values.tolist()
    
    for row in data:
        # 处理空值和特殊类型
        formatted_row = []
        for cell in row:
            if pd.isna(cell):
                formatted_row.append("")
            else:
                # 转换为字符串，处理数字格式
                formatted_row.append(str(cell))
        rows.append(formatted_row)
    
    # 组装Markdown表格
    md_lines = []
    # 添加表头
    md_lines.append(f"| {' | '.join(headers)} |")
    # 添加分隔线
    md_lines.append(f"| {' | '.join(separator)} |")
    # 添加数据行
    for row in rows:
        md_lines.append(f"| {' | '.join(row)} |")
    
    # 合并为完整的Markdown字符串
    md_content = "\n".join(md_lines)
    
    # 保存到文件（如果指定了路径）
    if md_path:
        # 创建输出目录（如果不存在）
        output_dir = os.path.dirname(md_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
    
    return md_content

# 示例使用
if __name__ == "__main__":
    # 配置参数
    EXCEL_FILE = "D:\Cursor\data\map\模块费用.xlsx"  # 你的Excel文件路径
    MD_FILE = "D:\Cursor\data\map\模块费用.md"     # 输出的Markdown文件路径
    
    try:
        # 转换Excel到Markdown
        md_content = excel_to_markdown(
            excel_path=EXCEL_FILE,
            md_path=MD_FILE,
            sheet_name=0,  # 0表示第一个工作表，也可以指定工作表名称如"Sheet1"
            index=False    # 不显示索引列
        )
        
        # 打印转换结果
        print("转换成功！Markdown内容：")
        print("-" * 50)
        print(md_content)
        print("-" * 50)
        print(f"文件已保存到: {os.path.abspath(MD_FILE)}")
        
    except Exception as e:
        print(f"转换失败: {str(e)}")