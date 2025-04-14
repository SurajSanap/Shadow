import streamlit as st
import traceback
from retrieval.vector_store import VectorStore
from rules import response_engine
from rules.response_engine import apply_agent_rules
from utils.access_control import is_authorized, deny_response
from streamlit_lottie import st_lottie
import json

# Initialize session state
if 'query_input' not in st.session_state:
    st.session_state.query_input = ""
if 'show_examples' not in st.session_state:
    st.session_state.show_examples = False

st.set_page_config(page_title="SHADOW", layout="centered")

# Animation loading
try:
    with open('Static/image/Home.json', encoding='utf-8') as anim_source:
        animation_data = json.load(anim_source)
    st_lottie(animation_data, 1, True, True, "high", 150, -200)
except FileNotFoundError:
    st.error("Animation file not found.")
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

# --- Query Suggestions ---
DEFAULT_SUGGESTIONS = [
    "What is the status of Project Requiem?",
    "How to evade thermal surveillance?",
    "Who is the Hollow Man?", 
    "Explain Cipher Delta protocol"
]

EXTENDED_SUGGESTIONS = DEFAULT_SUGGESTIONS + [
    "Safehouse locations in Berlin",
    "Extraction procedures for Level 5 agents",
    "Decryption keys for Omega Echo",
    "Current threat level assessment"
]

# --- CSS Styling ---
st.markdown("""
<style>
    .stTextArea textarea::placeholder {
        color: #6c757d !important;
        font-style: italic;
        opacity: 0.7;
    }
    .small-font {
        font-size: 0.8em !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Query Input Section ---
query_placeholder = DEFAULT_SUGGESTIONS[0] if not st.session_state.query_input else ""

col1, col2 = st.columns([4, 1])
with col1:
    query = st.text_area(
        "Enter your classified query:",
        value=st.session_state.query_input,
        placeholder=query_placeholder,
        key="main_query_input",
        help="Top secret query input"
    )

with col2:
    if st.button("📋 Examples", help="Show example queries"):
        st.session_state.show_examples = not st.session_state.show_examples

if st.session_state.show_examples:
    with st.expander("Example Queries", expanded=True):
        st.markdown("<p class='small-font'>Select an example to load:</p>", unsafe_allow_html=True)
        cols = st.columns(2)
        for i, example in enumerate(EXTENDED_SUGGESTIONS):
            with cols[i % 2]:
                if st.button(example, key=f"example_{i}"):
                    st.session_state.query_input = example
                    st.session_state.show_examples = False
                    st.rerun()

# --- Main Logic ---
if st.button("Submit"):
    agent_level = agent_label.split()[-1]

    if not query.strip():
        st.warning("Please enter a query.")
    else:
        st.write(f"Processing for {agent_label}...")
        if not is_authorized(int(agent_level), query):
            st.error(deny_response())
        else:
            try:
                vector = VectorStore("chunks/secret_info_chunks.json")
                results = vector.query(query)
                response = apply_agent_rules(agent_level, query, results)
                st.success(response)
            except Exception as e:
                st.error("❌ An error occurred during processing:")
                st.code(traceback.format_exc())