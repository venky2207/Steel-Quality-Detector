"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Regression</b> for the Prediction of Steel Quality.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    col1, col2 = st.columns(2)

    with col1:
        c = st.slider("Carbon %",float(df['c'].min()),float(df['c'].max()))
        mn = st.slider("Manganese %",float(df['mn'].min()),float(df['mn'].max()))
        si = st.slider("Silicon %",float(df['si'].min()),float(df['si'].max()))
        cr = st.slider("Chromium %",float(df['cr'].min()),float(df['cr'].max()))
        ni = st.slider("Nickle %",float(df['ni'].min()),float(df['ni'].max()))
        mo = st.slider("Molybdenum %",float(df['mo'].min()),float(df['mo'].max()))
        v = st.slider("Malleability Factor",float(df['v'].min()),float(df['v'].max()))

    with col2:
        n = st.slider("Ductility Factor",float(df['n'].min()),float(df['n'].max()))
        nb = st.slider("Niobium %",float(df['nb'].min()),float(df['nb'].max()))
        co = st.slider("Cobalt %",float(df['co'].min()),float(df['co'].max()))
        w = st.slider("Tungsten %",float(df['w'].min()),float(df['w'].max()))
        al = st.slider("Aluminium %",float(df['al'].min()),float(df['al'].max()))
        ti = st.slider("Titanium %",float(df['ti'].min()),float(df['ti'].max()))
        yield_strength = st.slider("Yield Strength %",float(df['yield_strength'].min()),float(df['yield_strength'].max()))

    # Create a list to store all the features
    features = [c,mn,si,cr,ni,mo,v,n,nb,co,w,al,ti,yield_strength]

  
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Steel quality detected...")

        # Print the output according to the prediction
        if (prediction < 1200):
            st.error("Poor! Class D Steel 😫")
        elif (prediction> 1200 and prediction < 1800):
            st.warning("Average Quality Steel. Class C Steel")
        elif (prediction>1800 and prediction < 2300):
            st.warning("Good Quality Steel. Class B Steel")
        elif (prediction>2400):
            st.success("Best Quality Steel! Class A 😎")
        
        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", round((score*100),2),"%")
