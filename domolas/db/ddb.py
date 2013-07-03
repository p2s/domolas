#!/usr/bin/python3
# -*-coding:Utf-8 -*

from sqlalchemy import *

class Ddb():
    """
    this util class aim to save data into database with sqlalchemy
    """
    global_table_list = (
        ('d_temphumi', (
            Column('id',Integer,Sequence('d_temphumi_id_seq'),primary_key=True),
            Column('name', String(40)),
            Column('temp', Integer),
            Column('humidite', Integer),
            Column('time', TIMESTAMP),
            )
        ),
        """('t_table2', (
            Column('c_id',Integer,Sequence('t_table2_id_seq'),primary_key=True),
            Column('c_type', Integer),
            Column('c_sex', BOOLEAN),
            Column('c_province', Integer),
            Column('c_area', Integer),
            Column('c_platform', String(40)),
            Column('c_url', String(100)),
            )
        ),
        ('t_table3', (
            Column('c_rule_id',Integer),
            Column('c_keyword', String(40)),
            Column('c_timeline', String(20)),
            )
        ),"""
    )

    def __init__(self):
        self.db = create_engine('sqlite:///domolas.db')

        self.db.echo = False  # no alchemy log

        metadata = MetaData(db)

        for (t_name,t_columns) in global_table_list:
            try:
                cur_table = Table(t_name,metadata,autoload=True)
            except:
                cur_table = apply(Table,(t_name,metadata) + t_columns)
                cur_table.create()


