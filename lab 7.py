import streamlit as st
import altair as alt
import polars as pl


data_url = "https://www.dei.unipd.it/~ceccarello/gapminder.csv"
data = pl.read_csv(data_url).filter(pl.col("year") == 2007)
st.write(data)

st.write("# A bubble chart")

chart = (
    alt.Chart(data)
    .mark_circle()
    .encode(
        x=alt.X("gdpPercap").scale(type="log"),
        y=alt.Y("lifeExp").scale(zero=False),
        size=alt.Size("pop"),
        color=alt.Color("continent")
    )
)

st.altair_chart(chart, use_container_width=True)

st.write("# A bar chart, with aggregations")
st.altair_chart(
    alt.Chart(data)
    .mark_bar()
    .encode(
        alt.Y("continent", sort="x"),
        alt.X("sum(pop)")
    ),
    use_container_width=True
)
