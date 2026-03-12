# ❤️ Heart Disease Risk Prediction System

## 📌 Project Overview

The **Heart Disease Risk Prediction System** is a Machine Learning web application that predicts the risk of heart disease based on a patient's health parameters.

This project uses a trained machine learning model to analyze important medical features such as **age, cholesterol level, blood pressure, chest pain type, and heart rate** to determine whether a person has a **high or low risk of heart disease**.

The application is built using **Python, Machine Learning, and Streamlit** to provide an interactive user interface for predictions and data visualizations.

---

# 🚀 Live Features

✔️ Predict heart disease risk using patient health details
✔️ Interactive **Streamlit web interface**
✔️ Risk probability score visualization
✔️ Dataset visualizations
✔️ Correlation heatmap for feature relationships
✔️ Clean and easy-to-use UI

---

# 📂 Project Structure

```
Heart_Disease_Predictor/
│
├── app.py                # Streamlit web application
├── heart.csv             # Dataset used for training
├── heart_model.pkl       # Trained machine learning model
├── README.md             # Project documentation
```

---

# 📊 Dataset Information

The dataset contains medical attributes used to predict heart disease.

| Feature  | Description                              |
| -------- | ---------------------------------------- |
| age      | Age of the patient                       |
| sex      | Gender (Male/Female)                     |
| cp       | Chest pain type                          |
| trestbps | Resting blood pressure                   |
| chol     | Serum cholesterol level                  |
| fbs      | Fasting blood sugar                      |
| restecg  | Resting electrocardiographic results     |
| thalach  | Maximum heart rate achieved              |
| exang    | Exercise-induced angina                  |
| oldpeak  | ST depression induced by exercise        |
| slope    | Slope of the ST segment                  |
| ca       | Number of major vessels                  |
| thal     | Thalassemia type                         |
| target   | Heart disease presence (0 = No, 1 = Yes) |

---

# ⚙️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Streamlit

---

# 🧠 Machine Learning Model

This project uses a **Supervised Machine Learning model** trained on heart disease data.

The model predicts:

* **0 → Low Risk of Heart Disease**
* **1 → High Risk of Heart Disease**

The prediction is based on multiple medical parameters entered by the user.

---

# 🖥️ Application Interface

The Streamlit application allows users to:

### 1️⃣ Enter Patient Health Details

Using the sidebar inputs:

* Age
* Sex
* Chest Pain Type
* Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* ECG Results
* Heart Rate
* Exercise Induced Angina
* ST Depression
* Major Vessels
* Thalassemia

### 2️⃣ Generate Prediction

The system calculates:

* Heart disease prediction
* Risk probability score
* Visualization of prediction probabilities

### 3️⃣ Data Visualization

The app also includes dataset analysis:

* Age distribution
* Heart disease distribution
* Cholesterol vs Age scatter plot
* Feature correlation heatmap

---

# ▶️ How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/harikrishhh07/Heart_Disease_Predictor.git
```

---

## 2️⃣ Navigate to the Project Folder

```
cd Heart_Disease_Predictor
```

---

## 3️⃣ Install Required Libraries

```
pip install pandas numpy matplotlib scikit-learn streamlit joblib
```

---

## 4️⃣ Run the Streamlit Application

```
streamlit run app.py
```

---

# 📊 Example Output

After entering the patient details, the system will display:

* Heart Disease Risk (High / Low)
* Risk Probability Percentage
* Prediction probability chart
* Dataset visualizations

---

# 🔮 Future Improvements

* Deploy the application on **Streamlit Cloud / Render / AWS**
* Improve model accuracy using advanced algorithms
* Add more medical features
* Integrate real-time patient data
* Create a mobile-friendly interface

---

# 👨‍💻 Author

**E. Harikrishna**

Machine Learning Enthusiast | Python Developer

---

# ⭐ Support

If you like this project, please **star ⭐ the repository** and share it with others.

---

# 📜 License

This project is open-source and available under the **MIT License**.
