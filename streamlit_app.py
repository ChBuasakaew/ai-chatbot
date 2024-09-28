import streamlit as st
import google.generativeai as genai 

st.title("🐹 My Trial Chatbot")
st.caption("Here is my GitHub https://github.com/ChBuasakaew/ai-chatbot that is a part of studying MADT8102 course")

# Capture Gemini API Key 
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password") 

# Initialize session state for storing chat history, configuration status, and model instance
if "chat_history" not in st.session_state: 
    st.session_state.chat_history = []  # Initialize with an empty list
if "gemini_configured" not in st.session_state:
    st.session_state.gemini_configured = False  # Track configuration status
if "introduction_sent" not in st.session_state:
    st.session_state.introduction_sent = False  # Track if introduction message has been sent
if "model" not in st.session_state:
    st.session_state.model = None  # To store the model instance

# Initialize the Gemini Model 
if gemini_api_key and not st.session_state.gemini_configured: 
    try: 
        # Configure Gemini with the provided API Key 
        genai.configure(api_key=gemini_api_key) 
        st.session_state.model = genai.GenerativeModel("gemini-pro") 
        st.balloons()
        st.success("Gemini API Key successfully configured.") 
        st.session_state.gemini_configured = True  # Set configuration status to True

        
        # Add an introduction message from the bot if not already sent
        if not st.session_state.introduction_sent:
            introduction_message = "สวัสดีค่ะ! '🐹 น้องใหม่' เองน้าา นักศึกษาฝึกงานจากธนาคารเกียรตินาคินภัทร (Kiatnakin Phatra Bank)  น้องใหม่พร้อมเคียงข้างให้คำปรึกษาทุกเรื่องเกี่ยวกับสินเชื่อรถยนต์ค่ะ 🚗 "
            st.session_state.chat_history.append(("assistant", introduction_message))
            st.session_state.introduction_sent = True  # Mark the introduction as sent

    except Exception as e: 
        st.error(f"An error occurred while setting up the Gemini model: {e}") 

# Display previous chat history using st.chat_message (if available) 
for role, message in st.session_state.chat_history: 
    st.chat_message(role).markdown(message) 

# Capture user input and generate bot response 
if user_input := st.chat_input("Type your message here..."): 
    # Store and display user message 
    st.session_state.chat_history.append(("user", user_input)) 
    st.chat_message("user").markdown(user_input) 

    # Use Gemini AI to generate a bot response 
    if st.session_state.model: 
        try: 
            response = st.session_state.model.generate_content(user_input) 
            bot_response = response.text  
            # Store and display the bot response 
            st.session_state.chat_history.append(("assistant", bot_response)) 
            st.chat_message("assistant").markdown(bot_response)
        except Exception as e: 
            st.error(f"An error occurred while generating the response: {e}") 
