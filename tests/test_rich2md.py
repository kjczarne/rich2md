import pandas as pd
import unittest
from rich.table import Table
from rich2md import rich_table_to_df, rich_table_to_md_table


class TestRich2Md(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.table = Table("A", "B")
        cls.table.add_row("my", "mom")
        cls.table.add_row("your", "dad")
        
    def test_to_df(self):
        df = rich_table_to_df(self.table)
        self.assertIsInstance(df, pd.DataFrame)

    def test_to_md(self):
        str_ = rich_table_to_md_table(self.table)
        expected = """| A    | B   |
|:-----|:----|
| my   | mom |
| your | dad |"""
        self.assertEqual(str_, expected)


if __name__ == "__main__":
    unittest.main()

