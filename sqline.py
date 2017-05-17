import click
from sqlalchemy import create_engine
import pandas as pd


def get_engine_string(dialect, username, password, endpoint, name, port):
    engine = """{}://{}:{}@{}:{}/{}""".format(
        dialect, username, password, endpoint, port, name
    )
    return engine


@click.command()
@click.argument('query', type=str, required=False)
@click.option('--username', envvar='DB_USER')
@click.option('--password', envvar='DB_PASSWORD')
@click.option('--endpoint', envvar='DB_ENDPOINT')
@click.option('--name', envvar='DB_NAME')
@click.option('--port', envvar='DB_PORT')
@click.option('--dialect', envvar='DB_DIALECT')
@click.option('-o', '--output')
def main(query, username, password, endpoint, name, port, dialect, output):
    """Console script for sqline."""

    if not query:
        query = click.get_text_stream('stdin').read()

    engine_string = get_engine_string(dialect, username, password,
                                      endpoint, name, port)

    engine = create_engine(engine_string)

    result = pd.read_sql(query, con=engine)

    if output == 'csv':
        click.echo(result.to_csv())
    elif output == 'json':
        click.echo(result.to_json(orient='records', lines=True))
    else:
        click.echo(result)
