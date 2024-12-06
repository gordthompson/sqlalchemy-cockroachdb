from alembic.testing.suite import *  # noqa
from sqlalchemy.testing import skip
from alembic.testing.suite import AutogenerateFKOptionsTest as _AutogenerateFKOptionsTest
from alembic.testing.suite import BackendAlterColumnTest as _BackendAlterColumnTest
from alembic.testing.suite import IncludeHooksTest as _IncludeHooksTest


class AutogenerateFKOptionsTest(_AutogenerateFKOptionsTest):
    @skip("cockroachdb")
    def test_nochange_ondelete(self):
        pass


class BackendAlterColumnTest(_BackendAlterColumnTest):
    def test_add_server_default_int(self):
        if config.db.dialect.driver != "asyncpg":
            super().test_add_server_default_int()

    def test_modify_non_nullable_to_nullable(self):
        if config.db.dialect.driver != "asyncpg":
            super().test_modify_non_nullable_to_nullable()

    @skip("cockroachdb")
    def test_modify_nullable_to_non(self):
        # previously needed "with self.op.get_context().autocommit_block():"
        # which is no longer valid in SQLA 2.0
        pass

    def test_modify_server_default_int(self):
        if config.db.dialect.driver != "asyncpg":
            super().test_modify_server_default_int()

    @skip("cockroachdb")
    def test_modify_type_int_str(self):
        # TODO: enable this test when warning removed for ALTER COLUMN int → string
        pass

    def test_rename_column(self):
        if config.db.dialect.driver != "asyncpg":
            super().test_rename_column()


class IncludeHooksTest(_IncludeHooksTest):
    def test_add_metadata_fk(self):
        if config.db.dialect.driver != "asyncpg":
            super().test_add_metadata_fk()

    @combinations(("object",), ("name",))
    def test_change_fk(self, hook_type):
        if config.db.dialect.driver != "asyncpg":
            super().test_change_fk(hook_type)

    @combinations(("object",), ("name",))
    def test_remove_connection_fk(self, hook_type):
        if config.db.dialect.driver != "asyncpg":
            super().test_remove_connection_fk(hook_type)
