import streamlit as st
import time
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="Generate Timetable", page_icon="🚀", layout="centered")

st.title("🚀 Generate a New Timetable")
st.write("This page will run the core scheduling algorithm based on the data provided in the dashboard.")

st.info("Ensure all teachers, subjects, classrooms, and batches are correctly entered before generating.", icon="ℹ️")


# This is a placeholder function for your actual algorithm.
def run_scheduling_algorithm():
    """
    This function will be replaced by your team's actual scheduling logic.
    For this prototype, it just creates some fake data after a delay.
    """
    time.sleep(3) # Simulate a long-running process

    # --- FAKE DATA CREATION ---
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    time_slots = ["09:00-10:00", "10:00-11:00", "11:00-12:00", "13:00-14:00", "14:00-15:00"]
    subjects = ["Data Structures", "Algorithms", "Database Systems", "Operating Systems", "Networking", "AI", "Machine Learning"]
    teachers = ["Dr. Smith", "Dr. Jones", "Dr. Williams", "Dr. Brown"]
    rooms = ["Room 101", "Room 102", "Lab 201", "Lab 202"]

    # Create a DataFrame with a multi-index for days and time slots
    index = pd.MultiIndex.from_product([days, time_slots], names=["Day", "Time"])
    timetable_df = pd.DataFrame(index=index)

    # For this demo, let's create a timetable for one batch
    batch = "CSE 2025 A"
    schedule = []
    for _ in range(len(days) * len(time_slots)):
        subject = np.random.choice(subjects + [None]) # Add None for empty slots
        if subject:
            teacher = np.random.choice(teachers)
            room = np.random.choice(rooms)
            schedule.append(f"{subject}\n({teacher})\n[{room}]")
        else:
            schedule.append("--- FREE ---")

    timetable_df[batch] = np.random.permutation(schedule) # Shuffle to make it look random
    return timetable_df


# --- GENERATE BUTTON ---
if st.button("✨ Generate Timetable", type="primary", use_container_width=True):
    with st.spinner("Running the scheduling algorithm... This might take a moment."):
        # Call your main algorithm function here
        generated_timetable = run_scheduling_algorithm()

        # Store the result in session state to be used by the 'View Timetable' page
        st.session_state['generated_timetable'] = generated_timetable

    st.success("🎉 Timetable generated successfully!")
    st.balloons()
    st.info("You can now view the result on the 'View Timetable' page from the sidebar.")
