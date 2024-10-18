# Rich2MD

This is a simple tool to convert [Rich](https://github.com/Textualize/rich) tables to Markdown tables.

## Installation

```bash
pip install rich2md
```

## Usage

There are two functions:

- `rich_table_to_df` – converts the Rich `Table` object to a Pandas DataFrame.
- `rich_table_to_md_table` – converts the Rich `Table` object to a Markdown table and returns it as a string.

Example:

```python
from rich.table import Table
from rich2md import rich_table_to_md_table

table = Table("A", "B")
table.add_row("my", "mom")
table.add_row("your", "dad")
table_md = rich_table_to_md_table(table)
print(table_md)
```
