import hashlib
import json
import uuid

from flask import Blueprint, Response, g, request
from psycopg2.extras import RealDictCursor
import datetime
from appholder import *
from User.models import User
from sqlalchemy import func, case, and_, exists, or_, desc
from util import (authenticate, generate_password_hash, generate_session,
                  get_user_roles,id_generator)
import psycopg2

user_blueprint= Blueprint('user', __name__)



@user_blueprint.route('/users',methods=['POST','GET','OPTIONS'])
def user_register():
    if request.method == 'POST': 
        try:
            first_name = request.values.get('first_name')
            last_name = request.values.get('last_name')
            email = request.values.get('email')
            mobile = request.values.get('mobile')
            pan_number = request.values.get('pan_number')
            dob = request.values.get('dob')
            if not first_name:
                return json.dumps({'error':'first_name_IS_MANDOTRY','status':0})
            elif not last_name:
                return json.dumps({'error':'last_name_IS_MANDOTRY','status':0})
            elif not mobile:
                return json.dumps({'error':'mobile_IS_MANDOTRY','status':0})
            
            #insert all values in the user tbl
            # con = g.con
            con = psycopg2.connect(config.DB_CONNECTION)
            print con
            cur = con.cursor(cursor_factory=RealDictCursor) 
            user_uuid = uuid.uuid4()
            user_name=str(first_name.lower())+str(datetime.datetime.now().year)

            user_password = id_generator(chars=user_name)
            # create the user
            user_obj = User(first_name=first_name,last_name=last_name,modhash=user_uuid,
                            email = email,mobile =mobile,pan_number=pan_number,login_name = user_name,
                            password = user_password,dob=dob
            )
            db.session.add(user_obj)
            db.session.commit()
            user_name_id = user_obj.id
            q = db.session.query(User).filter(User.id == user_name_id).update({'login_name':user_name+str(user_name_id)})
            # q = q.all()
            db.session.commit()
            # create entry in the session
            # and make user login
            # store session/token in the cookies
            return json.dumps({'message':'user inserted successfully','status':1})

        except Exception as e: 
            print "==Something went wrong==",str(e)
            return json.dumps({'error':'SOMETHING_WENT_WRONG_IN_LOGGING_USER','status':0})

    elif request.method == 'GET':
        ## display the data:
        q = db.session.query(User.first_name.label('firstname'),User.last_name.label('lastname'),
        User.email.label('User_email'),User.pan_number.label('Pan_number'),
        User.password.label('Password'),User.login_name.label('User_login'),
        User.modhash.label('Modhash')
        ).all()
        result_set =[]
        if q:
            result_set = [u._asdict() for u in q]
        return json.dumps({'message':'Data got successfully','data':result_set,'status':1})


    else:
        return json.dumps({'error':'UNAUTHORISED_METHOD_FOR_ACCESS','status':0})


@user_blueprint.route('/user/login',methods=['POST'])
def user_login():
    if request.method == 'POST': 
        try:
            user_name = request.values.get('user_name')
            password = request.values.get('password')

            if not user_name:
                return json.dumps({'error':'user_name_IS_MANDOTRY','status':0})
            if not password:
                return json.dumps({'error':'password_IS_MANDOTRY','status':0})
            # check that user_name exits or not
            l = User.query.filter_by(login_name=user_name).one_or_none()
            if l is None:
                return json.dumps({'error':'USER_IS_NOT_REGISTERED','status':0})
            #authenticate password
            exsisting_password = l.password
            print exsisting_password,password
            if not str(exsisting_password).strip() == str(password).strip():
                return json.dumps({'error':'PASSWORD_IS_INVALID','status':0})
            # check the seesion and if there is active session deactivate them
            session_id = request.cookies.get('session_id')
            if session_id:
                session_auth = authenticate(session_id=session_id)
                if session_auth:
                    db.session.query(UserLogin).filter(UserLogin.session_id == session_id).update({
                        'status':'D'
                        })
            # create new seesion for login
            session_id = generate_session(uuid=l.uuid)
            if isinstance(session_id,bool):
                return json.dumps({'error':'SOMETHING_WENT_WRONG_IN_LOGGING_USER','status':0})
            js={'status':1,'message':'login_created'}
            resp = Response(js, status=200, mimetype='application/json')
            resp.set_cookie('session_id', session_id.session_id, expires=session_id.expiration_ttm)
            return resp


            

        except Exception as e:
            print "==Something went wrong==",str(e)
            return json.dumps({'error':'SOMETHING_WENT_WRONG_IN_LOGGING_USER','status':0})

    else:
        return json.dumps({'error':'UNAUTHORISED_METHOD_FOR_ACCESS','status':0})



@user_blueprint.route('/user/logout',methods=['GET'])
def user_logout():
    if request.method == 'GET': 
        try:
            session_id = request.values.get('session_id')
            # check the seesion and if there is active session deactivate them
            if not session_id:
                session_id = request.cookies.get('session_id')
            if session_id:
                db.session.query(UserLogin).filter(UserLogin.session_id == session_id).update({
                    'status':'D'
                    })

            return json.dumps({'status':1,'message':'Logged Out Successfully!'})

            

        except Exception as e:
            print "==Something went wrong==",str(e)
            return json.dumps({'error':'SOMETHING_WENT_WRONG_IN_LOGGING_OUT_USER','status':0})

    else:
        return json.dumps({'error':'UNAUTHORISED_METHOD_FOR_ACCESS','status':0})

@user_blueprint.route('/user/authenticate',methods=['GET'])
def user_authenticate():
    if request.method == 'GET': 
        try:
            roles_data ={}
            session_id = request.values.get('session_id')
            print"===what is seesion==",session_id
            # check the seesion and if there is active session deactivate them
            if not session_id:
                session_id = request.cookies.get('session_id')
            if session_id:
                session_auth = authenticate(session_id=session_id)
                print"====check user_is authenicated====session is on==",session_auth
                ## if session is authorised we will check for the roles
                roles_data = get_user_roles(session_id=session_id)
            return json.dumps({'status':1,'message':'Roles Data','data':roles_data})

        except Exception as e:
            print "==Something went wrong==",str(e)
            return json.dumps({'error':'SOMETHING_WENT_WRONG_IN_LOGGING_OUT_USER','status':0})

    else:
        return json.dumps({'error':'UNAUTHORISED_METHOD_FOR_ACCESS','status':0})
