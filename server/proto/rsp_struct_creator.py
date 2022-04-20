
import tag_recommend_system_pb2

class rsp_struct:
  def __init__(self, tag_recommend_sys_pb):
    self.film_id = tag_recommend_sys_pb.film_id
    self.web_id = tag_recommend_sys_pb.web_id
    self.web_score = tag_recommend_sys_pb.web_score
    self.web_full_score = tag_recommend_sys_pb.web_full_score
    self.date = tag_recommend_sys_pb.date
    self.tags = tag_recommend_sys_pb.tags
    self.areas = tag_recommend_sys_pb.areas
    self.directors_and_actors = tag_recommend_sys_pb.directors_and_actors
    self.quote = tag_recommend_sys_pb.quote