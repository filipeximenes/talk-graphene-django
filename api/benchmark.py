import json
from django.db import connection, reset_queries
from api.schemaV1 import schema as schemaV1
from api.schemaV2 import schema as schemaV2


def print_result(result):
    print(json.dumps(result.data, indent=2))


query = """
query {
  bands {
    name
    artists {
      full_name
    }
    albums {
      title
      songs {
        title
      }
    }
  }
}
"""


reset_queries()
result = schemaV1.execute(query)
print('V1 queries: ', len(connection.queries))


reset_queries()
result = schemaV2.execute(query)
print('V2 queries: ', len(connection.queries))


