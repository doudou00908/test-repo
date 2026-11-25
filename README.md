# test-repo

临时测试仓库：用于 Git / GitHub 提交流程、`gh` CLI 认证切换、CI 接入等场景的验证，不含业务代码。

## 内容

| 文件 | 说明 |
| --- | --- |
| `sample.py` | 示例模块，含 `add` / `divide` / `is_palindrome` 三个纯函数 |
| `test_sample.py` | 单元测试，标准库 `unittest`，无第三方依赖 |
| `.gitignore` | Python 项目常用忽略规则 |
| `.gitattributes` | 统一 LF 行尾 |

## 环境

- Python 3.8+（本机已用 3.8.10 实测通过）
- 无第三方依赖，不需要 `pip install`

## 运行

跑全部单元测试：

```bash
python -m unittest -v
```

只跑某个测试类：

```bash
python -m unittest test_sample.TestDivide -v
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

32 个用例方法（参数化处用 `subTest` 展开，实际断言数更多），全部通过。

| 测试类 | 用例数 | 覆盖点 |
| --- | --- | --- |
| `TestAdd` | 8 | 整数、负数、浮点精度、零值、`10**18` 级大整数、加 0 恒等、交换律、`bool` 按 `int` 处理 |
| `TestDivide` | 10 | 整除、循环小数、整数/浮点除零异常、负除数、零被除数、除数 1、乘除往返、`NaN` 传播、`Inf` 边界 |
| `TestPalindrome` | 11 | 整句回文、单词回文、空串、非回文、大小写与符号忽略、单字符、纯数字、中文回文、纯符号（清理后为空）、纯空白、混合大小写 |
| `TestConsistency` | 3 | `add` 减法往返、`divide` 乘法往返、`add` 结合律 |

## 提交记录约定

该仓库仅作流程验证，提交信息用 `test:` 前缀。
