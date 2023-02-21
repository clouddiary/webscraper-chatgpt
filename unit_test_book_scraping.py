import unittest
import csv
import os
import subprocess


class TestBookScraping(unittest.TestCase):
    def test_book_scraping(self):
        # Run the book scraping code        
        subprocess.run("python book_scraping.py", check=True, shell=True)
        print(os.getcwd())


        # Verify that the CSV file was created and contains data
        self.assertTrue(os.path.isfile('books.csv'))
        with open('books.csv', mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            self.assertEqual(header, ['Title', 'Price'])
            rows = list(csv_reader)
            self.assertGreater(len(rows), 0)

        # Verify that the price visualization was created
        #self.assertTrue(plt.fignum_exists(1))

if __name__ == '__main__':
    unittest.main()
