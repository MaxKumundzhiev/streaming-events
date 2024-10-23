import edgedb
import datetime

client = edgedb.create_client(dsn="edgedb://edgedb@localhost/ambv")

client.execute(
    """
    CREATE TYPE User {
        CREATE REQUIRED PROPERTY name -> str;
        CREATE PROPERTY date_of_birth -> cal::local_date;
    }
    """
)

client.query(
    """
    INSERT User {
        name := <str>$name;
        date_of_birth := <cal::local_date>$dob
    }
    """, name="Max", dob=datetime(1996, 3, 29)
)

print(client.query("SELECT User {name, date_of_birth};"))
