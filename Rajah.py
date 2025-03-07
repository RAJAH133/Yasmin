import streamlit as st
from PIL import Image

# Sidebar Navigation with Icons
st.sidebar.title("📌Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📂 Projects", "💪 Skills", "💬 Testimonials", "📞 Contact"]
)

# Home Section
if page == "🏠 Home":
    image = Image.open("screen1.jpg")  # Ensure your image filename is correct
    st.image(image, caption="RAJAH B.M.W", width=500)  # Change width to an integer
    st.title("🎓My Digital Footprint")
    st.write("### Welcome to My Portfolio")
    st.write("I have a strong enthusiasm for technology and software development, backed by practical experience in creating projects and addressing real-world challenges")
    

# Projects Section
elif page == "📂 Projects":
    st.header("Projects")
    st.write("### i. Student Career Guidance System")
    st.write("Individual Project using Python")
    st.write("[GitHub Link](https://github.com/RAJAH133/Yasmin)")
    st.write("[LinkedIn](https://www.linkedin.com/in/yasmin-yousif-9a0573354/)")

    st.write("### ii. Malaria Diagnosis System")
    st.write("Group Project using Python")
    st.write("[GitHub Link](https://github.com/Yasmin7-w/yasmin)")

# Skills Section
elif page == "💪 Skills":
    st.header("Skills")
    st.write("#### Programming Languages")
    st.progress(90)
    st.write("Python - 90%")
    st.progress(50)
    st.write("Machine Learning - 50%")
    st.progress(80)
    st.write("Web Development - 80%")

# Testimonials Section
elif page == "💬 Testimonials":
    st.header("Testimonials")
    st.write("> RAJAH is a clever guy & a problem solver! – Anime guy ❤")
    st.write("> RAJAH project developer – kalam 😈")
    st.write("> RAJAH is a cool guy – Moni ❤")

# Contact Section
elif page == "📞 Contact":
    st.header("Contact")
    st.write("Feel free to reach out via my LinkedIn or GitHub profiles!")
    st.write("📧 Email: yasminyousif133@gmail.com")
    st.write("🔗[LinkedIn](https://www.linkedin.com/in/yasmin-yousif-9a0573354/)")
    st.write("📂[GitHub](https://github.com/RAJAH133/Yasmin)")
    # Resume Download Button
with open("RAJAH_CV.pdf", "rb") as file:
    st.sidebar.download_button("Download RAJAH_CV", file, file_name="RAJAH_CV.pdf")