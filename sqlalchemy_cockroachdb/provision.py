from sqlalchemy import event
from sqlalchemy.testing.provision import post_configure_engine
from sqlalchemy.testing.provision import temp_table_keyword_args


@post_configure_engine.for_db("cockroachdb")
def _cockroachdb_post_configure_engine(url, engine, follower_ident):
    @event.listens_for(engine, "checkout")
    def checkout(dbapi_con, con_record, con_proxy):
        if str(dbapi_con).startswith("<AdaptedConnection <asyncpg.connection.Connection"):
            cursor = dbapi_con.cursor()
            cursor.execute("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE")


@temp_table_keyword_args.for_db("cockroachdb")
def _cockroachdb_temp_table_keyword_args(cfg, eng):
    return {"prefixes": ["TEMPORARY"]}
