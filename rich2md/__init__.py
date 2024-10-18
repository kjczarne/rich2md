from rich.table import Table
import pandas as pd


def rich_table_to_df(table: Table, keep_index: bool = False) -> pd.DataFrame:
    df = pd.DataFrame()
    for column in table.columns:
        # Get the cell contents for each column
        # (Note: iterating over rows does not work!)
        column_name = column.header
        cells_per_column = list(column.cells)
        df[column_name] = cells_per_column
    if not keep_index:
        # Remove the index column:
        df.reset_index(drop=True, inplace=True)
    return df


def rich_table_to_md_table(table: Table, keep_index: bool = False) -> str:
    df = rich_table_to_df(table, keep_index)
    return df.to_markdown(index=keep_index)


def main():
    table = Table("A", "B")
    table.add_row("my", "mom")
    table.add_row("your", "dad")
    table_md = rich_table_to_md_table(table)
    print(table_md)


if __name__ == "__main__":
    main()
