#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load df_pt.pkl
df_pt_filename = 'df_pt.pkl'
with open(df_pt_filename, 'rb') as file:
    df_pt = pickle.load(file)

# Load similarity_scores.pkl
similarity_scores_filename = 'similarity_scores.pkl'
with open(similarity_scores_filename, 'rb') as file:
    similarity_scores = pickle.load(file)

# Load popular.pkl
popular_filename = 'popular.pkl'
with open(popular_filename, 'rb') as file:
    popular_df = pickle.load(file)

def recommend(Book_name):
    index = np.where(df_pt.index == Book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
    recommendations = [df_pt.index[i[0]] for i in similar_items]
    return recommendations

def main():
    st.header("Book Recommendation")

    # Get user input for book name
    book_name = st.text_input("Enter the book name")

    # Check if the user clicked the 'Recommend Similar Books' button
    if st.button('Recommend Similar Books'):
        # Get recommendations
        result = recommend(book_name)

        # Display the recommendations in Streamlit
        if result:
            st.success("Recommended Books:")
            st.write(result)
        else:
            st.warning("No recommendations found.")

# Call the main function
if __name__ == "__main__":
    main()


# In[ ]:




