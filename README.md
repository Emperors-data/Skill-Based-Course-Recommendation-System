#Name- Skill-Based Course Recommendation System

This is a simple yet powerful AI-based course recommender I built to help learners find the best Coursera courses based on their skills and learning level. 
It uses text similarity (TF-IDF) to understand what users are looking for and suggests the most relevant courses in real time through a clean Gradio UI.

#Features-
- Search Coursera courses by *skill* (e.g., Python, Data Analytics, Machine Learning).
- Filter by difficulty level (Beginner / Intermediate / Advanced).
- Shows top course recommendations with ratings and universities.
- Direct clickable links to Coursera course pages.
- Built using Python, Pandas, and Gradio.

#Tech Stack-
| Component | Technology |
|------------|-------------|
| Frontend UI | Gradio |
| Backend | Python |
| Data | [Coursera Course Dataset (CSV)](https://www.kaggle.com/datasets/khusheekapoor/coursera-courses-dataset-2021) |
| Libraries | Pandas, Scikit-learn, Gradio, Numpy |

How It Works
1. The user enters a skill or keyword (e.g., Machine Learning).
2. The system uses TF-IDF vectorization to compare the input with the course descriptions.
3. It then calculates similarity scores and returns the top 5–10 most relevant courses.
4. Results include the course name, university, difficulty level, rating, and a clickable Coursera link.


#Run Locally-

1.Clone Repository-

    git clone https://github.com/<your-username>/Skill-Based-Course-Recommendation-System.git
    cd Skill-Based-Course-Recommendation-System

2.Install Dependencies-

    pip install -r requirements.txt

3.Run-

    Python App.py

#Folder Structure-

Skill-Based-Course-Recommendation-System
│
├── app.py
├── Coursera.csv
├── requirements.txt
├── README.md
└── Skill_Based_Course_Recommender01.ipynb 

#Future Ideas-

Add more learning platforms (Udemy, edX).
Use semantic embeddings (BERT, Sentence Transformers) for smarter matching.
Include personalized recommendations based on user history.

#Acknowledgments

Dataset: Coursera public course dataset-https://www.kaggle.com/datasets/khusheekapoor/coursera-courses-dataset-2021
Libraries: Pandas, Scikit-learn, Numpy, Gradio

