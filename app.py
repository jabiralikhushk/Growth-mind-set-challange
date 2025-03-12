
import streamlit as st
import pandas as pd

# Function to display Growth Mindset Challenge content
def growth_mindset_challenge():
    st.title("Growth Mindset Challenge")
    st.write("""
    ## Embrace the Growth Mindset!
    **Growth Mindset**: The belief that you can develop your abilities through dedication and hard work.

    ### Key Principles:
    - **Embrace Challenges**: See challenges as opportunities to learn.
    - **Learn from Criticism**: Constructive feedback helps you grow.
    - **Celebrate Effort**: Focus on effort, not just the end result.
    - **Perseverance Pays Off**: Keep going, even when it's tough.

    ### Your Challenge:
    Take on at least one new challenge this week that helps you grow. Whether it’s learning a new skill, tackling a difficult problem, or simply trying something new, **keep pushing forward** and remember:
    
    > "Success is the result of good judgment, good judgment is the result of experience, and experience is the result of bad judgment."
    
    ### Growth Mindset Affirmations:
    - "I can learn anything I set my mind to."
    - "I embrace challenges as opportunities for growth."
    - "I learn and improve with every experience."
    """)

# Function to handle the file uploader
def file_uploader():
    st.header("Upload Your Files")
    
    # File uploader for images, text files, pdfs, etc.
    uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg", "pdf", "txt", "csv", "docx"])

    if uploaded_file is not None:
        # Display the uploaded file
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        
        st.write(f"### File Details:")
        st.write(f"**File Name:** {file_name}")
        st.write(f"**File Type:** {file_type}")
        st.write(f"**File Size:** {file_size} bytes")
        
        # File content preview (based on file type)
        if file_type.startswith("image"):
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        elif file_type == "application/pdf":
            st.write("You uploaded a PDF file. Unfortunately, I cannot display PDFs directly.")
        elif file_type == "text/plain":
            content = uploaded_file.getvalue().decode("utf-8")
            st.text(content)
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            st.write("You uploaded a Word document. Further functionality to extract text could be added.")
        else:
            st.write("Unsupported file type for preview.")

# Main function to manage navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Growth Mindset Challenge", "File Uploader"])

    if page == "Growth Mindset Challenge":
        growth_mindset_challenge()
    elif page == "File Uploader":
        file_uploader()

if __name__ == "__main__":
    main()
