import streamlit as st
import traceback
from retrieval.vector_store import VectorStore
from rules.response_engine import apply_agent_rules
from utils.access_control import is_authorized, deny_response
from utils.prompt_utils import format_prompt
from streamlit_lottie import st_lottie

import json




st.set_page_config(page_title="SHADOW", layout="centered")


try:
    with open('Static/image/Home.json', encoding='utf-8') as anim_source:
        animation_data = json.load(anim_source)
    st_lottie(animation_data, 1, True, True, "high", 150, -200)
except FileNotFoundError:
    st.error("Animation file not found.")
except UnicodeDecodeError as e:
    st.error(f"Error decoding JSON: {e}. Try specifying a different encoding.")
except Exception as e:
    st.error(f"An error occurred: {e}")

st.title("SHADOW - Classified Query Assistant")

# --- Sidebar ---
st.sidebar.title("Agent Controls")
agent_label = st.sidebar.selectbox("Select Agent Level:", ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"])
st.sidebar.markdown("---")

st.sidebar.info("Ensure proper clearance before submission.")
st.sidebar.markdown("---")

st.sidebar.info("Trust no one. Assume nothing. Adapt or be eliminated.")





# --- UI ---
query = st.text_area("Enter your classified query:")


# --- Main Logic ---
if st.button("Submit"):
    agent_level = agent_label.split()[-1]  # "Level 3" → "3"

    if not query.strip():
        st.warning("Please enter a query.")
    else:
        st.write(f"Processing for {agent_label}...")

        if not is_authorized(int(agent_level), query):
            st.error(deny_response())
        else:
            try:
                # Run vector search
                vector = VectorStore("chunks/secret_info_chunks.json")
                results = vector.query(query)

                # Get styled + rule-matched response
                response = apply_agent_rules(agent_level, query, results)
                st.success(response)

            except Exception as e:
                st.error("❌ An error occurred during processing:")
                st.code(traceback.format_exc())
