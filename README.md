# agent-portfolio
A project used to learn AI Agent

## 学习阶段 0：Python 基础复习

涵盖内容：
- 数据类型：`int`, `float`, `bool`, `str`, `list`, `tuple`, `dict`, `set`, `None`
- 控制流：`if / for / while / enumerate / range / comprehension`
- 函数：参数类型（位置参数、关键词参数、默认值、`*args`, `**kwargs`），返回值，类型注解
- 模块与包：`import / from ... import ... / __main__`
- 虚拟环境：`python -m venv .venv`，激活与依赖管理
- 常用内置：`len / sum / max / min / sorted / map / filter / any / all / zip`
- 文件操作：`pathlib.Path` 读写、编码
- 简单网络：`requests`（GET、超时、状态码、JSON）

## 练习脚本
目录：`scripts/`

1. `string_utils.py` 字符串处理
   - 归一化空白：`normalize_whitespace`
   - 词频统计：`word_frequencies`
   - 回文判断：`is_palindrome`
   - 直接运行会展示一个示例。
2. `file_demo.py` 文件读写
   - 如果文件不存在则创建并写入初始内容，然后追加一行
   - 再次运行会继续追加新行并打印所有内容
3. `http_demo.py` 简单网络请求
   - 调用 JSONPlaceholder 公共测试接口，获取一个 TODO 项并打印字段

## 安装依赖

```bash
# 在仓库根目录（已创建虚拟环境）
D:/projects/Github/agent-portfolio/.venv/Scripts/python.exe -m pip install -U pip
D:/projects/Github/agent-portfolio/.venv/Scripts/python.exe -m pip install -r requirements.txt
```

## 运行示例

```bash
# 字符串处理演示
d:/projects/Github/agent-portfolio/.venv/Scripts/python.exe scripts/string_utils.py

# 文件读写（多次运行可看到行数增加）
d:/projects/Github/agent-portfolio/.venv/Scripts/python.exe scripts/file_demo.py

# 简单 GET 请求
d:/projects/Github/agent-portfolio/.venv/Scripts/python.exe scripts/http_demo.py
```

## 测试（pytest）

```bash
# 运行全部测试
D:/projects/Github/agent-portfolio/.venv/Scripts/python.exe -m pytest -q

# 运行单个测试文件
D:/projects/Github/agent-portfolio/.venv/Scripts/python.exe -m pytest tests/test_string_utils.py -q

# 运行指定测试用例
D:/projects/Github/agent-portfolio/.venv/Scripts/python.exe -m pytest tests/test_string_utils.py::test_is_palindrome -q
```

测试覆盖内容：
- 字符串工具函数（含 possessive 归一化）
- 文件脚本多次运行行为
- HTTP 脚本通过 mock 避免真实网络依赖

## 下一步计划（可迭代）
- 添加基础单元测试（pytest） ✅ 已完成
- 引入日志与配置管理
- 学习异步：`asyncio`、`httpx`
- 初步封装一个最小 Agent 结构（Prompt 模板 / 工具函数 / 记忆存储）

欢迎根据需要调整学习顺序。
