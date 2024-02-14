# Python Quick Log Class

这是一个现成的Python Log类，基于logging，集成了控制台颜色、日志切割、日志分模块存储功能。

你可以直接Copy到你的项目中使用

# 使用

## 初始化

```python
import logging
import log as Log

# 定义日志输出的等级
log_level = logging.INFO
# "Main"可以是任意的字符串，用于区分不同模块的日志
log = Log.log("Main",log_level)
```

## 日志输出

```python
# Debug
log.debug("Debug")

# Info
log.info("Info")

# Warning
log.warning("Warning")

# Error
log.error("Error")

# Critical
log.critical("Critical")
```
