import streamlit as st
import google.oauth2.credentials

from google.cloud import bigquery
from streamlit_google_oauth import google_oauth2_required


@google_oauth2_required
def main():
     user_email = st.session_state.user_email 
     access_token = st.session_state["token"]
     st.write(f"あなたは {user_email} でログイン中です")
     
     credentials = google.oauth2.credentials.Credentials(
          token = access_token,
          scopes=["https://www.googleapis.com/auth/bigquery"]
     )
     client = bigquery.Client(credentials=credentials, project="Google projectIDを記載する")

     # Perform a query.
     QUERY = """
     ここにBigQueryに向けたSQLを記載すれば、表構造で画面上に出力される
     """
     df = client.query(QUERY).to_dataframe()  # API request
          
     st.dataframe(df,width=1200,height=1500)
main()