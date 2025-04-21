import streamlit as st
import openai
import pickle
import numpy as np
# Load the trained LGBM model from a pickle file

@st.cache_resource
def load_model():
    return  model = pickle.load(open("lgbm_movie_rating_model.pkl", "rb"))
    
# the model is stored in the same directory 
# e.g., train a model and then upload to github directory
model = load_model()

st.title("Movie Rating Predictor")

movie_summary = st.text_area("Movie Summary", height=200)
if movie_summary:
    with st.spinner("Generating embedding and predicting rating..."):
        # Step 1: Get embedding from OpenAI
        embedding_response = openai.embeddings.create(
            model="text-embedding-3-small",
            input=movie_summary
        )
        embedding = embedding_response.data[0].embedding

          # Step 2: Predict using LGBM
        embedding_array = np.array(embedding).reshape(1, -1)
        predicted_rating = model.predict(embedding_array)[0]

    st.success(f"Predicted IMDb Rating: ⭐ {predicted_rating:.2f}")
