import streamlit as st
import requests

# ------------------ CONFIG ------------------
st.set_page_config(page_title="AI Assistant", layout="centered")

# ------------------ MODEL CHECK ------------------
def check_model():
    try:
        requests.get("http://localhost:11434")
        return True
    except:
        return False

model_available = check_model()

# ------------------ UI ------------------
st.title("🤖 AI Assistant")
st.write("Ask anything and get AI responses")

if not model_available:
    st.warning("⚠️ AI model not running. Using fallback mode.")

# ------------------ SESSION ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ FUNCTION ------------------
def get_answer(q):
    if model_available:
        try:
            with st.spinner("Thinking..."):
                r = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "llama3",
                        "prompt": q,
                        "stream": False
                    },
                    timeout=20
                )

                if r.status_code == 200:
                    data = r.json()
                    if "response" in data:
                        return data["response"]

        except:
            pass

    # 🔥 FALLBACK SYSTEM (always works)
    q_lower = q.lower()

    if "cloud" in q_lower:
        return "Cloud computing allows applications to run on remote servers instead of local machines."
    elif "ai" in q_lower:
        return "Artificial Intelligence enables machines to perform tasks that normally require human intelligence."
    elif "devops" in q_lower:
        return "DevOps is a practice that combines development and operations to automate software delivery."
    elif "docker" in q_lower:
        return "Docker is a containerization tool used to package applications with their dependencies."
    elif "kubernetes" in q_lower:
        return "Kubernetes is used to manage and scale containerized applications."

    return "AI service is temporarily unavailable, but the system is functioning correctly."

# ------------------ INPUT ------------------
user_input = st.text_input("Enter your question")

if user_input:
    response = get_answer(user_input)

    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("AI", response))

# ------------------ CHAT DISPLAY ------------------
st.subheader("💬 Chat History")

for role, msg in st.session_state.messages:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")

# ------------------ CLEAR BUTTON ------------------
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()