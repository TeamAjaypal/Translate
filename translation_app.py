import streamlit as st
from googletrans import Translator

def main():
    st.title("Language Translation App")

    # Workaround for token acquisition issue
    from googletrans import client
    client.Translator().token_acquirer._tokens = {}

    # Create a Translator object
    translator = Translator()

    # Input text box for user to enter a sentence in English
    input_text = st.text_area("Enter a sentence in English:", "")

    if st.button("Translate"):
        if input_text:
            try:
                # Translate the input sentence to Hindi and Punjabi
                translated_en = translator.translate(input_text, dest="en").text
                translated_hi = translator.translate(input_text, dest="hi").text
                translated_pa = translator.translate(input_text, dest="pa").text

                # Display the translated sentences
                st.subheader("English:")
                st.write(translated_en)

                st.subheader("Hindi:")
                st.write(translated_hi)

                st.subheader("Punjabi:")
                st.write(translated_pa)

            except Exception as e:
                st.error("Translation failed. Please try again.")
                st.error(str(e))  # Display the actual error message for debugging

if __name__ == "__main__":
    main()
