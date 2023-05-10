from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

datos = Table("datos", meta_data,
              Column("id", Integer, primary_key=True),
              Column("estado",String(255), nullable=False),
              Column("fecha", Integer, nullable=False))

meta_data.create_all(engine)