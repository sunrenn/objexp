# Sub Plan:

    - read:
        https://realpython.com/pypi-publish-python-package/,
        https://builtin.com/data-science/how-to-publish-python-code-pypi
        https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/

    - 仍没有找到更好的替代方案的需求，inspect的getmembers()方法（再配合一下pprint.pprint()）看似能完成这项任务，实则不是给人看的: https://favtutor.com/blogs/print-object-attributes-python Using __dir__() method / Using vars() function / Using inspect module


# Note from Realpython - Pypi Publish Python package

## Example
[Realpython Reader Download](https://codeload.github.com/realpython/reader/zip/refs/heads/master)

realpython-reader/
│
├── src/
│   └── reader/
│       ├── __init__.py
│       ├── __main__.py
│       ├── config.toml
│       ├── feed.py
│       └── viewer.py
│
├── tests/
│   ├── test_feed.py
│   └── test_viewer.py
│
├── LICENSE
├── MANIFEST.in
├── README.md
└── pyproject.toml


## pyproject.toml Example: 
https://realpython.com/pypi-publish-python-package/#configure-your-package

## Install Your Package Locally
在本地安装软件包

可编辑安装。这是一种使用 pip 在本地安装包的方法，可让您在安装代码后编辑代码。

通常，pip 会进行常规安装，将包放入您的 site-packages/ 文件夹中。如果安装本地项目，则源代码将复制到 site-packages/。这样做的效果是，您稍后所做的更改不会生效。您需要先重新安装您的软件包。

在开发过程中，这可能既无效又令人沮丧。Editable 安装通过直接链接到您的源代码来解决此问题。

可编辑的安装已在 PEP 660 中正式确定。这些在开发包时非常有用，因为您可以测试包的所有功能并更新源代码，而无需重新安装。

您可以通过添加 -e 或 --editable 标志，使用 pip 以可编辑模式安装包：

```powershell
(venv) $ python -m pip install -e .
```

请注意命令末尾的句点（.）。这是命令的必要部分，并告诉 pip 您要安装位于当前工作目录中的软件包。通常，这应该是包含 pyproject.toml 文件的目录的路径。

## 脚本
教程示例reader中 pyproject.toml 
```toml
    [project.scripts]
    realpython = "reader.__main__:main"
```
定义了一个realpython脚本，可以在终端中直接运行`realpython`执行main

## token

test.pypi.org 和 pypi.org 的两步安全认证可以用安卓app：Microsofte Authenticator 来扫码完成。

完成两步安全认证后才能生成token。

构建 `python -m build`

上传 `twine upload dist/*`

<!-- https://www.pyopensci.org/python-package-guide/tutorials/publish-pypi.html#step-4-create-a-package-upload-token -->




