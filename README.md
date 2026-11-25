# test-repo

临时测试仓库：用于 Git / GitHub 提交流程、`gh` CLI 认证切换、CI 接入等场景的验证，不含业务代码。

## 内容

| 文件 | 说明 |
| --- | --- |
| `sample.py` | 示例模块，含 `add` / `divide` / `is_palindrome` 三个纯函数 |
| `test_sample.py` | 单元测试，标准库 `unittest`，无第三方依赖 |
| `.gitignore` | Python 项目常用忽略规则 |

## 环境

- Python 3.8+（本机已用 3.8.10 实测通过）
- 无第三方依赖，不需要 `pip install`

## 运行

跑全部单元测试：

```bash
python -m unittest -v
```

只跑单个测试文件：

```bash
python -m unittest test_sample -v
```

直接运行模块看示例输出：

```bash
python sample.py
```

预期输出：

```
add(2, 3) = 5
divide(10, 4) = 2.5
is_palindrome('A man, a plan, a canal: Panama') = True
```

## 测试覆盖

13 个用例，全部通过：

- `add`：整数、负数、浮点精度、零值
- `divide`：整除、循环小数、除零异常、负除数
- `is_palindrome`：整句回文、单词回文、空串、非回文、大小写与符号忽略

## 提交记录约定

该仓库仅作流程验证，提交信息用 `test:` 前缀。
