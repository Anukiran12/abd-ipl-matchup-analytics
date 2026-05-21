import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="ABD IPL Matchup Analytics",
    layout="wide"
)

st.title("AB de Villiers IPL Matchup Analytics Dashboard")

st.write("""
This dashboard analyzes AB de Villiers' performance against elite IPL bowlers
using ball-by-ball IPL data from 2008–2022.

The selected bowlers were identified based on sustained IPL impact,
longevity, wicket-taking ability, economy control, and reputation across eras.
The analysis combines overall, phase-wise, and contextual relative metrics
to evaluate ABD's matchup performance against high-quality bowling attacks.
""")


overall_stats_df=pd.read_csv("data/processed/abd_vs_bowlers_overall.csv")
phase_wise_stats_df=pd.read_csv("data/processed/abd_vs_bowler_phase-wise.csv")
overall_relative_df=pd.read_csv("data/processed/overall_realtive_metrics.csv")
phase_wise_relative_df=pd.read_csv("data/processed/phase_wise_realtive_metrics.csv")



col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots(figsize=(10,8))

    sns.barplot(
        data=overall_stats_df,
        x='bowler',
        y='strike_rate',
        ax=ax
    )

    ax.set_title("AB de Villiers Strike Rate Against Elite IPL Bowlers")
    ax.set_xlabel("Bowler")
    ax.set_ylabel("Strike Rate")

    st.pyplot(fig)


with col2:

    fig, ax = plt.subplots(figsize=(10,8))

    sns.barplot(
        data=overall_stats_df,
        x='bowler',
        y='dot_ball%',
        ax=ax
    )

    ax.set_title("AB de Villiers Dot-Ball % Against Elite IPL Bowlers")
    ax.set_xlabel("Bowler")
    ax.set_ylabel("Dot-Ball %")

    st.pyplot(fig)






col1,col2=st.columns(2)

with col1:
    fig,ax=plt.subplots(figsize=(10,8))

    sns.barplot(
        data=phase_wise_stats_df,
        x='bowler',
        y='strike_rate',
        hue='phase',
        errorbar=None,
        ax=ax

    )

    ax.set_title("Phase-Wise Matchup Statistics")
    ax.set_xlabel("Bowlers")
    ax.set_ylabel("Strike Rate")

    st.pyplot(fig)

with col2:

    fig,ax=plt.subplots(figsize=(10,8))

    sns.barplot(
        data=phase_wise_stats_df,
        x='bowler',
        y='boundary_pct',
        hue='phase',
        errorbar=None,
        ax=ax
    )

    ax.set_title("AB De Villers Phase-Wise Boundary%")
    ax.set_xlabel("Bowlers")
    ax.set_ylabel("Boundary %")

    st.pyplot(fig)


st.header("Relative Metrics Analysis")

relative_display_df = overall_relative_df.copy()

relative_display_df = relative_display_df.rename(columns={
    'strike_rate_abd': 'ABD Strike Rate',
    'strike_rate_baseline': 'Baseline Strike Rate',
    'dot-ball%_abd': 'ABD Dot-Ball %',
    'dot-ball%_baseline': 'Baseline Dot-Ball %'
})

relative_display_df.index = relative_display_df.index + 1

st.dataframe(relative_display_df)



st.header("Key Insights")

st.markdown("""
- AB de Villiers maintained exceptionally high strike rates against elite death bowlers like Lasith Malinga and DJ Bravo.

- Dale Steyn and Sunil Narine restricted most IPL batters effectively, yet ABD sustained aggressive scoring rates against them.
            
- R Ashwin and Ravindra Jadeja were two bowlers who kept ABD quiet with low Strike Rate and score runs at a Strike Rate close to or less than than the other batters scored against them.         

- ABD showed his strongest acceleration during death overs, significantly outperforming bowlers' baseline conceded strike rates.

- Relative metrics reveal that ABD consistently scored faster than the average IPL batter against most elite bowlers analyzed.
""")