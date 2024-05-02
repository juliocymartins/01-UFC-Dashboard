import pandas as pd

## STEP 1: LOAD DATASET AND PREPARE A NEW DATAFRAME WITH DATA THAT WILL BE USED IN FURTHER ANALYSIS.

# Load the dataset into a DataFrame.
ufc_df_raw = pd.read_csv(r'caminho\ufc-master.csv')

ufc_df = ufc_df_raw.copy()

# Changing the format of some dates to standardize their format

for index in range(0, 58):  # Intervalo de linhas 0 a 57 (lembrando que o índice começa em 0)
    old_date = ufc_df.at[index, 'date']
    parts = old_date.split('-')
    year = parts[0]
    month = parts[1]
    day = parts[2]
    new_date = f"{int(month)}/{int(day)}/{year}"  # Convertendo para formato 'm/d/Y'
    ufc_df.at[index, 'date'] = new_date

# Convert the 'date' column to datetime type.
ufc_df['date'] = pd.to_datetime(ufc_df['date'])   

# Select the desired columns from the original DataFrame
selected_columns = [
    "R_fighter", "weight_class", "R_wins", "R_losses", "R_draw", "R_age",
    "R_win_by_Submission", "R_win_by_KO/TKO", "R_Stance", "R_total_title_bouts",
    "R_total_rounds_fought", "R_longest_win_streak", "R_win_by_Decision_Majority",
    "R_win_by_Decision_Split", "R_win_by_Decision_Unanimous",
    "R_win_by_TKO_Doctor_Stoppage", "date"
]

# Create a new DataFrame r_fighters_df_raw with the selected columns
r_fighters_df_raw = ufc_df[selected_columns].copy()

# Rename the columns in r_fighters_df_raw
column_rename_dict = {
    "R_fighter": "fighter",
    "R_wins": "wins",
    "R_losses": "losses",
    "R_draw": "draws",
    "R_age": "age",
    "R_win_by_Submission": "win_by_Submission",
    "R_win_by_KO/TKO": "win_by_KO/TKO",
    "R_Stance": "Stance",
    "R_total_title_bouts": "total_title_bouts",
    "R_total_rounds_fought": "total_rounds_fought",
    "R_longest_win_streak": "longest_win_streak",
    "R_win_by_Decision_Majority": "win_by_Decision_Majority",
    "R_win_by_Decision_Split": "win_by_Decision_Split",
    "R_win_by_Decision_Unanimous": "win_by_Decision_Unanimous",
    "R_win_by_TKO_Doctor_Stoppage": "win_by_TKO_Doctor_Stoppage"
}

r_fighters_df_raw.rename(columns=column_rename_dict, inplace=True)

# Sort the DataFrame by 'fighter', 'weight_class', and 'date' in descending order
r_fighters_df_raw.sort_values(by=['fighter', 'weight_class', 'date'], ascending=[True, True, False], inplace=True)

# Keep only the unique rows based on 'fighter' and 'weight_class', keeping the first (most recent)
r_fighters_df = r_fighters_df_raw.drop_duplicates(subset=['fighter', 'weight_class'])
# print(r_fighters_df.head())
# print(r_fighters_df.head())
# print(r_fighters_df.shape)

# Select the desired columns from the original DataFrame
selected_columns = [
    "B_fighter", "weight_class", "B_wins", "B_losses", "B_draw", "B_age",
    "B_win_by_Submission", "B_win_by_KO/TKO", "B_Stance", "B_total_title_bouts",
    "B_total_rounds_fought", "B_longest_win_streak", "B_win_by_Decision_Majority",
    "B_win_by_Decision_Split", "B_win_by_Decision_Unanimous",
    "B_win_by_TKO_Doctor_Stoppage", "date"
]

# Create a new DataFrame r_fighters_df_raw with the selected columns
b_fighters_df_raw = ufc_df[selected_columns].copy()

# Rename the columns in r_fighters_df_raw
column_rename_dict2 = {
    "B_fighter": "fighter",
    "B_wins": "wins",
    "B_losses": "losses",
    "B_draw": "draws",
    "B_age": "age",
    "B_win_by_Submission": "win_by_Submission",
    "B_win_by_KO/TKO": "win_by_KO/TKO",
    "B_Stance": "Stance",
    "B_total_title_bouts": "total_title_bouts",
    "B_total_rounds_fought": "total_rounds_fought",
    "B_longest_win_streak": "longest_win_streak",
    "B_win_by_Decision_Majority": "win_by_Decision_Majority",
    "B_win_by_Decision_Split": "win_by_Decision_Split",
    "B_win_by_Decision_Unanimous": "win_by_Decision_Unanimous",
    "B_win_by_TKO_Doctor_Stoppage": "win_by_TKO_Doctor_Stoppage"
}

b_fighters_df_raw.rename(columns=column_rename_dict2, inplace=True)

# Sort the DataFrame by 'fighter', 'weight_class', and 'date' in descending order
b_fighters_df_raw.sort_values(by=['fighter', 'weight_class', 'date'], ascending=[True, True, False], inplace=True)

# Keep only the unique rows based on 'fighter' and 'weight_class', keeping the first (most recent)
b_fighters_df = b_fighters_df_raw.drop_duplicates(subset=['fighter', 'weight_class'])
# print(r_fighters_df.head())
# print(b_fighters_df.head())
# print(b_fighters_df.shape)
# Concatenar os dataframes ao longo das linhas
ufc_fighters_df_raw = pd.concat([r_fighters_df, b_fighters_df], ignore_index=True)

## Até criação de novo dataframe ufc_fighters_df ##

# Calculate the column win_by_Decision
ufc_fighters_df_raw['win_by_Decision'] = (
    ufc_fighters_df_raw['win_by_Decision_Majority'] +
    ufc_fighters_df_raw['win_by_Decision_Split'] +
    ufc_fighters_df_raw['win_by_Decision_Unanimous']
)

# Create the 'win-loss differential' column
ufc_fighters_df_raw.loc[:, 'win-loss differential'] = ufc_fighters_df_raw['wins'] - ufc_fighters_df_raw['losses']

# Sort the DataFrame by 'fighter', 'weight_class', and 'date' in descending order
ufc_fighters_df_raw.sort_values(by=['fighter', 'weight_class', 'date'], ascending=[True, True, False], inplace=True)

# Keep only the unique rows based on 'fighter' and 'weight_class', keeping the first (most recent)
ufc_fighters_df = ufc_fighters_df_raw.drop_duplicates(subset=['fighter', 'weight_class'])

# print(ufc_fighters_df.head())
# print(ufc_fighters_df.shape)

# ## Até wrangling de novo dataframe ufc_fighters_df ##
# ufc_fighters_df.to_excel(r'caminho\ufc_fighters.xlsx')

# List of columns for statistics to be summed
stat_columns = ['wins', 'draws', 'losses', 'age', 'win_by_Submission', 'win_by_KO/TKO', 'Stance',
                'total_title_bouts', 'total_rounds_fought', 'longest_win_streak', 'win_by_Decision_Majority',
                'win_by_Decision_Split', 'win_by_Decision_Unanimous', 'win_by_TKO_Doctor_Stoppage',
                'win_by_Decision', 'win-loss differential']

# Group by fighter, combine weight classes and most recent date
grouped = ufc_fighters_df.groupby('fighter', as_index=False).agg({
    'weight_class': '/'.join,
    'date': 'max',
    'age': 'max',  # Keep the highest age
    **{col: 'sum' for col in stat_columns if col not in ['fighter', 'date', 'age', 'Stance', ]}
})

# Rename the columns
ufc_fighters_all_df = grouped.rename(columns={'win_by_KO/TKO': 'win_by_KO_TKO'})

grouped.to_excel(r'caminho\ufc_fighters_all.xlsx')

for index in range(0, 58):  # Intervalo de linhas 0 a 57 (lembrando que o índice começa em 0)
    old_date = ufc_df_raw.at[index, 'date']
    parts = old_date.split('-')
    year = parts[0]
    month = parts[1]
    day = parts[2]
    new_date = f"{int(month)}/{int(day)}/{year}"  # Convertendo para formato 'm/d/Y'
    ufc_df_raw.at[index, 'date'] = new_date

# Converter a coluna 'date' para o tipo datetime.
ufc_df_raw['date'] = pd.to_datetime(ufc_df_raw['date'])   
ufc_df_raw.to_excel(r'caminho\ufc_fights.xlsx')

