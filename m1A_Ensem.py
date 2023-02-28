import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

selected2 = option_menu(None, ["Home", "Predictor", "Dataset", "Citations"],
                        icons=['house', 'search', 'list-task', 'book'],
                        menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

if selected2 == "Home":
    st.header("m1A-Ensem")
    #st.subheader("A web-server for the prediction of 1-methyladenosine in RNA"
     #            "modifications.")
    st.write("The current study proposed a novel framework for the prediction of m1A sites using ensemble models. These models were categorized into blending, bagging, and boosting. It's worth mentioning here that RAMPred, iRNA3typeA, ISGm1A and DeepMRMP have used the same dataset for training and validation. The dataset is composed of RNA sequences belonging to three species: Homosapiens, Saccharomyces cerevisiae, Mus musculus and Schizosaccharomyces pombe. The extraction of meaningful attributes from the sequences was carried out by considering the position and formation of nucleotide bases. Statistical moments were calculated that helped in feature dimensionality reduction in few matrics developed for attributes extraction. The performance of these ensemble models was evaluated through k-fold cross validation and independent set testing."
             )
    #image = Image.open('pseudo.PNG')
    #st.image(image, width=400)

elif selected2 == "Predictor":
    #st.subheader("Predictor Page")
    import predictor

    exec(open('predictor.py').read())


elif selected2 == "Dataset":
    #st.subheader("Data Set")
    st.info("Positive Samples (modified m1A-sites)")
    with open("Sup1", "rb") as file:
        btn = st.download_button(
            label="Download file",
            data=file,
            file_name="Sup1",
            mime=""
        )
    st.info("Negative Samples (Non-modified m1A sites")
    with open("Sup2", "rb") as file:
        btn = st.download_button(
            label="Download file",
            data=file,
            file_name="Sup2",
            mime=""
        )
