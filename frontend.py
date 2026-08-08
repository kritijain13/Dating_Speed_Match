import streamlit as st
import requests

# ----------------------------
# Config
# ----------------------------
API_URL = "http://dating-backend:8000/predict"

st.set_page_config(
    page_title="Dating Speed Match",
    layout="wide"
)

st.title("💖 Dating Speed Match Prediction")

st.write("Fill all details and click Predict Match.")

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.header("Backend")

api_url = st.sidebar.text_input(
    "API URL",
    value=API_URL
)

# ----------------------------
# Form
# ----------------------------

with st.form("prediction_form"):

    st.header("Basic Details")

    male_age = st.number_input("Male Age", value=25)
    female_age = st.number_input("Female Age", value=23)
    age_gap = st.number_input("Age Gap", value=2)

    same_race = st.selectbox("Same Race", [0, 1])
    same_field = st.selectbox("Same Field", [0, 1])

    shared_interests = st.number_input(
        "Shared Interests",
        value=5.0
    )

    st.header("Female Ratings")

    attr_of_female = st.number_input("Female Attractiveness", value=5.0)
    sinc_of_female = st.number_input("Female Sincerity", value=5.0)
    intel_of_female = st.number_input("Female Intelligence", value=5.0)
    fun_of_female = st.number_input("Female Fun", value=5.0)
    amb_of_female = st.number_input("Female Ambition", value=5.0)

    st.header("Male Ratings")

    attr_of_male = st.number_input("Male Attractiveness", value=5.0)
    sinc_of_male = st.number_input("Male Sincerity", value=5.0)
    intel_of_male = st.number_input("Male Intelligence", value=5.0)
    fun_of_male = st.number_input("Male Fun", value=5.0)
    amb_of_male = st.number_input("Male Ambition", value=5.0)

    st.header("Preferences")

    male_pref_attr = st.number_input("Male Preference Attractiveness", value=5.0)
    male_pref_intel = st.number_input("Male Preference Intelligence", value=5.0)

    female_pref_attr = st.number_input("Female Preference Attractiveness", value=5.0)
    female_pref_intel = st.number_input("Female Preference Intelligence", value=5.0)

    male_self_attr = st.number_input("Male Self Attractiveness", value=5.0)
    female_self_attr = st.number_input("Female Self Attractiveness", value=5.0)

    st.header("Lifestyle")

    male_goes_out = st.selectbox(
        "Male Goes Out",
        [0, 1, 2, 3, 4]
    )

    female_goes_out = st.selectbox(
        "Female Goes Out",
        [0, 1, 2, 3, 4]
    )

    male_decision = st.selectbox(
        "Male Decision",
        [0, 1]
    )

    female_decision = st.selectbox(
        "Female Decision",
        [0, 1]
    )

    submit = st.form_submit_button("💘 Predict Match")

# ----------------------------
# Prediction
# ----------------------------

if submit:

    payload = {
        "male_age": male_age,
        "female_age": female_age,
        "age_gap": age_gap,
        "same_race": same_race,
        "same_field": same_field,
        "shared_interests": shared_interests,

        "attr_of_female": attr_of_female,
        "sinc_of_female": sinc_of_female,
        "intel_of_female": intel_of_female,
        "fun_of_female": fun_of_female,
        "amb_of_female": amb_of_female,

        "attr_of_male": attr_of_male,
        "sinc_of_male": sinc_of_male,
        "intel_of_male": intel_of_male,
        "fun_of_male": fun_of_male,
        "amb_of_male": amb_of_male,

        "male_pref_attr": male_pref_attr,
        "male_pref_intel": male_pref_intel,
        "female_pref_attr": female_pref_attr,
        "female_pref_intel": female_pref_intel,

        "male_self_attr": male_self_attr,
        "female_self_attr": female_self_attr,

        "male_goes_out": male_goes_out,
        "female_goes_out": female_goes_out,

        "male_decision": male_decision,
        "female_decision": female_decision
    }
    st.subheader("Payload")
    st.json(payload)

    try:

        response = requests.post(
            api_url,
            json=payload
        )

        response.raise_for_status()

        result = response.json()

        prediction = result["Prediction"]

        if prediction == 1:

            st.success("❤️ Match Found")

            st.balloons()

        else:

            st.error("💔 No Match")

    except Exception as e:

        st.error(str(e))