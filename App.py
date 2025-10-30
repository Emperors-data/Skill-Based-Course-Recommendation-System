import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import gradio as gr


df = pd.read_csv("Coursera.csv")

# Normalize and rename columns to match logic
df.columns = df.columns.str.strip().str.lower()
df = df.rename(columns={
    'course name': 'course_name',
    'difficulty level': 'level',
    'course url': 'url'
})

# Fill missing text fields to avoid errors
df['skills'] = df['skills'].fillna('')
df['course_name'] = df['course_name'].fillna('Unknown Course')

# Prepare TF-IDF model on the "skills" column
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['skills'])

#Creating a function to recommend courses
def recommend_courses(skill, difficulty):
    if not skill or skill.strip() == "":
        return "⚠️ Please enter a skill to get recommendations."

    results = df[df['skills'].str.contains(skill, case=False, na=False)]

    if difficulty != "All":
        results = results[results['level'].str.contains(difficulty, case=False, na=False)]

    if results.empty:
        return f"😕 No courses found for '{skill}' at '{difficulty}' level."

    if 'rating' in results.columns:
        results = results.sort_values(by='rating', ascending=False)

    top_courses = results.head(5)

    html = "<div style='display: flex; flex-wrap: wrap; gap: 16px;'>"
    for _, row in top_courses.iterrows():
        title = row.get('course_name', 'Unknown Course')
        rating = row.get('rating', 'N/A')
        level = row.get('level', 'N/A')
        url = row.get('url', '#')

        html += f"""
        <div style='background: #1e1e2f; padding: 16px; border-radius: 12px; width: 300px; box-shadow: 0 2px 8px rgba(0,0,0,0.3);'>
            <h3 style='color:#8ab4f8; margin-bottom:8px; font-size:18px;'><a href='{url}' target='_blank' style='color:#8ab4f8; text-decoration:none;'>{title}</a></h3>
            <p style='color:#e8eaed; margin:4px 0;'>Rating: {rating}</p>
            <p style='color:#e8eaed; margin:4px 0;'>Level: {level}</p>
        </div>
        """
    html += "</div>"

    return html

# Gradio Interface
with gr.Blocks(theme=gr.themes.Soft(primary_hue="indigo", secondary_hue="blue")) as demo:
    gr.Markdown(
        """
        <h1 style='text-align:center;'>Skill-Based Course Recommendation System</h1>
        <p style='text-align:center;'>Find the best Coursera courses that match your skills and difficulty level!</p>
        """
    )

    with gr.Row():
        skill_input = gr.Textbox(label="Enter a Skill (e.g., Python, Data Analytics, Machine Learning)", placeholder="e.g. Python")
        difficulty_input = gr.Dropdown(choices=["All", "Beginner", "Intermediate", "Advanced"], label="Difficulty Level", value="All")

    submit_btn = gr.Button("Get Recommendations", variant="primary")
    clear_btn = gr.Button("Clear")

    output = gr.HTML(label="Recommended Courses")

    submit_btn.click(fn=recommend_courses, inputs=[skill_input, difficulty_input], outputs=output)
    clear_btn.click(fn=lambda: "", inputs=None, outputs=output)

    gr.Examples(
        examples=["Python", "Machine Learning", "Data Analytics", "Cloud Computing"],
        inputs=skill_input
    )

demo.launch(share=True)