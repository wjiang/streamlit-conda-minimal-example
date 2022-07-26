import sys
import shutil 
import streamlit as st

st.info(sys.path)
st.info(sys.executable)
st.info(shutil.which("python"))
st.info(shutil.which("cuda"))
st.info(shutil.which("streamlit"))

sys.path = [p for p in sys.path if p.find("3.7")==-1 and not p.startswith("/usr/local")]
st.info(sys.path)

import cctbx
import iotbx
