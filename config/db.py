from sqlalchemy import  create_engine, MetaData

engine = create_engine('mysql+mysqlconnector://root:1234@localhost/test')
meta_data = MetaData()