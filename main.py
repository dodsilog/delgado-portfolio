import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Donnell's Portfolio", page_icon="🐼", layout="wide")



# Sidebar content
st.sidebar.image("Logo.jpg", use_column_width=True)
sections = ["Home", "About Me", "Skills", "Projects"]
selection = st.sidebar.radio("", sections)

# Home Section
if selection == "Home":
    st.title("Welcome to My Portfolio! 👋")
    st.write("Hi! I'm Donnell, an aspiring developer with a passion for technology and learning new things. Explore my portfolio to learn more about me and my work 🐼.")
    # Cat and Dog Feature
    st.markdown("---")
    st.subheader("What pet do you prefer?")
    pet_choice = st.radio("", ["none :(", "Dog", "Cat"], index=0)
    if pet_choice == "Dog":
            st.subheader("Here's a cute dog! 🐶")
            dog_image = Image.open("cute_dog.gif")  # Replace with your dog image path
            st.image(dog_image, width=300)
    elif pet_choice == "Cat":
            st.subheader("Here's a cute cat! 🐱")
            cat_image = Image.open("cute_cat.gif")  # Replace with your cat image path
            st.image(cat_image, width=300)

# About Me Section
elif selection == "About Me":
    st.title("About Me")
    st.write("I'm an aspiring software developer with a love for learning and exploring new technologies. Below is a little more about me:")
    st.subheader("Biography")
    st.write("""
        From Ormoc City, Leyte. Currently studying at Cebu Institute of Technology - University. Currently a fourth year Bachelor of Science in
        Information Technology student.
    """)

# Skills Section
elif selection == "Skills":
    st.title("Skills")
    st.subheader("Programming Languages")
    st.write("Python")
    st.progress(45)
    st.write("JavaScript")
    st.progress(30)
    st.write("HTML & CSS")
    st.progress(50)
    
    st.subheader("Frameworks & Tools")
    st.write("Streamlit, Django, Flask, React.js, Git, Docker")
    st.subheader("Other Experiences")
    st.write(
          """
          - Photojournalist during my Senior High School Years.
          - Worked as technical staff for multiple government 
          and private    events 
          hosted in Ormoc City, Leyte.
          - Freelance Computer building, maintenance and troubleshooting.
          
          """
    )

# Projects Section
elif selection == "Projects":
    st.title("Projects")
    st.write("Here are a few of the projects I've worked on:")
    
    st.subheader("Project 1: Personal Portfolio Website")
    st.write("A responsive personal website built using HTML, CSS, and JavaScript.")
    st.markdown("[View Project](https://www.facebook.com)")
    
    st.subheader("Project 2: E-commerce Platform")
    st.write("An e-commerce platform built using Django and React.")
    st.markdown("[View Project](https://shopee.ph)")
    


with st.container():
# Footer
    st.markdown("---")
    st.subheader("Get In Touch")
    st.write("For more inquiries, feel free to reach out to me.")
    col1, col2, col3, col4 = st.columns(4)

    with col1: 
        st.write("📧 ggdoddy@gmail.com")
    with col2:
        st.markdown("𝕏 [@dodsilog](https://x.com/elonmusk)")
    with col3:
        st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/mark-zuckerberg-618bba58)")
    with col4:
        st.markdown("💻 [GitHub](https://github.com/twpayne)")
