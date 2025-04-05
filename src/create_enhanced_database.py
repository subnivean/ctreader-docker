import pandas as pd
import sqlite3

DBPATH = "../data/heatpumpctdata.sqlite"
CTS = "ct0 ct1 ct2 ct3".split()


with sqlite3.connect(DBPATH) as conn:
    df = pd.read_sql_query("SELECT * from housectdata", conn)

df.DateTime = pd.to_datetime(df.DateTime)
df["incrhours"] = df.DateTime.diff().dt.seconds / 3600

# for TH in (100, 150, 200, 250, 300, 350, 400):
for TH in (200,):
    for ct in CTS:
        ctadj = f"{ct}Adj"
        ctincr = f"{ct}IncrKWh"
        cttotl = f"{ct}TotKWh"

        df[ctadj] = df[ct]
        df.loc[df[ctadj] < TH, ctadj] = 0.0
        df[ctincr] = df["incrhours"] * df[ctadj] / 1000
        df[cttotl] = df[ctincr].cumsum()
    print(f"{TH}: {(df.ct3TotKWh * 0.19).iloc[-1]}")

df.set_index("DateTime", inplace=True)

with sqlite3.connect("/data/test.sqlite") as conn:
    df.to_sql("housectdata", conn)

