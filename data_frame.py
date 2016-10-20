"""
Easy utilities to use dataframe with pandas.
"""

import pymysql.cursors
import pandas as pd
import os

# ---------------------------------------------------------------------
# MySQL
# ---------------------------------------------------------------------

# Paste below variables to ~/.bash_profile first.
"""
export db_host=db_host
export db_name=database
export db_user=user
export db_pass=pass
export db_charset=utf8
"""


def mysql_connect():
    """
    MySQL connection.
    Above parameters must be set to ~/.bash_profile first.
    """

    db_host = os.environ["db_host"]
    db_name = os.environ["db_name"]
    db_user = os.environ["db_user"]
    db_pass = os.environ["db_pass"]
    db_charset = os.environ["db_charset"]

    return pymysql.connect(
        host=db_host,
        db=db_name,
        user=db_user,
        # passwd = user,
        charset=db_charset,
    )


def table_data(table):
    """
    Execute SQL with pandas.

    Parameters
    ----------
    table : string
        Table name.
    """
    qry = "SELECT * FROM {0}".format(table)
    return pd.read_sql(qry, mysql_connect())


def table_data_chunk(table, chunksize):
    """
    Execute SQL with chunk.

    Parameters
    ----------
    table : string
        Table name.
    chunksize : integer
        Number of chunk size to process.
    """
    qry = "SELECT * FROM {0}".format(table)
    return pd.read_sql(qry, mysql_connect(), chunksize=chunksize)

# ---------------------------------------------------------------------
# csv
# ---------------------------------------------------------------------

def read_csv(csv_path):
    """
    Read csv

    Prameters
    ---------
    csv_path : str
        csv file path to read.
    """
    pd.read_csv(csv_path)

# ---------------------------------------------------------------------
# Generate random/test data
# ---------------------------------------------------------------------

def simple_df(num):
    """
    Generate simple dataframe

    Parameters
    ----------
    num : integer
        Number of craete data.
    """
    return pd.DataFrame([i for i in range(num)])

def simple_df_with_col(col, num):
    """
    Generate simple dataframe with column.

    Parameters:
    -----------
    col : string
        Column name.
    num : integer
        Number of values to generate.
    """
    return pd.DataFrame({
        col : [i for i in range(num)]
    })

# ---------------------------------------------------------------------
# Search data
# ---------------------------------------------------------------------


def more_than_num(df, col, num):
    """
    Get more than num data from dataframe.

    Ex:
        more_than_num(df, "id", 1)

    Parameters
    ----------
    df  : DataFrame
        DataFrame
    col : column name
        Column name.
    num : integer
        More than value
    """
    return df.query("{0} > {1}".format(col, num))


def less_than_num(df, col, num):
    """
    Get less than num data from dataframe.

    Ex:
        more_than_num(df, "id", 100)

    Parameters
    ----------
    df  : DataFrame
        DataFrame
    col : column name
        Column name.
    num : integer
        Less than value
    """
    return df.query("{0} < {1}".format(col, num))


def between_num(df, col, low, high):
    """
    Get between data from dataframe.

    Ex:
        df = simple_df_with_col("id", 10)
        between_num(df, "id", 1, 8)
        # 8

    Parameters
    ----------
    df  : DataFrame
        DataFrame
    col : column name
        Column name.
    low : integer
        Less than value
    high : integer
        More than value
    """
    return df.query("{0} > {1} & {0} < {2}".format(col, low, high))

# ---------------------------------------------------------------------
# concatenate
# ---------------------------------------------------------------------

def concat_row(df1, df2):
    """
    Concatenate as row.

    Ex:
        df1 = pd.DataFrame([1,2,3])
        df2 = pd.DataFrame([4,5,6])
        concat_row(df1, df2)

    Sample return
    -------------
       0
    0  1
    1  2
    2  3
    3  4
    4  5
    5  6

    Parameters
    ----------
    df1 : pd.DataFrame
    df2 : pd.DataFrame

    """
    return pd.concat([df1, df2]).reset_index(drop=True)
