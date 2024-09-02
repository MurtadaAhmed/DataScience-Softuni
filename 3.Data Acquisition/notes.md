importing pandas library:
```
impoort pandas as pd
```

reading csv file:
```
file = pd.read_cvs("file.csv")
```

show columns, index, dimensions:
```
file.columns
file.index
file.shape
```

reading json file:
```
file = pd.read_json()
```

reading from sql:
```
conda install sqlalchemy

import sqlalchemy
engine = sqlalchemy.create_engine("....")
```

perform a query:
```
customer_info = pd.read_sql(
    "select * from Sales.Customer",
    engine
    )
```