import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="View Timetable", page_icon="🗓️", layout="wide")

st.title("🗓️ View Generated Timetable")

# --- CHECK IF TIMETABLE EXISTS ---
if 'generated_timetable' not in st.session_state or st.session_state.generated_timetable.empty:
    st.warning("No timetable has been generated yet. Please go to the 'Generate Timetable' page first.")
else:
    timetable_df = st.session_state.generated_timetable

    st.success("Displaying the most recently generated timetable.")

    # --- DISPLAY FILTERS (Optional but good for demo) ---
    # In a real app, you would get these from your data
    batches = timetable_df.columns.tolist()
    selected_batch = st.selectbox("Select a Batch to View", batches)

    # --- DISPLAY TIMETABLE ---
    if selected_batch:
        st.header(f"Timetable for {selected_batch}")

        # Streamlit doesn't handle multi-index well for display, so we reset it for a clean table.
        display_df = timetable_df[[selected_batch]].reset_index()

        # Pivot the table for a classic timetable view
        try:
            pivoted_df = display_df.pivot(index='Time', columns='Day', values=selected_batch)

            # Reorder columns to be in chronological order
            day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            pivoted_df = pivoted_df.reindex(columns=day_order)

            st.dataframe(pivoted_df, use_container_width=True)
        except Exception as e:
            st.error(f"Could not pivot the data for display. Error: {e}")
            st.write("Raw data:")
            st.dataframe(display_df, use_container_width=True)

    else:
        st.info("Select a batch to see its timetable.")
