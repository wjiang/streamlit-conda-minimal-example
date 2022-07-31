import sys
import shutil
from pathlib import Path
import streamlit as st

# essential to avoid cctbx import errors
target = Path("/home/appuser/venv/share/cctbx")
if not target.exists():
  target.symlink_to("/home/appuser/.conda/share/cctbx")

import cctbx
import iotbx

st.info(dir(iotbx))
st.info(dir(cctbx))
st.info(f"cctbx version: {cctbx.get_version()}")

sys.path += ["/home/appuser/venv/lib/python3.9/lib-dynload"]
for p in sys.path:
  if p.find("lib-dynload")==-1: continue
  st.info(f'{p}: {[str(item) for item in Path(p).glob("*")]}')
  
st.info([str(item) for item in Path("/").glob("**/boost_python_meta_ext*")])

from cctbx.array_family import flex
