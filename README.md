# SQLine

[![Build Status](https://travis-ci.org/davidgasquez/sqline.svg?branch=master)](https://travis-ci.org/davidgasquez/sqline)

Command line tool to perform SQL database queries. With `sqline` you can mix the power of Unix tools with the power of SQL.

## Installation

To install `sqline`, simply:

```bash
pip install sqline
```

## Requirements

You need to set the following environment variables:
- `DB_USER`
- `DB_PASSWORD`
- `DB_ENDPOINT`
- `DB_NAME`
- `DB_PORT`
- [`DB_DIALECT`](http://docs.sqlalchemy.org/en/latest/core/engines.html): Engine and driver for SQLAlchemy.

## Usage

Making a simple query is easy as running `sqline "select * from users limit 10"`. One you're happy with your query you can get the entire result in JSON or CSV. Is also possible to get the input from a file. For example, having `query.sql`:

```SQL
SELECT
    user,
    age,
    country
FROM users
WHERE age > 25
```

Running `cat query.sql | sqline -o json` will give a set of new line delimited JSONs. You can plug any existing Unix tool to the output, for example `jq` for the JSON output (`cat query.sql | sqline -o json | jq .country | uniq -c`).


Contributions are welcome!
