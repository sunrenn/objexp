# 这是一个版本备份的脚本，由于主要代码都在`./src/objxp/_init_.py`中，所以只需要备份这一个文件即可。现在我希望备份文件名中包含日期，所以需要修改脚本。

# 备份文件名格式为：objxp_init_YYYYMMDD.py
# 获取当前日期
$Date = Get-Date -Format "yyyyMMdd"

# 备份文件名
$BackupFile = "./bak/objxp_init_$Date.py"

Copy-Item -Path ./src/objxp/__init__.py -Destination $BackupFile