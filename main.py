import pandas as pd
import mlflow.pyfunc




# test_data = pd.DataFrame({
#     "male_age":[28],
#     "female_age":[26],
#     "age_gap":[2],
#     "same_race":[0],
#     "same_field":[1],
#     "shared_interests":[7.5],
#     "attr_of_female":[8.0],
#     "sinc_of_female":[7.5],
#     "intel_of_female":[8.5],
#     "fun_of_female":[7.0],
#     "amb_of_female":[6.5],
#     "attr_of_male":[8.2],
#     "sinc_of_male":[7.8],
#     "intel_of_male":[8.0],
#     "fun_of_male":[7.5],
#     "amb_of_male":[7.0],
#     "male_pref_attr":[25.0],
#     "male_pref_intel":[20.0],
#     "female_pref_attr":[30.0],
#     "female_pref_intel":[18.0],
#     "male_self_attr":[8.0],
#     "female_self_attr":[7.0],
#     "male_goes_out":[3],      # often
#     "female_goes_out":[2],    # sometimes
#     "male_decision":[1],
#     "female_decision":[1]
# })

# prediction = model.predict(test_data)

# print(prediction)


from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import mlflow.pyfunc

app = FastAPI()

# Load Model
model = mlflow.pyfunc.load_model(
    "mlruns/1/models/m-ff9fc7d8768347c7b638d481dcae6359/artifacts"
)
class DatingData(BaseModel):
    male_age: int
    female_age: int
    age_gap: int
    same_race: int
    same_field: int
    shared_interests: float
    attr_of_female: float
    sinc_of_female: float
    intel_of_female: float
    fun_of_female: float
    amb_of_female: float
    attr_of_male: float
    sinc_of_male: float
    intel_of_male: float
    fun_of_male: float
    amb_of_male: float
    male_pref_attr: float
    male_pref_intel: float
    female_pref_attr: float
    female_pref_intel: float
    male_self_attr: float
    female_self_attr: float
    male_goes_out: int
    female_goes_out: int
    male_decision: int
    female_decision: int


@app.post("/predict")
def predict(data: DatingData):

    df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(df)

    return {
        "Prediction": int(prediction[0])
    }