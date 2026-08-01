# System Configuration: Career Guide Enterprise Web App

## 1. Project Overview
You are acting as a Senior Python Front-End Developer. We are building an enterprise-grade Streamlit web application designed to guide students (specifically in India) toward diverse career opportunities outside of standard engineering and medical paths.

## 2. Tech Stack
* **Language:** Python
* **Framework:** Streamlit
* **Data Source:** `information.md` (Parse the JSON data within this file to act as the database)

## 3. UI/UX Requirements
* **Page Configuration:** Set the page layout to "wide".
* **Hero Section:** Add a highly professional hero banner/header at the top that says: "Beyond Engineering: Discover Your True Path".
* **Sub-header:** "Select your interests below to discover high-paying, global career opportunities and startup ideas."

## 4. The Logic Engine & User Flow
Create a three-step funnel for the user:
* **Step 1 (Input):** Render two Streamlit dropdown menus side-by-side using `st.columns`.
    * Dropdown 1: 'Subject Interest' (Extract unique values dynamically from the database).
    * Dropdown 2: 'Work Style' (Extract unique values dynamically from the database).
* **Step 2 (Processing):** Write a Python filtering engine that takes the user's two selections and searches the database for exact matches.
* **Step 3 (Output):** Display the matching careers using clean, formatted Streamlit cards (or styled containers).

## 5. Data Display Formatting
For each matching career, display the following data points clearly:
* **Career Name** (as a subheader)
* **Average Income** (highlighted text)
* **Required Degree & Subjects**
* **Required Exams**
* **Pathway Steps** (rendered as a bulleted list)
* **Interactive Element:** Add a Streamlit button (e.g., `st.button`) under each career that says "How to Start a Business in this Field". When clicked, it should expand or reveal the 'Startup_Potential' data point.