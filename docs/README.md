# PPT转Markdown工具

这个工具可以将PowerPoint文件(.pptx)转换为Markdown格式文件。

## 功能特点

- 支持命令行参数
- 自动识别幻灯片标题和内容
- 生成标准Markdown格式
- 包含错误处理机制
- 支持中文内容

## 安装

### 方法1：从源码安装（推荐）

```bash
git clone https://github.com/bamboodew/ppt-to-md.git
cd ppt-to-md
pip install -e .
```

### 方法2：使用pip安装（需要先发布到PyPI）

```bash
# 注意：此方法目前不可用，因为包尚未发布到PyPI
# pip install ppt-to-md
```

## 使用方法

### 作为命令行工具使用

```bash
ppt-to-md input.pptx output.md
```

### 作为Python模块使用

```python
from src.ppt_to_md.main import ppt_to_md

ppt_to_md("input.pptx", "output.md")
```

### 参数说明

- `input.pptx`: 输入的PPT文件路径
- `output.md`: 输出的Markdown文件路径

## 示例

```bash
# 转换单个文件
ppt-to-md presentation.pptx presentation.md

# 查看帮助信息
ppt-to-md --help
```

## 项目结构

```text
ppt-to-md/                 # 项目根目录
├── .gitignore             # Git忽略文件
├── LICENSE                # 许可证文件
├── README.md             # 项目主说明文件
├── requirements.txt      # 依赖清单
├── setup.py              # 包安装配置文件
├── src/                  # 源代码目录
│   └── ppt_to_md/        # 主包目录
│       ├── __init__.py    # 包初始化文件
│       └── main.py       # 主程序文件
├── examples/             # 示例文件目录
│   ├── test.pptx         # 简单测试PPT文件
│   ├── demo.pptx         # 复杂演示PPT文件
│   ├── output.md         # 简单测试输出
│   ├── test_output.md    # 简单测试输出（新生成）
│   └── demo_output.md    # 复杂演示输出
├── docs/                # 文档目录
│   └── README.md        # 详细文档
└── tests/               # 测试目录
    ├── import_test.py   # 导入测试文件
    └── test_ppt_to_md.py # 单元测试文件
```

## 输出格式

生成的Markdown文件将按照以下格式组织：

```markdown
## 幻灯片 1

### 幻灯片标题

幻灯片内容...

## 幻灯片 2

### 幻灯片标题

幻灯片内容...
```

## 注意事项

1. 仅支持 .pptx 格式的文件，不支持旧版 .ppt 文件
2. 确保输入文件路径正确且文件存在
3. 输出文件将被覆盖如果已存在

## 开发

### 运行测试

```bash
python -m pytest tests/
```

### 贡献代码

欢迎提交Pull Request或报告Issue。
