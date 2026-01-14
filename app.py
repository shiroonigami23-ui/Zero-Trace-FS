
import streamlit as st
import os
from core.engine import ZeroTraceEngine
from core.indexer import PhantomIndexer

st.set_page_config(page_title="Zero-Trace Dashboard", page_icon="👻")
st.title("Shiro Oni: Zero-Trace FS")

# Initialize Engine
engine = ZeroTraceEngine()
if not os.path.exists("vault.bin"):
    engine.initialize_vault(size_mb=10)
    st.success("Vault Initialized (10MB of Noise Generated)")

password = st.sidebar.text_input("Master Password", type="password")

if password:
    key, salt = engine.generate_master_key(password)
    indexer = PhantomIndexer(key)
    
    tab1, tab2 = st.tabs(["Ghost a File", "Retrieve File"])
    
    with tab1:
        uploaded_file = st.file_uploader("Choose a file to hide")
        if uploaded_file and st.button("Ghost It"):
            data = uploaded_file.read()
            indexer.hide_file("vault.bin", uploaded_file.name, data)
            indexer.export_index("index.oni")
            st.info(f"File {uploaded_file.name} is now part of the noise.")
            
    with tab2:
        file_to_get = st.text_input("Filename to retrieve")
        if st.button("Extract"):
            # This would call the GhostExtractor we planned
            st.warning("Extraction logic bridge coming in Step 2.")
