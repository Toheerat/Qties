import streamlit as st

def main():
    st.title("Introducing Qties (App of Qeelsthoughts) - Your Gateway to Opportunities and Community Building!")

    # Google Drive logo image link
    logo_link = "https://drive.google.com/uc?export=download&id=1C5ThRLFMJCsTjBMWF3VD5VZmjlqWVlVd"
    
    # Display the logo image with a width of 200 pixels
    st.image(logo_link, caption="Qties App Logo", width=200)


    st.markdown(
        "QTies is a revolutionary app designed to bring people together, fostering a thriving network of like-minded individuals seeking to explore new opportunities, build meaningful connections, and enhance their job search process. With a user-friendly interface and powerful features, we are your one-stop platform to connect, collaborate, and succeed."
    )

    st.header("Key Features:")

    st.markdown("1. **Connecting People:** Whether you're a seasoned professional, a recent graduate, or simply looking to expand your social circle, QTies makes it effortless to find and connect with individuals who share your interests, professional goals, and passions.")

    st.markdown("2. **Exploring Opportunities:** Say goodbye to traditional job boards. Our app provides a dynamic and updated job search feature that tailors results based on your skills, experience, and preferences.")

    st.markdown("3. **Fostering Community:** Building a strong community is at the heart of QTies App. Join groups and forums centered around your areas of expertise, hobbies, or personal interests. Engage in discussions, ask questions, and share knowledge with like-minded individuals who are eager to connect and grow together.")

    st.markdown("4. **Events and Meetups:** Stay informed about local and virtual events, workshops, and meetups happening in your area. Expand your network, gain valuable insights from industry experts, and create lasting memories with your newfound connections.")

    st.markdown("5. **Skill Development:** Never stop learning and improving. Access a wide range of educational resources, online courses, and webinars that can help you enhance your skillset and stay ahead in your professional journey.")

    st.markdown("6. **Personalized Recommendations:** The more you use QTies, the smarter it gets. Our app's intelligent algorithm learns from your interactions and provides personalized recommendations for jobs, events, and groups that align with your preferences and objectives.")

    st.markdown("7. **Secure and Private:** We value your privacy and security. Rest assured that all your personal information is protected, and you have full control over your profile visibility and data sharing options.")

    st.markdown(
        "Join QTies today and embark on a journey of growth, collaboration, and endless possibilities. Whether you're searching for new job opportunities, seeking meaningful connections, or eager to be a part of vibrant communities, our app is here to empower you on your path to success. Download now and take the first step towards a brighter future!"
    )

    st.header("Other Images:")
    # Google Drive image links for other images
    image_links = [
        "https://drive.google.com/uc?export=download&id=16at1Ic-oy3CavRd4c2Vc55feLLlA54Nh",
        "https://drive.google.com/uc?export=download&id=1llabBUj9gfFC0jQZBPTiEW1GJ0PHCbnF",
        "https://drive.google.com/uc?export=download&id=1CxDs_8lvPNNqKSwh6mGh_lj3TtN645Ef",
        "https://drive.google.com/uc?export=download&id=1BefQZDpVgNUR8NYkzRt-rF-QT6GTvpMb",
    ]
    
  #  # Display all the other images beside each other in columns
    cols = st.columns(4)
    
    for i, col in enumerate(cols):
        col.image(image_links[i], caption="Image", width=200)

    
if __name__ == "__main__":
    main()

