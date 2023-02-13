import toml
import streamlit as st
import pandas as pd
import snowflake.connector as sf
from datetime import date
import altair as alt

sidebar = st.sidebar
st.set_page_config(layout='wide')

def connect_to_snowflake(acct,usr,pwd,role,wh,db):
    ctx = sf.connect(user=usr,account=acct,password=pwd,role=role,warehouse=wh,database=db)
    cs = ctx.cursor()
    st.session_state['snow_conn'] = cs
    st.session_state['is_ready'] = True
    return cs

#@st.cache(suppress_st_warning=True,show_spinner=False)
def get_data():
    query = 'select * from lob1_db.lob1_schema.customer LIMIT 10;'
    results = st.session_state['snow_conn'].execute(query)
    results = st.session_state['snow_conn'].fetch_pandas_all()
    return results

# def render_chart(df):
#     summary = alt.Chart(df).mark_bar().encode(
#         x='C_MKTSEGMENT',
#         y='sum(C_ACCTBAL):Q'
#
#     )
#     st.altair_chart(summary,use_container_width=True)

with sidebar:
    account = st.text_input("Account")
    username = st.text_input("Username")
    password = st.text_input("Password")
    role = st.text_input("Role")
    wh = st.text_input("Warehouse")
    db = st.text_input("Database")
    connect = st.button("Connect to Snowflake",
                        on_click=connect_to_snowflake,
                        args=[account,username,password,role,wh,db])

if 'is_ready' not in st.session_state:
    st.session_state['is_ready'] = False

if st.session_state['is_ready'] == True:
    data = get_data()
    acctbal = data['C_ACCTBAL'].agg(['min','max'])
    min,max = st.slider("Account Balance Range",
                        min_value=float(acctbal['min']),
                        max_value=float(acctbal['max']),
                        value=[float(acctbal['min']),float(acctbal['max'])])

    data.loc[data['C_ACCTBAL'].between(min,max)]
    #st.dataframe(acctbal)
    summary = alt.Chart(data.loc[data['C_ACCTBAL'].between(min,max)]).mark_bar().encode(
        x='C_MKTSEGMENT',
        y='sum(C_ACCTBAL):Q'

    )
    # average = alt.Chart(data.loc[data['C_ACCTBAL'].between(min,max)]).mark_bar().encode(
    #     x='C_MKTSEGMENT',
    #     y='avg(C_ACCTBAL):Q'
    #
    # )

    st.altair_chart(summary,use_container_width=True)
    #render_chart(data)
    for sgm in list(data['C_MKTSEGMENT'].unique()):
        st.write(sgm,key=f'{sgm}')
        chart = alt.Chart(data.loc[data['C_MKTSEGMENT']==sgm]).mark_bar().encode(
            x='C_CUSTKEY',
            y='sum(C_ACCTBAL):Q'

        )
        st.altair_chart(chart, use_container_width=True)



