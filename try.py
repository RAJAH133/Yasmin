import streamlit as st
import json

#Set page title and icon

st.set_page_config(page_title="Student Portfolio",page_icon="🎓")

#Sidebar naviagtion

st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go To:",
	   ["Home","Projects","Skills","Settings","Contact"])
#Home section

if page =="Home":
	st.title("🎓 Student Portfolio")

	#Profile image
	uploaded_image = st.file_uploader("Uplaod Profile Picture", type=["jpg","png"])
	if uploaded_image is not None:
		st.image(uploaded_image, width=150, caption="Uploaded image")
	else:
		st.image("person.png", width=150, caption="Default image")
	#Student details (Editable!)
	name = st.text_input("Name: ", "RAJAH Yousif")
	location = st.text_input("Location: ", "Musanze,Rwanda")
	field_of_study = st.text_input("Field of Study: ", 
	                               "Computer Science, SWE")
	university = st.text_input("University: ", "INES - Ruhengeri")

	st.write(f"📍{location}")
	st.write(f"📚{field_of_study}")
	st.write(f"🎓{university}")

	# Resume download button
	with open("/management ass2.pdf", "rb") as file:
		resume_bytes = file.read()
	st.download_button(label="📄Download Resume",
		data=resume_bytes,file_name="/# AI-Based Desktop Smart Voice Assistant.md", 
		mime="application/pdf")

	st.markdown("---")
	st.subheader("About Me")
	about_me = st.text_area("Short introduction about myself:",
		"I am a passionate AI look forward engineer!")
	st.write(about_me)

#Projects section
elif page =="Projects":	
	st.title("💻 My Projects")

	# Project Filtering System
	category = st.selectbox("Filter by Category", ["All", "Year 1 Project", "Group Projects", "Dissertation"])
	if category == "All" or category == "Year 1 Project":
		with st.expander("📊 Data Analysis Project"):
			st.write("A project analyzing trends of Rwanda GDP accounts using Pandas and Matplotlib")
	if category == "All" or category == "Group Projects":
		with st.expander("🤖 AI Chatbot"):
			st.write("Developed an AI-Powered chatbot using Python and NLP Techniques")
	if category == "All" or category == "Dissertation":
		with st.expander("🌐 Caritas CDJP Gikongoro Website"):
			st.write("Designed and Developed and website for Caritas Gikondoro using Wordpress CMS")

elif page =="Skills":
	st.title("⚡ Skills and Achievements")

	st.subheader("Programming Skills")
	skill_python = st.slider("Python",0,100,90)
	st.progress(skill_python)

	skill_js = st.slider("JavaScript",0,100,75)
	st.progress(skill_js)
	skill_AI = st.slider("Artificial Intelligence",0,100,65)
	st.progress(skill_AI)

	st.subheader("Cerfications & Achievements")
	st.write("✔ Completed AI&ML in Business Cerfication")
	st.write("✔ Certified AI in Research and Course Preparation for Education")

	# Timeline of Academic & Project Milestones
	st.subheader("Timeline of Academic & Project Milestones")
	st.write("Year 1: First project completed ✅")
	st.write("Year 2: Hackathon participation 🏆")
	st.write("Year 3: Internship experience 💼")
	st.write("Year 4: Dissertation submission 📖")

elif page == "Settings":
	st.title("🎨 Customize your profile")

	st.subheader("Upload a Profile Picture")
	uploaded_image = st.file_uploader("Choose a file", type=["./screen1.jpg","png"])
	if uploaded_image:
		st.image(uploaded_image, width=150)

	st.subheader("✍ Edit Personal Info")

elif page =="Contact":
	st.title("📬 Contact Me")

	with st.form("contact_form"):
		name = st.text_input("Your Name")
		email = st.text_input("Your Email")
		message=st.text_area("Your message")

		submitted = st.form_submit_button("Send Message")
		if submitted:
			st.success("✅ Message sent successfully")

		st.write("📧 Email: yasminyousif133@gmail.com")
		st.write("[🔗LinkedIn](https://ikigugugroup.rw)")
		st.write("[📂GitHub](https://ikigugugroup.rw)")

	# Student Testimonials
	st.subheader("🗣️ Student Testimonials")
	st.text_area("Leave a testimonial about me:")

	st.sidebar.write("---")
	st.sidebar.write("🔹 Create with ❤ using My Banana")
