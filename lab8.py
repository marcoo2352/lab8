import streamlit as st
import altair as alt
import polars as pl


data_url = "https://www.dei.unipd.it/~ceccarello/data/gapminder.csv"
data = pl.read_csv(data_url).filter(pl.col("year") == 2007)
datac = pl.read_csv(data_url)
st.write(datac)

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

st.write("Relation between years and life expextancy")
st.altair_chart(
    alt.Chart(data).mark_point().properties(height = 500, width= 800).encode(
        alt.X("lifeExp:Q").scale(zero=False),
        alt.Y("continent:O"),
        color=alt.Color("continent:O", scale=alt.Scale(scheme="category10"))
))

st.altair_chart(
    alt.Chart(datac).mark_line().properties(height = 500, width= 800).encode(
        alt.Y("lifeExp:Q", aggregate = "median" ).scale(zero=False), #aggregate
        alt.X("year:O"),
        color=alt.Color("continent:O", scale=alt.Scale(scheme="category10"))        
    )
)
# Dizionario che mappa ogni continente a un colore specifico
color_mapping = {
    'Asia': 'yellow',
    'Europe': 'blue',
    'Africa': 'green',
    'Americas': 'purple',
    'Oceania': 'red'
}



base_pie = (
    alt.Chart(data).mark_arc(radius=90, radius2=150, size =15).encode(
        theta="sum(pop)",
       color=alt.Color("continent:O", scale=alt.Scale(domain=list(color_mapping.keys()), range=list(color_mapping.values())))
    )
)
st.altair_chart(base_pie)
"""
text_pie = (
    base_pie
    .mark_text(
        radius = 150
    )
    .transoform_calculate(
        label = "round(data.pop / 10000000)" + ' M'"
    )
    .encode(
        alt.Text("pop:N")
        alt.theta("pop", stack = True)
        alt.Order("continent")
    )
)

"""

chart = (
     base_pie + text_pie + text_total
)
.properties(
    height = 30,
    width = 30

)
.faced("year", columns = 3))












