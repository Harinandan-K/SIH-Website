import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")
st.title("📊 Admin Dashboard")
st.write("Manage all the core data required for timetable generation here.")

# --- INITIALIZE SESSION STATE FOR DATA ---
# This is crucial to persist data across page reruns and interactions.
if 'teachers' not in st.session_state:
    st.session_state.teachers = pd.DataFrame(columns=['Name', 'Department'])
if 'subjects' not in st.session_state:
    st.session_state.subjects = pd.DataFrame(columns=['Name', 'Code'])
if 'classrooms' not in st.session_state:
    st.session_state.classrooms = pd.DataFrame(columns=['Room Name/No.', 'Capacity'])
if 'batches' not in st.session_state:
    st.session_state.batches = pd.DataFrame(columns=['Batch Name', 'Strength'])


# --- LAYOUT ---
col1, col2 = st.columns(2)

# --- TEACHERS MANAGEMENT ---
with col1:
    st.header("👨‍🏫 Manage Teachers")
    with st.expander("Add New Teacher", expanded=False):
        with st.form("teacher_form", clear_on_submit=True):
            teacher_name = st.text_input("Teacher Name")
            teacher_dept = st.text_input("Department")
            submitted = st.form_submit_button("Add Teacher")
            if submitted and teacher_name:
                new_teacher = pd.DataFrame([{'Name': teacher_name, 'Department': teacher_dept}])
                st.session_state.teachers = pd.concat([st.session_state.teachers, new_teacher], ignore_index=True)
                st.success(f"Added {teacher_name}!")
    st.write("Current Teachers:")
    st.dataframe(st.session_state.teachers, use_container_width=True)

# --- SUBJECTS MANAGEMENT ---
with col1:
    st.header("📚 Manage Subjects")
    with st.expander("Add New Subject", expanded=False):
        with st.form("subject_form", clear_on_submit=True):
            subject_name = st.text_input("Subject Name")
            subject_code = st.text_input("Subject Code")
            submitted = st.form_submit_button("Add Subject")
            if submitted and subject_name:
                new_subject = pd.DataFrame([{'Name': subject_name, 'Code': subject_code}])
                st.session_state.subjects = pd.concat([st.session_state.subjects, new_subject], ignore_index=True)
                st.success(f"Added {subject_name}!")
    st.write("Current Subjects:")
    st.dataframe(st.session_state.subjects, use_container_width=True)


# --- CLASSROOMS MANAGEMENT ---
with col2:
    st.header("🏫 Manage Classrooms")
    with st.expander("Add New Classroom", expanded=False):
        with st.form("classroom_form", clear_on_submit=True):
            room_name = st.text_input("Room Name / Number")
            capacity = st.number_input("Capacity", min_value=10, step=5)
            submitted = st.form_submit_button("Add Classroom")
            if submitted and room_name:
                new_classroom = pd.DataFrame([{'Room Name/No.': room_name, 'Capacity': capacity}])
                st.session_state.classrooms = pd.concat([st.session_state.classrooms, new_classroom], ignore_index=True)
                st.success(f"Added {room_name}!")
    st.write("Available Classrooms:")
    st.dataframe(st.session_state.classrooms, use_container_width=True)


# --- BATCHES MANAGEMENT ---
with col2:
    st.header("🧑‍🎓 Manage Student Batches")
    with st.expander("Add New Batch", expanded=False):
        with st.form("batch_form", clear_on_submit=True):
            batch_name = st.text_input("Batch Name (e.g., 'CSE 2025 A')")
            strength = st.number_input("Strength", min_value=10, step=5)
            submitted = st.form_submit_button("Add Batch")
            if submitted and batch_name:
                new_batch = pd.DataFrame([{'Batch Name': batch_name, 'Strength': strength}])
                st.session_state.batches = pd.concat([st.session_state.batches, new_batch], ignore_index=True)
                st.success(f"Added {batch_name}!")
    st.write("Current Batches:")
    st.dataframe(st.session_state.batches, use_container_width=True)
