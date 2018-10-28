from appholder import *
# from Movies.views import movies_blueprint


from sqlalchemy import Column, DateTime, Integer, String, text,Float,Date

    

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, name='id')
    first_name = Column(String(50), name='first_name')
    last_name = Column(String(50), name='last_name')
    email = Column(String(20), name='email')
    mobile = Column(String(15), name='mobile')
    pan_number = Column(String(20), name='pan_number')
    login_name = Column(String(20), name='login_name')
    password = Column(String(50), name='password')
    modhash = Column(String(50), name='modhash')
    gcm_id = Column(String(50), name='gcm_id')
    dob = Column(Date, name='DOB')

    update_dttm = Column(DateTime(True), server_default=text("now()"), name='update_dttm')
    create_dttm = Column(DateTime(True), server_default=text("now()"), name='create_dttm')
    status = Column(String(1), name='status', default='A')

class Group(db.Model):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, name='id')
    group_name = Column(String(20), name='group_name')
    group_code = Column(String(20), name='group_name')
    parent_id =  Column(Integer,name='parent_id')
    update_dttm = Column(DateTime(True), server_default=text("now()"), name='update_dttm')
    create_dttm = Column(DateTime(True), server_default=text("now()"), name='create_dttm')
    status = Column(String(1), name='status', default='A')


class group_category(db.Model):
    __tablename__ = 'group_category'
    group_id = Column(Integer,name='group_id',primary_key=True)
    category_id = Column(Integer,name='group_id',primary_key=True)
    session_id = Column(String(100),name='session_id')
    expiration_ttm = Column(DateTime(True),name='expiration_ttm')
    update_dttm = Column(DateTime(True), server_default=text("now()"), name='update_dttm')
    create_dttm = Column(DateTime(True), server_default=text("now()"), name='create_dttm')
    status = Column(String(1), name='status', default='A')


class UserLogin(db.Model):
    __tablename__ = 'user_login'

    id = Column(Integer, primary_key=True, name='id')
    user_token = Column(String(100),name='user_token')
    session_id = Column(String(100),name='session_id')
    expiration_ttm = Column(DateTime(True),name='expiration_ttm')
    update_dttm = Column(DateTime(True), server_default=text("now()"), name='update_dttm')
    create_dttm = Column(DateTime(True), server_default=text("now()"), name='create_dttm')
    status = Column(String(1), name='status', default='A')





if __name__ == '__main__':
   manager.run()