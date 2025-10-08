#!/usr/bin/env python3
import argparse
import csv
import html


def csv_to_html_rows(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            # Trim whitespace and escape HTML
            cells = [html.escape(cell.strip()) for cell in row if cell.strip() != ""]
            html_row = "<tr>" + "".join(f"<td>{cell}</td>" for cell in cells) + "</tr>"
            print(html_row)


def main():
    parser = argparse.ArgumentParser(
        description="Convert CSV file rows to HTML table rows."
    )
    parser.add_argument("csv_file", help="Path to the CSV file.")
    args = parser.parse_args()
    csv_to_html_rows(args.csv_file)


if __name__ == "__main__":
    main()
