
import os
now_path = os.getcwd()
from tag_recommend_system_util import get_cur_info
from tag_recommend_system_util import append_project_path

append_project_path()
import config_parser

print(get_cur_info())
config = config_parser.DataParser(now_path + "/../conf/tag_recommend_system.yaml")
