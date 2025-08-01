import streamlit as st
from ai_models.granite_ai_roadmap import generate_ai_roadmap


# Page title
st.title("👩‍🎓 LearnMate - Personalized Course Path Generator")

# Sidebar for inputs
st.sidebar.header("📝 Fill Your Learning Preferences")

# Inputs
name = st.sidebar.text_input("Your Name")
skill_level = st.sidebar.selectbox("Your Skill Level", ["Beginner", "Intermediate", "Advanced"])
interests = st.sidebar.multiselect("Select Your Interests", ["Frontend Development", "Cybersecurity", "UI/UX Design", "AI/ML", "Data Science"])
weekly_hours = st.sidebar.slider("How many hours can you study per week?", 1, 40, 6)
career_goal = st.sidebar.text_area("What is your career goal?")

# Submit Button
if st.sidebar.button("Generate Roadmap"):
    if name and interests and career_goal:
        st.success(f"Hello {name}! Generating your personalized roadmap...")
        
        # Echo user input
        st.markdown(f"### 📌 Profile Summary")
        st.write(f"**Skill Level:** {skill_level}")
        st.write(f"**Interests:** {', '.join(interests)}")
        st.write(f"**Study Time per Week:** {weekly_hours} hours")
        st.write(f"**Career Goal:** {career_goal}")

        with st.spinner("🧠 Generating personalized roadmap with IBM Granite..."):
            try:
                # Call the Granite model
                roadmap_output = generate_ai_roadmap(name, skill_level, interests, career_goal, weekly_hours)

                # Display AI-generated roadmap
                st.markdown("### 📘 AI-Generated Learning Roadmap")
                st.markdown(roadmap_output)

            except Exception as e:
                st.error("⚠️ Failed to generate roadmap. Please check your IBM credentials.")
                st.exception(e)
    else:
        st.error("Please fill in all required fields.")

