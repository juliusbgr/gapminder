import pandas as pd

def tidy_df(df, value_name):
    df = df.melt(id_vars=["country"], var_name="year", value_name=value_name)
    df["year"] = df["year"].astype(int)
    return df

def load_and_clean_data():

    pop_df = pd.read_csv("pop.csv")
    life_df = pd.read_csv("lex.csv")
    gni_df = pd.read_csv("gnipercapita_ppp_current_international.csv")

    pop_df = pop_df.fillna(method='bfill', axis=1)
    life_df = life_df.fillna(method='bfill', axis=1)
    gni_df = gni_df.fillna(method='bfill', axis=1)

    pop_tidy = tidy_df(pop_df, "population")
    life_tidy = tidy_df(life_df, "life_expectancy")
    gni_tidy = tidy_df(gni_df, "gni_per_capita")

    df = pop_tidy.merge(life_tidy, on=["country", "year"], how="outer") \
                  .merge(gni_tidy, on=["country", "year"], how="outer")

    for col in ["population", "life_expectancy", "gni_per_capita"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.sort_values(["country", "year"])

    for col in ["population", "life_expectancy", "gni_per_capita"]:
        df[col] = df.groupby("country")[col].ffill()
        df[col] = df.groupby("country")[col].bfill()

    return df

