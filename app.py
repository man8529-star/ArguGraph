import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="wide")

st.title("ArguGraph: Visualizing the Structure of Student Argumentation")

# -------------------------------------------------
# Essay metadata
# -------------------------------------------------

essay_data = {
    "Essay 1 (Low Complexity)": {
        "id": "essay_1",
        "collapsed_acc": 0.88,
        "expanded_acc": 0.75,
        "complexity": "Low Complexity"
    },
    "Essay 2 (High Complexity)": {
        "id": "essay_2",
        "collapsed_acc": 0.24,
        "expanded_acc": 0.60,
        "complexity": "High Complexity"
    }
}

# -------------------------------------------------
# Essay Selection
# -------------------------------------------------

essay_choice = st.selectbox(
    "Select Essay",
    list(essay_data.keys())
)

essay_info = essay_data[essay_choice]
essay_id = essay_info["id"]

st.markdown(f"**Complexity Level:** {essay_info['complexity']}")

# -------------------------------------------------
# Model View Selection
# -------------------------------------------------

model_option = st.radio(
    "Select Structure View",
    ["Reference Structure", "Collapsed Model", "Expanded Model"],
    horizontal=True
)

# -------------------------------------------------
# Accuracy Display
# -------------------------------------------------

st.markdown("### Ranking Accuracy")

col1, col2 = st.columns(2)

with col1:
    st.metric("Collapsed Model", essay_info["collapsed_acc"])

with col2:
    st.metric("Expanded Model", essay_info["expanded_acc"])

# -------------------------------------------------
# Essay Text (Collapsible)
# -------------------------------------------------

def load_essay_text(essay_id):
    path = f"essays/{essay_id}.txt"
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return "Essay text not found."

with st.expander("View Essay Text"):
    st.write(load_essay_text(essay_id))

# --------------------------------------------
# Image Selection Logic
# --------------------------------------------

image_path = None  # always define first

if model_option == "Reference Structure":
    image_path = f"trees/{essay_id}_gold.png"

elif model_option == "Collapsed Model":
    image_path = f"trees/{essay_id}_collapsed.png"

elif model_option == "Expanded Model":
    image_path = f"trees/{essay_id}_expanded.png"

# --------------------------------------------
# Display Tree
# --------------------------------------------

if image_path and os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, width=1200)
else:
    st.warning("Tree image not found.")
