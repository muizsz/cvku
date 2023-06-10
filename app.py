from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV |  Muhammad Muizz"
PAGE_ICON = ":wave:"
NAME = "Muhammad Muizz"
DESCRIPTION = """
Junior programming ruby on rails sinatra and Python Flask 
"""
EMAIL = "muhammadmuizz8@gmail.com"
SOCIAL_MEDIA = {
   "Instagram": "https://instagram.com/muiz2z?igshid=MzNlNGNkZWQ4Mg==",
   #-- "LinkedIn": "https://linkedin.com",
   #-- "GitHub": "https://github.com",
   #-- "Twitter": "https://twitter.com",
}

PROJECTS = { #--
   #-- "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
   #-- "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
   #-- "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
   #-- "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience")
st.write(
    """
- ✔️ can reading Qur'an 
- ✔️ have knowladge laptop reparation 
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Junior Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Flask), Ruby(Rails), SQL.
- 📊 editing Video : PhotoShop, Canva, CapCut and FinalCut Pro
- 🗄️ Database: MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Activity")
st.write("---")

# --- JOB 1
st.write("🚧", "Informatics Engineering")
st.write("semester 6")
st.write(
    """
- ► Learn coding C++, HTML CSS, Java Script, Ruby on Rails, Python Flask
- ► assistant professor Informatics Engineering 
- ► Photo editing (photoshop)
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "C++ ")
st.write(" inheritance of object properties ")
st.write(
    """
- ► Inheritance is an OOP concept where a class can pass down its data members and member functions to other classes. 
- ► The inheritance concept is used to utilize the code reuse feature, which avoids duplication of program code.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", " Ruby Sinatra ")
st.write("Create, read, Update and Delete")
st.write(
    """
- ► Understanding the concept CRUD in Ruby with sinatra 
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
#-- st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
