from alembic.testing.suite import *  # noqa
from sqlalchemy.testing import skip
from alembic.testing.suite import AutogenerateFKOptionsTest as _AutogenerateFKOptionsTest
from alembic.testing.suite import BackendAlterColumnTest as _BackendAlterColumnTest


class AutogenerateFKOptionsTest(_AutogenerateFKOptionsTest):
    @skip("cockroachdb")
    def test_nochange_ondelete(self):
        # case sensitivity seems to have changed in 26.1_beta.3
        pass


class BackendAlterColumnTest(_BackendAlterColumnTest):
    def test_modify_nullable_to_non(self):
        if config.db.dialect._is_v253plus:
            super().test_modify_nullable_to_non()

    def test_modify_type_int_str(self):
        if config.db.dialect._is_v253plus:
            super().test_modify_type_int_str()
