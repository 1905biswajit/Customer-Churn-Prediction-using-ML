import pandas as pd
import streamlit as st
import streamlit_lottie
import pickle
from streamlit_option_menu import option_menu



@st.cache_resource
def model():
    clf = pickle.load(open(r"C:\Users\BISWAJIT KAR\ML PROJECT FILE\vt_clf.pkl",'rb'))
    return clf

with st.sidebar:
    opt_selected	=	option_menu(
            menu_title=	"Main	Menu",
            options	=	["Home",'Info'],
            icons	=	['house-fill','info-circle-fill'],
            default_index	=	0,
            menu_icon	=	"tv-fill",
            orientation=	"vertical")


if opt_selected == 'Home':

    st.markdown("## **:green[Welcome]**")
    st.markdown('''**This is a :orange[Customer Churn Prediction tool] !!**\
              \n\n**Please fill out the form below with your relevant\
              details. By providing us with your information, we'l\
             l analyze various factors to predict whether you're likely to churn as a customer.\
              This prediction will help us tailor our services and offers to better meet your needs and preferences.\
              Thank you for participating!**''')
    st.write('---')
    with st.form("telco_form"):
        st.markdown('## :green[Telecom Form]')
        col1, col2= st.columns(2)

        with col1:
            gender= st.selectbox("Select your gender", ('Male', 'Female'))
            SeniorCitizen = st.selectbox("Are your senior citizen", ('Yes', 'No'))
            Partner = st.selectbox("Do you have partner", ('Yes','No'))
            Dependents = st.selectbox("Do you have any dependents", ('Yes','No'))
            PhoneService = st.selectbox("Do you have Phone Service", ("Yes","No"))
            MultipleLines = st.selectbox("Multiple Lines", ('No phone service', 'No', 'Yes'))
            InternetService= st.selectbox('Internet Service?', ('DSL', 'Fiber optic', 'No'))
            OnlineSecurity= st.selectbox('Online security', ('Yes', 'No'))
            OnlineBackup = st.selectbox('Online Backup', ('Yes', 'No'))
            tenure = st.number_input("Months stayed with company", 1,100,1,1)
        
        with col2:
            DeviceProtection = st.selectbox('Device Protection', ('Yes','No'))
            TechSupport= st.selectbox("Tech Support", ('Yes', 'No'))
            StreamingTV= st.selectbox("StreamingTV", ('Yes', 'No'))
            StreamingMovies = st.selectbox("Streaming Movies", ('Yes', 'No'))
            Contract = st.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'))
            PaperlessBilling = st.selectbox("Paperless Billing", ('Yes', 'No'))
            PaymentMethod = st.selectbox("Payment Method", ('Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'))
            MonthlyCharges = st.number_input("Monthly Charges", 0, 1500, 10, 2)
            TotalCharges = st.number_input("Total Charges", 0,10000,500, 100 )
        formbutton = st.form_submit_button('Predict')


    if formbutton:
        tenure_group= ''
        if 1 <= tenure <= 12:
            tenure_group = '1 - 12'
        elif 13 <= tenure <= 24:
            tenure_group = '13 - 24'
        elif 25 <= tenure <= 36:
            tenure_group = '25 - 36'
        elif 37 <= tenure <= 48:
            tenure_group = '37 - 48'
        elif 49 <= tenure <= 60:
            tenure_group = '49 - 60'
        else:
            tenure_group = '61 - 72'


        data = {
            'gender': gender,
            'SeniorCitizen': 1 if SeniorCitizen == 'Yes' else 0,
            'Partner': Partner,
            'Dependents': Dependents,
            'PhoneService': PhoneService,
            'MultipleLines': MultipleLines,
            'InternetService': InternetService,
            'OnlineSecurity': OnlineSecurity,
            'OnlineBackup': OnlineBackup,
            'DeviceProtection': DeviceProtection,
            'TechSupport': TechSupport,
            'StreamingTV': StreamingTV,
            'StreamingMovies': StreamingMovies,
            'Contract': Contract,
            'PaperlessBilling': PaperlessBilling,
            'PaymentMethod': PaymentMethod,
            'MonthlyCharges': MonthlyCharges,
            'TotalCharges': TotalCharges,
            'tenure_group': tenure_group
        }

        test_data= pd.DataFrame([data])
        predictor = model()

        result = predictor.predict(test_data)
    
        st.write('---')

        st.markdown('''## :green[**Prediction**]''')
            
        st.write('---')
        if result[0] == 0:
            st.markdown('### :orange[Customer is not likely to churn]')
        else:
            st.markdown('### :orange[Customer is likely to churn]')
else:
    st.title(":green[Welcome to the Customer Churn Prediction Tool!]")

    # Introduction
    st.markdown("""
    In today's competitive telecommunications landscape, retaining customers is crucial for sustained business success. Customer churn, or the rate at which customers discontinue their services, presents a significant challenge for companies seeking to maintain long-term profitability and growth. Understanding the factors that contribute to churn is essential for devising effective retention strategies and ensuring customer satisfaction.
    """)

    # Overview of the Tool
    st.header(":orange[About Our Customer Churn Prediction Tool]")
    st.markdown("""
    Our Customer Churn Prediction tool is designed to harness the power of machine learning to analyze customer data and predict the likelihood of churn. By inputting your relevant information into the form below, you enable our predictive models to assess various factors that may influence your decision to continue or discontinue your services with us.
    """)

    # Form Details
    st.subheader(":orange[Information Collected]")
    st.markdown("""
    The form collects essential information such as your tenure with our company, monthly charges, and senior citizen status. These attributes serve as valuable predictors in our churn prediction model, allowing us to identify patterns and trends that may indicate a higher likelihood of churn.
    """)

    # Explanation of the Process
    st.subheader(":orange[How It Works]")
    st.markdown("""
    Once you submit the form, our algorithm will process your data and generate a churn prediction score. This score represents the estimated probability of you churning as a customer. Armed with this insight, we can tailor our services and engagement strategies to better meet your needs and preferences, ultimately enhancing your experience and increasing your satisfaction with our company.
    """)

    # Benefits
    st.header(":orange[Why Participate?]")
    st.markdown("""
    Your participation in this prediction exercise not only benefits you by providing personalized insights but also contributes to our ongoing efforts to improve customer retention and loyalty. By better understanding the factors driving churn, we can proactively address potential issues, strengthen our customer relationships, and foster long-term partnerships.
    """)

    # Conclusion
    st.subheader(":orange[Thank You]")
    st.markdown("""
    Thank you for choosing to engage with our Customer Churn Prediction tool. Your feedback and participation are invaluable as we continue to innovate and evolve in our mission to deliver exceptional service and value to our customers. Together, we can navigate the challenges of customer churn and build a stronger, more resilient telecommunications ecosystem.

    Let's embark on this journey towards enhanced customer satisfaction and mutual success!
    """)

    st.subheader(":orange[Creator]")
    st.markdown('''
    Hello everyone!!, Myself Biswajit Kar the creator of this customer churn prediction tool.\
    This tool was made as a part of the Machine Learning mini project that I got as a student of VIT-AP.\
    A numerous machine learning algorithms were used to make predictions whether a customer will churn or not.
                
    You can follow me here:
                
    [LinkedIN](https://www.linkedin.com/in/biswajit-kar-627924261/)\n
    [GitHub](https://github.com/1905biswajit)
    
''')
