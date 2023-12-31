import streamlit as st
import pandas as pd

st.title('Dit is mijn titel')
st.divider()
st.header('1 Dit is mijn eerste kop',divider='orange')

st.subheader('Dit is een subkop',help='Je kunt ook wat extra info tonen')
st.caption('Een caption is een onderschrift')
st.text('Zo schrijf je normale tekst')
st.write('Andere manier van schrijven, kan meerdere datatypes in 1 bevatten')
st.markdown('Zo kun je ook nog teksten schrijven')

st.subheader('Hieronder zijn data elementen te zien')
my_dataframe=pd.DataFrame([[1,2],[3,4]],columns=['Column A','Column B'])
st.dataframe(my_dataframe)

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

st.table([[1,2],[3,4]])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Temp",value="273 K",delta="1.2 K")

st.subheader('Wat input widgets')
c1,c2,c3=st.columns(3)
with c1:
    st.button("Click me")
with c2:
    st.checkbox("I agree")
with c3:
    st.toggle("Activate")

st.text_input("Tekst toevoegen")
st.sidebar.write("This lives in the sidebar")
