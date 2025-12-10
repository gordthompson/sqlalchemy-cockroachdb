# CockroachDB dialect for SQLAlchemy

## Setup

### Version of SQLAlchemy to be used

This version of the dialect requires SQLAlchemy 2.1.x. To work with
SQLAlchemy 2.0.x you'll need to install the corresponding version of this
dialect.

```
pip install "sqlalchemy-cockroachdb~=2.0"
```

### Using async

If you will be running async code you'll need to install the additional
support components for SQLAlchemy:

```
pip install "sqlalchemy[asyncio]"
```

### Database driver

A database driver (DBAPI layer) is required to work with this dialect.

#### psycopg2 (sync only)

For psycopg2 support you must install either:

* [psycopg2](https://pypi.org/project/psycopg2/), which has some
  [prerequisites](https://www.psycopg.org/docs/install.html#prerequisites) of
  its own, or

* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)

(The binary package is a practical choice for development and testing but in
production it is advised to use the package built from sources.)

#### asyncpg (async only)

For asyncpg support you must install [asyncpg](https://pypi.org/project/asyncpg/). For more details on working with asyncpg, see 
[README.asyncpg.md](README.asyncpg.md).

#### psycopg (sync or async)

For psycopg version 3 support, you'll need to install [psycopg](https://pypi.org/project/psycopg/). As with psycopg2, psycopg can 
be installed as binary for development and testing purposes.
(Installing as binary avoids the need for the libpq-dev package to be installed first.)

```
pip install "psycopg[binary]"
```

For more details on working with psycopg, see 
[README.psycopg.md](README.psycopg.md)
 
## Usage

Use a `cockroachdb` connection string when creating the `Engine`. For example,
to connect to an insecure, local CockroachDB cluster using psycopg2:

```python
from sqlalchemy import create_engine
engine = create_engine('cockroachdb://root@localhost:26257/defaultdb?sslmode=disable')
```

or

```python
from sqlalchemy import create_engine
engine = create_engine('cockroachdb+psycopg2://root@localhost:26257/defaultdb?sslmode=disable')
```

To connect using asyncpg:

```python
from sqlalchemy.ext.asyncio import create_async_engine
engine = create_async_engine('cockroachdb+asyncpg://root@localhost:26257/defaultdb')
```

To connect using psycopg for sync operation:

```python
from sqlalchemy import create_engine
engine = create_engine('cockroachdb+psycopg://root@localhost:26257/defaultdb')
```

To connect using psycopg for async operation, see
[README.psycopg.md](README.psycopg.md)


## Changelog

See [CHANGES.md](CHANGES.md)
