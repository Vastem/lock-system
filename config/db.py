from sqlalchemy import  create_engine, MetaData

engine = create_engine('mysql+mysqlconnector://root:c8UQwSGYneKMPHAWjEkk@containers-us-west-193.railway.app:6980/railway/')
meta_data = MetaData()