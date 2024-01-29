import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)


# def get_gemini_response(input):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content(input)
#     try:
#         response_data = json.loads(response.text)
#         return response_data
#     except json.JSONDecodeError as e:
#         print("Error decoding JSON. Response content:", response.text)
#         return {"error": str(e)}

# def input_pdf_text(uploaded_file):
#     reader=pdf.PdfReader(uploaded_file)
#     text=""
#     for page in range(len(reader.pages)):
#         page=reader.pages[page]
#         text+=str(page.extract_text())
#     return text

# # prompt_template

# input_prompt = """
#  You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
#   Please share your professional evaluation on whether the candidate's profile aligns with the role. 
#  Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
#  Also please provide the percentage of match and keywords missing and final thoughts.

#     Resume:{text}
#     Job Description:{job_description}

#     I want the response in the following format:
#     Percentage Match: {percentage_match}
#     Keywords Missing: {keywords_missing}
#     Final Thoughts: {final_thoughts}
# """

# # streamlit app

# st.set_page_config(page_title="ATS Resume EXpert")
# st.header("ATS Tracking System")
# input_text=st.text_area("Job Description: ",key="input")
# uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])

# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")

# submit1 = st.button("Tell Me About the Resume")

# submit2 = st.button("How Can I Improvise my Skills")

# submit3 = st.button("Percentage match")

# if submit1:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_text(uploaded_file)
#         response=get_gemini_response(input_prompt)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")

# elif submit2:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_text(uploaded_file)
#         response=get_gemini_response(input_prompt)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_text(uploaded_file)
#         response=get_gemini_response(input_prompt)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume") 












