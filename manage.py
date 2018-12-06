# -*- coding:utf-8 -*-
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from house import create_app, db

"""启动文件"""


app = create_app("development")

# 创建脚本管理工具对象
manager = Manager(app)
# 创建数据库迁移对象
migrate = Migrate(app, db)
# 在脚本工具中添加数据库迁移语句
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run() 