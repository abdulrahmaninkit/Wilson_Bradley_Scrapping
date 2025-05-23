import streamlit as st
import pandas as pd
from scrape import save_to_excel, scrape_website, extract_body_content
st.title("Web Scraping of Wilson and Bradley Products")
url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape"):
    st.write("Scrapping the website...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    excel_data = save_to_excel(body_content)
    

    # with st.expander("View DOM Content"):
    #     st.text_area("DOM Content", body_content[4], height=500)

    df = pd.read_excel('product_description.xlsx')
    st.dataframe(df,height=500)

