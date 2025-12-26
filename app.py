import streamlit as st
import json
from module_extractor import run_extraction
from utils import is_valid_url

st.set_page_config(page_title="Module Extraction AI Agent")

st.title("Module Extraction AI Agent")
st.write("Enter a documentation URL to extract modules and submodules")

url = st.text_input("Documentation URL")

if st.button("Extract Modules"):
    if not is_valid_url(url):
        st.error("Please enter a valid URL")
    else:
        with st.spinner("Processing documentation..."):
            result = run_extraction(url)
            st.subheader("Extracted Modules")
            st.json(result)

            with open("output/sample_output.json", "w") as f:
                json.dump(result, f, indent=2)

            st.success("Extraction completed and saved to output folder")
