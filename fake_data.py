import csv

from multiprocessing.pool import Pool
from faker import Faker


def make_tsv_file(filename, fake, number_rows):
    with open(filename, 'wt') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        for i in range(number_rows):
            id = fake.pyint()
            code = fake.ean13()
            cost = fake.pydecimal(left_digits=5, right_digits=2, positive=True)
            qty = fake.pydecimal(left_digits=2, right_digits=1, positive=True)
            total = cost*qty
            created_ts = fake.date_time_between(
                start_date="-3y", end_date="now")
            modified_ts = fake.date_time_between(
                start_date="-3y", end_date="now")
            writer.writerow(
                [id, code, cost, qty, total, created_ts, modified_ts])


def generate(number_rows,
             number_files,
             start_num=0,
             filename_prefix="book",
             path="data"):

    fake = Faker()

    for i in range(start_num, start_num+number_files):
        filepath = "{path}/{filename_prefix}-{index}.tsv".format(
            path=path,
            filename_prefix=filename_prefix,
            index=i)
        make_tsv_file(filepath, fake, number_rows)


if __name__ == "__main__":
    rows = 200000
    pool = Pool()
    pool.starmap(generate,
                 [(rows, 5, 0),
                  (rows, 5, 5),
                  (rows, 5, 10),
                  (rows, 5, 15)])
