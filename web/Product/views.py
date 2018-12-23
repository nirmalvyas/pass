import hashlib
import json
import uuid

from flask import Blueprint, Response, g, request
from psycopg2.extras import RealDictCursor
import datetime
from appholder import *
from Product.models import Products
from sqlalchemy import func, case, and_, exists, or_, desc
from utils import *
import psycopg2
product_blueprint= Blueprint('product', __name__)

@product_blueprint.route('/products',methods=['POST','GET','OPTIONS'])
@crossdomain(origin="*", headers="Content-Type")
def products():
    if request.method == 'POST': 
        try:
            product_name = request.values.get('product_name')
            product_code = request.values.get('product_code')
            unit_price = request.values.get('unit_price')
            uom = request.values.get('uom',0.00)
            stock_in_hand = request.values.get('stock_in_hand',1)
            description = request.values.get('description')
            product_type = request.values.get('product_type','consumable')
            category_id = request.values.get('category_id')

            if not product_name:
                return json.dumps({'error':'Product_name_IS_MANDOTRY','status':0})
            elif not product_code:
                return json.dumps({'error':'last_name_IS_MANDOTRY','status':0})
            elif not product_type:
                return json.dumps({'error':'product_type_IS_MANDOTRY','status':0})
            elif not category_id:
                return json.dumps({'error':'category_id_IS_MANDOTRY','status':0})
            
            #insert all values in the user tbl
            # con = g.con
            con = psycopg2.connect(config.DB_CONNECTION)
            print con
            cur = con.cursor(cursor_factory=RealDictCursor) 
            
            # create the product
            product_obj = Products(product_name=product_name,product_code=product_code,
            unit_price= unit_price,uom = uom,stock_in_hand = stock_in_hand,description = description,
            product_type = product_type,category_id = category_id
            )
            db.session.add(product_obj)
            db.session.commit()
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
        q = db.session.query(Products.product_name,Products.product_code,Products.description,
        Products.stock_in_hand,Products.unit_price,Products.product_type
        ).filter(Products.status == 'A').all()
        result_set =[]
        if q:
            result_set = [u._asdict() for u in q]
        return json.dumps({'message':'Data got successfully','data':result_set,'status':1})

    elif request.method == 'PUT':
        ## display the data:
        product_id = request.values.get('product_id')
        product_name = request.values.get('product_name')
        product_code = request.values.get('product_code')
        unit_price = request.values.get('unit_price')
        uom = request.values.get('uom',0.00)
        stock_in_hand = request.values.get('stock_in_hand',1)
        description = request.values.get('description')
        product_type = request.values.get('product_type','consumable')
        category_id = request.values.get('category_id')
        result_set = []
        if not product_name:
            return json.dumps({'error':'Product_name_IS_MANDOTRY','status':0})
        elif not product_code:
            return json.dumps({'error':'last_name_IS_MANDOTRY','status':0})
        elif not product_type:
            return json.dumps({'error':'product_type_IS_MANDOTRY','status':0})
        elif not category_id:
            return json.dumps({'error':'category_id_IS_MANDOTRY','status':0})
        
        q = db.session.query(Products).filter(Products.id == product_id).update(
            {'product_name':product_name,
             'product_code': product_code,
             'unit_price': unit_price,
             'uom':uom,
             'stock_in_hand': stock_in_hand,
             'description': description,
             'product_type': product_type,
             'category_id':category_id
            })
        result_set_all = q.all()
        db.session.commit()
        if result_set_all:
            result_set = [u._asdict() for u in q]
        return json.dumps({'message':'Data update Successfully','data':result_set,'status':1})

    elif request.method == 'DELETE':
        product_id = request.values.get('product_id')
        if not product_id:
            return json.dumps({'error':'product_id_IS_MANDOTRY','status':0})

        q = db.session.query(Products).filter(Products.id == product_id).update({
            'status': 'D' 
        })
        q.all()
        db.session.commit()
        return json.dumps({'message':'Data deleted successfully!!','status':1})

            



    else:
        return json.dumps({'error':'UNAUTHORISED_METHOD_FOR_ACCESS','status':0})