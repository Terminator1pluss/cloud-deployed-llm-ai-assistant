import streamlit as st

st.title("Notes Manager")

# store notes
if "notes" not in st.session_state:
    st.session_state.notes = []

note = st.text_area("Write your note")

if st.button("Add Note"):
    if note:
        st.session_state.notes.append(note)
        st.success("Note added!")

st.subheader("Your Notes")

for n in st.session_state.notes:
    st.write("-", n)