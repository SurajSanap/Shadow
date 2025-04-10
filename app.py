import streamlit as st
import traceback
from retrieval.vector_store import VectorStore
from rules.response_engine import apply_agent_rules
from utils.access_control import is_authorized, deny_response
from utils.prompt_utils import format_prompt

st.set_page_config(page_title="Project SHADOW", layout="centered")
st.title("🕵️ Project SHADOW - Classified Query Assistant")

# --- UI ---
agent_label = st.selectbox("Select Agent Level:", ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"])
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
