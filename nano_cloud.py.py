import streamlit as st
from groq import Groq

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Nano AI ⚡", layout="centered")

# ضع مفتاح الـ API هنا (سأعلمك لاحقاً كيف تخفيه للأمان)
client = Groq(api_key="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")

st.markdown("""
    <style>
    .stApp { background: #121212; color: white; }
    .user-bubble { background: #0084ff; color: white; padding: 12px; border-radius: 15px; margin: 5px; text-align: right; }
    .bot-bubble { background: #2e2e2e; color: #f0f0f0; padding: 12px; border-radius: 15px; margin: 5px; border: 1px solid #444; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Nano Cloud- by Momin")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    div_class = "user-bubble" if msg["role"] == "user" else "bot-bubble"
    st.markdown(f'<div class="{div_class}">{msg["content"]}</div>', unsafe_allow_html=True)

if prompt := st.chat_input("تحدث مع نانو العالمي..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-bubble">{prompt}</div>', unsafe_allow_html=True)

    with st.spinner("Nano يفكر..."):
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Your name is Nano. Be a smart, friendly, and concise AI assistant. Respond in the user's language."},
                *st.session_state.messages
            ],
            model="llama-3.3-70b-versatile", # موديل سريع جداً
        )
        answer = chat_completion.choices[0].message.content
        st.markdown(f'<div class="bot-bubble">{answer}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": answer})
