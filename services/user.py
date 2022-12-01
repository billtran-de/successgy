from repo.user import UserModel
from utils.db import log

log = log

class UserServices:
  '''
    This layer handles all logical interaction between handler layer and repo layer
  '''

  # check if credentials in payload match in db
  @classmethod
  def check_permission(cls, emp_id, password):
    all_users_info = UserModel.find_all_users()

    for user_info in all_users_info:
      if emp_id == user_info['emp_id'] and password == user_info['password']:
        return True

  # add new user to the database (if user not yet exists)
  @classmethod
  def add_user(cls, user_info):
    try:
      UserModel.add_new_user(user_info)
    except:
      log.error("Not be able to add this user to db")
      
