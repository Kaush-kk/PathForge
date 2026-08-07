# 🚀 PathForge: The Ultimate Career Navigation Engine

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## 📌 Project Overview
PathForge was engineered to solve a massive problem in the Indian educational system: the "JEE/NEET tunnel vision." It is a stateful, interactive web application that acts as a personalized career mapping engine. 

Instead of static text, PathForge dynamically renders 185+ careers, 50+ entrance exams, and 117+ specialized degrees into a dark-mode, glassmorphic 3D UI, complete with a persistent user memory system (The Forge HUD).

## ⚡ Core Architecture & Features

### 1. The Dynamic Data Engine
* **The Career Vault:** Maps over 185 highly specialized, non-overlapping careers.
* **Pathway Flowcharts:** Utilizes Streamlit modal overlays (`@st.dialog`) to map chronological steps from high school to professional income without forcing page reloads.
* **Verified Exam & Course Matrices:** A hardcoded database of 50 entrance exams and 117 Master Degrees featuring real-time search, multi-tier filtering (Degree/Specialization), and SSL-verified secure links.

### 2. Enterprise Authentication & User Memory (Supabase)
PathForge upgraded from a stateless script to a fully stateful platform utilizing a **Supabase (PostgreSQL)** backend.
* **Custom Auth Routing:** Uses `.streamlit/secrets.toml` to securely communicate with the database, allowing users to register unique usernames and passwords.
* **Relational Database Design:** Built on a 3-table architecture (`users`, `saved_careers`, `career_notes`) linked flawlessly via UUID Foreign Keys.
* **Bypassed RLS:** Engineered custom SQL overrides to perfectly integrate Streamlit's internal session state with Supabase's strict Row Level Security protocols.

### 3. The "My Forge" Persistent HUD
* **Sidebar as a Player HUD:** The UI completely re-engineers the standard Streamlit sidebar into a permanent, interactive Heads Up Display.
* **Frictionless Note Syncing:** Users can dynamically switch between saved careers in a dropdown. The HUD instantly pulls their specific career data and their personalized, private notes via active `UPSERT` database commands.

### 4. 3D Glassmorphic UI/UX
* Deeply patched Streamlit's native DOM using raw HTML/CSS injections.
* Features a decoupled WebGL/Shader 3D Hero background.
* Implements the "Z-Index Overlay Hack" to float custom UI elements perfectly over the interactive 3D canvas.

## 🛠️ Installation & Setup (Local Deployment)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kaush-kk/PathForge.git](https://github.com/kaush-kk/PathForge.git)
   cd PathForge
