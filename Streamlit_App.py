# This is a Streamlit App

import streamlit as st
import pickle

# Save and Load Model
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


# A custom function for predicting the values
def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return prediction


def main():
    st.title("Bank Note Authenticator 💵 ")

    st.markdown("""
    ## **Dataset Information : **
    **Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.**
    """,True)
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Note Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance", "Variance")
    skewness = st.text_input("skewness", "skewness")
    curtosis = st.text_input("curtosis", "curtosis")
    entropy = st.text_input("entropy", "entropy")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        if result == 0:
            st.success('The Banknotes are Genuine ✔️')
        else:
            st.error('The Banknotes are Forged ⚔️')
            #st.success('The output is {}'.format(result))

    if st.button("About"):
        st.markdown("""**Built with ❤️ by Ritesh**""")


if __name__ == '__main__':
    main()
