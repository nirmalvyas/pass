from appholder import *
# from Movies.views import movies_blueprint


from sqlalchemy import Column, DateTime, Integer, String, text,Float,Date

    

class Products(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, name='id')
    product_name = Column(String(50), name='product_name')
    product_code = Column(String(20), name='product_code')
    unit_price = Column(Float, name='unit_price')
    uom = Column(String(20), name='uom')
    stock_in_hand = Column(Float, name='stock_in_hand')
    description = Column(String(50), name='description')
    product_type = Column(String(20), name='product_type')
    category_id = Column(Integer, name='category_id')   
    update_dttm = Column(DateTime(True), server_default=text("now()"), name='update_dttm')
    create_dttm = Column(DateTime(True), server_default=text("now()"), name='create_dttm')
    status = Column(String(1), name='status', default='A')

