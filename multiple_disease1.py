# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 21:58:59 2023

@author: ssris
"""

import pickle
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Load the saved models (assuming they were saved in pickle format)
#diabetes_model = pickle.load(open('D:/Multiple Disease Prediction/saved_modules/diabetes_model.sav'))
#heart_disease_model = pickle.load(open('D:/Multiple Disease Prediction/saved_modules/heart_disease_model.sav'))
#parkinsons_disease_model = pickle.load(open('D:/Multiple Disease Prediction/saved_modules/parkinsons_disease_model.sav'))
#with open('D:/Multiple Disease Prediction/saved_modules/diabetes_model1.sav', 'rb') as file:
    #diabetes_model = pickle.load(file)

#with open('D:/Multiple Disease Prediction/saved_modules/heart_disease_model1.sav', 'rb') as file:
    #heart_disease_model = pickle.load(file)

#with open('D:/Multiple Disease Prediction/saved_modules/parkinsons_disease_model.sav', 'rb') as file:
#parkinsons_disease_model = pickle.load(file)

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))


# Sidebar for navigation
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['heart','activity',  'person'],
                           default_index=0)
#show_help = st.sidebar.checkbox("Show Help")
#with st.beta_expander("Help", expanded=False):
   # st.write("This is the help section. Add information about the page here.")
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction System ')
    #info_col, form_col = st.beta_columns(2)
    
   
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
       Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level (mm)')
    
    with col3:
       BloodPressure = st.text_input('Blood Pressure value (mmHg)')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value (mm)')
    
    with col2:
        Insulin = st.text_input('Insulin Level (IU/mL) ')
    
    with col3:
        BMI = st.text_input('BMI value (kg/m2)')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
        
        #code for Prediction
        diab_diagnosis =''
        
        #creating a button for Prediction
        
        if st.button('Diabetes Test Result'):
            st.write("Input Values:")
            st.write("Input Values:")
            st.write(f"Number of Pregnancies: {Pregnancies}")
            st.write(f"Glucose Level: {Glucose}")
            st.write(f"Blood Pressure value: {BloodPressure}")
            st.write(f"Skin Thickness value: {SkinThickness}")
            st.write(f"Insulin Level: {Insulin}")
            st.write(f"BMI value: {BMI}")
            st.write(f"Diabetes Pedigree Function value: {DiabetesPedigreeFunction}")
            st.write(f"Age of the Person: {Age}")
            diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
            st.write(f"Diabetes Prediction Value: {diab_prediction[0]}")
            if (diab_prediction[0]==1):
                diab_diagnosis = 'The person is Diabetic'
                
            else:
                diab_diagnosis = 'The person is not Diabetic'
                
            # Add a disclaimer message
            st.write("""
        **Disclaimer:**
        This test result is generated by a machine learning model and should not be considered a definitive diagnosis. It is highly recommended to consult with a qualified healthcare professional for a thorough evaluation and diagnosis.
         """)        
        st.success(diab_diagnosis) 
        #st.text('-by Srishty sharma')
     # Display information about the parameters
    st.write("Information about Parameters:")
    st.write("- Number of Pregnancies: This is a count, so there's no specific normal range. It depends on the individual.")
    st.write("- Skin Thickness value (mm): Normal values can vary, but skinfold thickness measurements are often taken at specific body locations, and the range might be between 10mm to 30mm.")
    st.write("- Diabetes Pedigree Function value: The value is a score, and there isn't a strict normal range. Higher scores generally indicate a higher likelihood of diabetes based on family history.")
    st.write("- Glucose Level (mm): Fasting blood glucose levels are typically below 100 mg/dL (5.6 mmol/L) for normal. Values between 100-125 mg/dL (5.6-6.9 mmol/L) may indicate prediabetes.")
    st.write("- Insulin Level (IU/mL): Normal fasting insulin levels can vary, but they are typically in the range of 2-25 μIU/mL.")
    st.write("- Age of the Person: There's no specific normal range for age. It depends on the context of the individual's health assessment.")
    st.write("- Blood Pressure value (mmHg): Normal blood pressure is usually considered to be around 120/80 mmHg. The American Heart Association defines normal blood pressure as less than 120/80 mmHg.")
    st.write("- BMI value (kg/m2): BMI ranges include Underweight (less than 18.5), Normal weight (18.5 to 24.9), Overweight (25 to 29.9), and Obesity (30 or greater).")
      
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('Thal')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
         # Add a disclaimer message
        st.write("""
        **Disclaimer:**
        This test result is generated by a machine learning model and should not be considered a definitive diagnosis. It is highly recommended to consult with a qualified healthcare professional for a thorough evaluation and diagnosis.
         """)   
    st.success(heart_diagnosis)
    st.write("### Information about Parameters:")
    #st.write("- Age: Age of the individual.")
    #st.write("- Normal Range: There isn't a strict normal range. It depends on the context of the individual's health assessment.")
   # image_path = "D:/Multiple Disease Prediction/multiple_prediction/ECG.jpg"

# Display the image
   # st.image(image_path, caption='ECG Image', use_column_width=True)  
    st.write("- Resting Blood Pressure: Resting blood pressure measured in mmHg, Normal blood pressure is usually considered to be around 120/80 mmHg. The American Heart Association defines normal blood pressure as less than 120/80 mmHg.")
    #st.write("- Normal Range: Normal blood pressure is usually considered to be around 120/80 mmHg. The American Heart Association defines normal blood pressure as less than 120/80 mmHg.")
        
    st.write("- Resting Electrocardiographic results: Results of the resting electrocardiogram (ECG or EKG).  0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy.")
    #st.write("- Normal Value: 0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy.")
        
    st.write("- ST depression induced by exercise: Depression induced by exercise relative to rest,The interpretation depends on the specific measurement and context. It's generally evaluated in conjunction with other factors.")
    #st.write("- Normal Value: The interpretation depends on the specific measurement and context. It's generally evaluated in conjunction with other factors.")
        
    st.write("- Thal:  0 = normal, 1 = fixed defect (likely indicating scar tissue), 2 = reversible defect (potentially indicating ischemia).")
    #st.write("- Normal Value: 0 = normal, 1 = fixed defect (likely indicating scar tissue), 2 = reversible defect (potentially indicating ischemia).")
        
    st.write("- Sex: Gender of the individual,0 = Female, 1 = Male")
   # st.write("- Normal Value: 0 = Female, 1 = Male.")
        
    st.write("- Serum Cholestoral in mg/dl: Serum cholesterol level in mg/dl, Desirable levels are below 200 mg/dL. However, this is often assessed in conjunction with other risk factors.")
    #st.write("- Normal Range: Desirable levels are below 200 mg/dL. However, this is often assessed in conjunction with other risk factors.")
        
    st.write("- Maximum Heart Rate achieved: Maximum heart rate achieved during exercise, Varies based on age, but a general rule of thumb is around 220 minus age.")
   # st.write("- Normal Range: Varies based on age, but a general rule of thumb is around 220 minus age.")
        
    st.write("- Slope of the peak exercise ST segment: Slope of the peak exercise ST segment, 0 = upsloping, 1 = flat, 2 = downsloping.")
    #st.write("- Normal Value: 0 = upsloping, 1 = flat, 2 = downsloping.")
        
    st.write("- Chest Pain types: Type of chest pain experienced, The interpretation may vary, but 0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic.")
   # st.write("- Normal Value: The interpretation may vary, but 0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic.")
        
    st.write("- Fasting Blood Sugar > 120 mg/dl: Fasting blood sugar level, Normal fasting blood sugar is typically below 100 mg/dL. Levels between 100-125 mg/dL may indicate prediabetes.")
   # st.write("- Normal Range: Normal fasting blood sugar is typically below 100 mg/dL. Levels between 100-125 mg/dL may indicate prediabetes.")
        
    st.write("- Exercise Induced Angina: Presence of exercise-induced angina , Normal Value: 0 = No, 1 = Yes.")
    #st.write("- Normal Value: 0 = No, 1 = Yes.")
#Parkisons Prediction Page
if (selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction System')    
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP RAP')
        
    with col2:
        PPQ = st.text_input('MDVP PPQ')
        
    with col3:
        DDP = st.text_input('Jitter DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer APQ5')
        
    with col3:
        APQ = st.text_input('MDVP APQ')
        
    with col4:
        DDA = st.text_input('Shimmer DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_disease_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
         # Add a disclaimer message
        st.write("""
        **Disclaimer:**
        This test result is generated by a machine learning model and should not be considered a definitive diagnosis. It is highly recommended to consult with a qualified healthcare professional for a thorough evaluation and diagnosis.
         """)   
    st.success(parkinsons_diagnosis)
    
    st.write("### Information about Parameters:")
        
    st.write("- MDVP:Fo (Hz) Fundamental frequency of the voice: The normal range can vary, but typically it's around 85-255 Hz.")
    #st.write("   - Description: Fundamental frequency of the voice.")
    #st.write("   - Normal Range: The normal range can vary, but typically it's around 85-255 Hz.")
        
    st.write("- MDVP:Fhi (Hz)Maximum pitch frequency:It can vary, but normal values are often in the range of 175-280 Hz. ")
    #st.write("   - Description: Maximum pitch frequency.")
    #st.write("   - Normal Range: It can vary, but normal values are often in the range of 175-280 Hz.")
        
    st.write("- MDVP Flo (Hz) Minimum pitch frequency :It can vary, but normal values are often in the range of 80-155 Hz. ")
   # st.write("   - Description: Minimum pitch frequency.")
    #st.write("   - Normal Range: It can vary, but normal values are often in the range of 80-155 Hz.")
    st.write("- MDVP Jitter (%)Voice jitter percentage :ormal values are typically below 1.04%")
   # st.write("   - Description: Voice jitter percentage.")
    #st.write("   - Normal Range: Normal values are typically below 1.04%.")

    st.write("- MDVP Jitter(Abs) : Absolute jitter measured in ms:Normal values are typically below 0.00006 ms")
   # st.write("   - Description: Absolute jitter measured in ms.")
    #st.write("   - Normal Range: Normal values are typically below 0.00006 ms.")

    st.write("- DVP RAP (Relative amplitude perturbation):It is a ratio, and normal values are typically below 0.005.")
   # st.write("   - Description: Relative amplitude perturbation.")
    #st.write("   - Normal Range: It is a ratio, and normal values are typically below 0.005.")

    st.write("- MDVP PPQ (Five-point period perturbation quotient):It is a ratio, and normal values are typically below 0.005")
    #st.write("   - Description: Five-point period perturbation quotient.")
    #st.write("   - Normal Range: It is a ratio, and normal values are typically below 0.005.")

    st.write("- Jitter DDP (Average absolute difference of differences between jitter cycles): It is a ratio, and normal values are typically below 0.01.")
   # st.write("   - Description: Average absolute difference of differences between jitter cycles.")
    #st.write("   - Normal Range: It is a ratio, and normal values are typically below 0.01.")

    st.write("- MDVP Shimmer (Voice shimmer):Normal values are typically below 0.18")
    #st.write("   - Description: Voice shimmer.")
    #st.write("   - Normal Range: Normal values are typically below 0.18.")

    st.write("- MDVP Shimmer(dB): Normal values are typically below 1.5 dB.")
   # st.write("    - Description: Shimmer in dB.")
    #st.write("    - Normal Range: Normal values are typically below 1.5 dB.")
    st.write("- Shimmer APQ3 (Three-point amplitude perturbation quotient):It is a ratio, and normal values are typically below 0.02.")
   # st.write("    - Description: Three-point amplitude perturbation quotient.")
    #st.write("    - Normal Range: It is a ratio, and normal values are typically below 0.02.")

    st.write("- Shimmer APQ5 (Five-point amplitude perturbation quotient): It is a ratio, and normal values are typically below 0.03.")
    #st.write("    - Description: Five-point amplitude perturbation quotient.")
    #st.write("    - Normal Range: It is a ratio, and normal values are typically below 0.03.")

    st.write("- MDVP APQ (Overall amplitude perturbation quotient):It is a ratio, and normal values are typically below 0.04.")
    #st.write("    - Description: Overall amplitude perturbation quotient.")
    #st.write("    - Normal Range: It is a ratio, and normal values are typically below 0.04.")

    st.write("- Shimmer DDA (Average absolute differences between consecutive differences in amplitude):")
    #st.write("    - Description: Average absolute differences between consecutive differences in amplitude.")
    #st.write("    - Normal Range: It is a ratio, and normal values are typically below 0.06.")

    st.write("- NHR (Noise-to-harmonics ratio):Normal values are typically below 0.03.")
    #st.write("    - Description: Noise-to-harmonics ratio.")
    #st.write("    - Normal Range: Normal values are typically below 0.03.")

    st.write("- HNR (Harmonics-to-noise ratio):Normal values are typically above 8.4.")
   # st.write("    - Description: Harmonics-to-noise ratio.")
    #st.write("    - Normal Range: Normal values are typically above 8.4.")

    st.write("- RPDE (Recurrence period density entropy):Normal values are context-dependent, but lower values are generally considered normal.")
    #st.write("    - Description: Recurrence period density entropy.")
    #st.write("    - Normal Range: Normal values are context-dependent, but lower values are generally considered normal.")

    st.write("- DFA (Detrended fluctuation analysis):Normal values are context-dependent, but lower values are generally considered normal.")
    #st.write("    - Description: Detrended fluctuation analysis.")
    #st.write("    - Normal Range: Normal values are context-dependent, but lower values are generally considered normal.")

    st.write("- spread1 (Measure of spread of fundamental frequency):Normal values are context-dependent")
    #st.write("    - Description: Measure of spread of fundamental frequency.")
    #st.write("    - Normal Range: Normal values are context-dependent.")

    st.write("- spread2 (Measure of spread of fundamental frequency):Normal values are context-dependent.")
    #st.write("    - Description: Measure of spread of fundamental frequency.")
    #st.write("    - Normal Range: Normal values are context-dependent.")

    st.write("- D2 (Correlation dimension):Normal values are context-dependent.")
    #st.write("    - Description: Correlation dimension.")
    #st.write("    - Normal Range: Normal values are context-dependent.")

    st.write("- PPE (Pitch period entropy): Normal values are context-dependent.")
    #st.write("    - Description: Pitch period entropy.")
    #st.write("    - Normal Range: Normal values are context-dependent.")
    
    #st.text('-by Srishty sharma')
