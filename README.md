# LearnMate – AI-Powered Personalized Roadmap Generator 🎓

LearnMate is an intelligent AI-powered learning assistant that generates a 10-week personalized course roadmap based on student inputs like:
- Skill level
- Interests (e.g., Frontend, UI/UX)
- Career goals
- Weekly study hours

🔗 Powered by IBM Granite via Watsonx  
🧠 Built using Streamlit + Python

## 🔧 Tech Stack
- Streamlit (Frontend UI)
- IBM Watsonx AI (Granite model)
- Python + Prompt Engineering
- IBM Cloud Lite (for hosting Granite)

## 🚀 Try It Live
Click here: [Live App URL Will Go Here]

## 📥 Input Form
- Name
- Skill level (Beginner, Intermediate, Advanced)
- Interests (multi-select)
- Weekly hours
- Career goal

## 📚 Output
- Custom roadmap (Week 1 to Week 10)
- Aligned to interests and skill level

---

## ✅ How to Run Locally
```bash
pip install -r requirements.txt
streamlit run learnmate_ui.py
```

### ⚠️ Environment Variables

Create a `.env` file in your project root (do NOT commit this file) with:

```
IBM_API_KEY=your_actual_api_key
IBM_PROJECT_ID=your_actual_project_id
IBM_MODEL_ID=ibm/granite-3-3-8b-instruct
IBM_URL=https://us-south.ml.cloud.ibm.com
```

- Your `.env` file is **private** and should be listed in `.gitignore`.

---

### ✅ Step 3: Push to GitHub

- Make sure all files are committed and pushed:
  - `learnmate_ui.py`
  - `ai_models/granite_ai_roadmap.py`
  - `requirements.txt`
  - `README.md`
  - `.gitignore`
- **Do NOT push your `.env` file.**

---

### 🌐 Step 4: Deploy on Streamlit Cloud

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Sign in with your GitHub
3. Click **“New App”**
4. Choose your GitHub repo
5. Set the file path to:
