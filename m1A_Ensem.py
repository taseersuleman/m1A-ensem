import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

selected2 = option_menu(None, ["Home", "Predictor", "Dataset", "Citations"],
                        icons=['house', 'search', 'list-task', 'book'],
                        menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

if selected2 == "Home":
    st.header("iDHU-Ensem")
    #st.subheader("The DHU-Pred is a web-server for the prediction of Dihydrouridine in transfer RNA (tRNA) "
     #            "modifications.")
    st.write("Dihydrouridine (D) is one of the most significant post transcriptional modifications (PTM) that is abundantly found in eukaryotes. This modification is involved in the folding and conformational flexibility of transfer RNA (tRNA) and is also responsible for pulmonary carcinogenesis in humans. The identification of D sites was carried out through conventional laboratory methods; however, those were expensive and time-consuming. The availability of sequence data helped in the development of computationally intelligent models that enhance the identification of D sites. The current study focused on the identification of D sites in tRNA sequences using ensemble models such as bagging, boosting, and stacking. The models were evaluated through an independent set test and k-fold cross validation. The results revealed that the stacking ensemble model outperformed all the ensemble models by revealing 0.98 accuracy, 0.98 specificity, 0.97 sensitivity, and 0.92 Matthews Correlation Coefficient. The proposed model, iDHU-Ensem, was also compared with preexisting predictors using an independent test. The accuracy scores have shown that the proposed model in this research study performed better than available predictors. An online web-based server for the proposed model was also made for the researchers."
             )
    #image = Image.open('pseudo.PNG')
    #st.image(image, width=400)

elif selected2 == "Predictor":
    #st.subheader("Predictor Page")
    import predictor

    exec(open('predictor.py').read())


elif selected2 == "Dataset":
    #st.subheader("Data Set")
    st.info("Poisitive Samples (tRNA sequences with D-sites)")
    with open("Sup1.fasta", "rb") as file:
        btn = st.download_button(
            label="Download file",
            data=file,
            file_name="Sup1.fasta",
            mime=""
        )
    st.info("Negative Samples (tRNA sequences with Non-D sites")
    with open("Sup2.fasta", "rb") as file:
        btn = st.download_button(
            label="Download file",
            data=file,
            file_name="Sup2.fasta",
            mime=""
        )
