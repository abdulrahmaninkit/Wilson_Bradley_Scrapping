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
    # st.dataframe(df,height=500)

    # for index, row in df.iterrows():
    #     image_urls = str(row["Product Image"]).split('\n')  # Handles multiple URLs
    # for url in image_urls:
    #     if url.strip():
    #         st.image(url.strip(), use_column_width=True)

    # Create two columns: one for the DataFrame, one for the images
    col1, col2 = st.columns([7, 3])  # Adjust ratios as needed

    # Show the table in the first column
    with col1:
        st.dataframe(df, height=1000, use_container_width=True)  # Display the DataFrame with specified height and width

    # Show images in the second column
    with col2:
        for index, row in df.iterrows():
            image_urls = str(row["Product Image"]).split('\n')
            for url in image_urls:
                if url.strip():
                    st.image(url.strip(), width=70)
                    col2.write(row["Product ID"])

