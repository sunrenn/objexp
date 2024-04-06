# Building and Distributing Packages with Setuptools

Setuptools is a collection of enhancements to the Python distutils that allow developers to more easily build and distribute Python packages, especially ones that have dependencies on other packages.

Packages built and distributed using setuptools look to the user like ordinary Python packages based on the distutils.

## Feature Highlights：

- Create Python Eggs - a single-file importable distribution format
创建 Python Eggs ---- 一种单文件可导入的分发格式

- Enhanced support for accessing data files hosted in zipped packages.
增强了对访问托管在压缩包中的数据文件的支持。

- Automatically include all packages in your source tree, without listing them individually in setup.py
自动将所有包包含在源代码树中，而无需在 setup.py 中单独列出它们

- Automatically include all relevant files in your source distributions, without needing to create a MANIFEST.in file, and without having to force regeneration of the MANIFEST file when your source tree changes [1].
自动将所有相关文件包含在源代码分发中，而无需创建 MANIFEST.in 文件，也不必在源代码树更改 1 时强制重新生成 MANIFEST 文件。

- Automatically generate wrapper scripts or Windows (console and GUI) .exe files for any number of “main” functions in your project. (Note: this is not a py2exe replacement; the .exe files rely on the local Python installation.)
自动生成包装脚本或 Windows（console 和 GUI）.exe文件，用于项目中任意数量的“主要”函数。（注意：这不是 py2exe 的替代品;.exe文件依赖于本地 Python 安装。

- Transparent Cython support, so that your setup.py can list .pyx files and still work even when the end-user doesn’t have Cython installed (as long as you include the Cython-generated C in your source distribution)
透明的 Cython 支持，因此您的 setup.py 可以列出 .pyx 文件，即使最终用户没有安装 Cython（只要您在源代码分发中包含 Cython 生成的 C）

- Command aliases - create project-specific, per-user, or site-wide shortcut names for commonly used commands and options
命令别名 - 为常用的命令和选项创建特定于项目的快捷方式名称、每用户名称或站点范围的快捷方式名称

- Deploy your project in “development mode”, such that it’s available on sys.path, yet can still be edited directly from its source checkout.
在“开发模式”下部署您的项目，使其在 上 sys.path 可用，但仍然可以直接从其源代码检出进行编辑。

- Easily extend the distutils with new commands or setup() arguments, and distribute/reuse your extensions for multiple projects, without copying code.
使用新的命令或 setup() 参数轻松扩展 distutils，并为多个项目分发/重用您的扩展，而无需复制代码。

- Create extensible applications and frameworks that automatically discover extensions, using simple “entry points” declared in a project’s setup script.
使用项目设置脚本中声明的简单“入口点”创建可扩展的应用程序和框架，这些应用程序和框架可以自动发现扩展。

- Full support for PEP 420 via find_namespace_packages(), which is also backwards compatible to the existing find_packages() for Python >= 3.3.
完全支持 PEP 420 via find_namespace_packages() ，它也向后兼容现有的 find_packages() Python >= 3.3。

## Developer’s Guide 开发者指南
The developer’s guide has been updated. See the [most recent version](https://setuptools.pypa.io/en/latest/userguide/index.html).
开发人员指南已更新。查看最新版本。

### TRANSITIONAL NOTE 过渡性说明#

Setuptools automatically calls declare_namespace() for you at runtime, but future versions may not. This is because the automatic declaration feature has some negative side effects, such as needing to import all namespace packages during the initialization of the pkg_resources runtime, and also the need for pkg_resources to be explicitly imported before any namespace packages work at all. In some future releases, you’ll be responsible for including your own declaration lines, and the automatic declaration feature will be dropped to get rid of the negative side effects.
Setuptools 在运行时会自动调用 declare_namespace() 您，但将来的版本可能不会。这是因为自动声明功能有一些负面的副作用，例如需要在 pkg_resources 运行时初始化期间导入所有命名空间包，并且还需要 pkg_resources 在任何命名空间包工作之前显式导入。在将来的某些版本中，您将负责包含自己的声明行，并且将删除自动声明功能以消除负面副作用。

During the remainder of the current development cycle, therefore, setuptools will warn you about missing declare_namespace() calls in your __init__.py files, and you should correct these as soon as possible before the compatibility support is removed. Namespace packages without declaration lines will not work correctly once a user has upgraded to a later version, so it’s important that you make this change now in order to avoid having your code break in the field. Our apologies for the inconvenience, and thank you for your patience.
因此，在当前开发周期的剩余时间里，setuptools 会警告您 __init__.py 文件中缺少 declare_namespace() 调用，您应该在删除兼容性支持之前尽快更正这些调用。一旦用户升级到更高版本，没有声明行的命名空间包将无法正常工作，因此请务必立即进行此更改，以避免在字段中中断代码。对于给您带来的不便，我们深表歉意，并感谢您的耐心等待。

## setup.cfg-only projects 仅限 setup.cfg 的项目

New in version 40.9.0. 
新版本 40.9.0.

If setup.py is missing from the project directory when a PEP 517 build is invoked, setuptools emulates a dummy setup.py file containing only a setuptools.setup() call.
如果 setup.py 在调用 setuptools PEP 517 构建时从项目目录中丢失，则模拟仅包含调用的 setuptools.setup() 虚拟 setup.py 文件。

> ##### Note 注意
>
> PEP 517 doesn’t support editable installs so this is currently incompatible with pip install -e ..
PEP 517 不支持可编辑安装，因此目前与 pip install -e . .
> 
> ...

This means that you can have a Python project with all build configuration specified in setup.cfg, without a setup.py file, if you can rely on your project always being built by a PEP 517/PEP 518 compatible frontend.
这意味着，如果项目始终由 PEP 517/PEP 518 兼容的前端构建，则可以在没有 setup.py 文件的情况下拥有 中指定 setup.cfg 的所有构建配置的 Python 项目。

#### To use this feature 要使用此功能，请执行以下操作：

- Specify build requirements and PEP 517 build backend in pyproject.toml. For example:
在 pyproject.toml 中指定构建要求和 PEP 517 构建后端。例如：

```toml
[build-system]
requires = [
  "setuptools >= 40.9.0",
]
build-backend = "setuptools.build_meta"
```

- Use a PEP 517 compatible build frontend, such as pip >= 19 or build.
使用 PEP 517 兼容的构建前端，例如 pip >= 19 或 build .

> #### Warning 警告
> 
> As PEP 517 is new, support is not universal, and frontends that do support it may still have bugs. For compatibility, you may want to put a setup.py file containing only a setuptools.setup() invocation.
由于 PEP 517 是新的，因此支持不是通用的，支持它的前端可能仍然存在错误。为了兼容，您可能希望放置一个 setup.py 仅包含 setuptools.setup() 调用的文件。
> 
> ...


## Configuration API 配置 API#

Some automation tools may wish to access data from a configuration file.
某些自动化工具可能希望从配置文件访问数据。

Setuptools exposes a read_configuration() function for parsing metadata and options sections into a dictionary.
Setuptools 在字典中公开用于 read_configuration() 解析 metadata 和 options 节的函数。

```python
from setuptools.config import read_configuration

conf_dict = read_configuration("/home/user/dev/package/setup.cfg")
```

By default, read_configuration() will read only the file provided in the first argument. To include values from other configuration files which could be in various places, set the find_others keyword argument to True.
默认情况下， read_configuration() 将只读取第一个参数中提供的文件。要包含可能位于不同位置的其他配置文件中的值，请将 find_others 关键字参数设置为 True 。

If you have only a configuration file but not the whole package, you can still try to get data out of it with the help of the ignore_option_errors keyword argument. When it is set to True, all options with errors possibly produced by directives, such as attr: and others, will be silently ignored. As a consequence, the resulting dictionary will include no such options.
如果你只有一个配置文件，而不是整个包，你仍然可以尝试借助 ignore_option_errors 关键字参数从中获取数据。当它设置为 True 时，所有可能由指令（如 attr: 和 等）产生的错误的选项都将被静默忽略。因此，生成的字典将不包含此类选项。

### Forum and Bug Tracker 论坛和错误跟踪器#

Please use GitHub Discussions for questions and discussion about setuptools, and the setuptools bug tracker ONLY for issues you have confirmed via the forum are actual bugs, and which you have reduced to a minimal set of steps to reproduce.
请使用 GitHub Discussions 来回答有关 setuptools 的问题和讨论，而 setuptools bug 跟踪器仅适用于您通过论坛确认的问题是实际的 bug，并且您已将其简化为一组最小的步骤来重现。

-----

[1]
The default behaviour for setuptools will work well for pure Python packages, or packages with simple C extensions (that don’t require any special C header). See Controlling files in the distribution and Data Files Support for more information about complex scenarios, if you want to include other types of files.
默认行为 setuptools 适用于纯 Python 包或具有简单 C 扩展的包（不需要任何特殊的 C 标头）。有关复杂方案的详细信息，请参阅控制分发中的文件和数据文件支持（如果要包含其他类型的文件）。