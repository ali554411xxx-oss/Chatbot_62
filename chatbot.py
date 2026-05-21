import streamlit as st
from groq import Groq
import time

st.set_page_config(
    page_title="بوتي | مساعدك الذكي",
    page_icon="🤖",
    layout="centered"
)

# ===== CSS تصميم احترافي =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;900&display=swap');

* {
    font-family: 'Tajawal', sans-serif !important;
    direction: rtl;
}

/* خلفية الصفحة */
.stApp {
    background: #0a0a0f;
    background-image:
        radial-gradient(ellipse at 20% 20%, rgba(99, 52, 255, 0.15) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 80%, rgba(0, 200, 255, 0.1) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 50%, rgba(255, 60, 120, 0.05) 0%, transparent 70%);
    min-height: 100vh;
}

/* إخفاء عناصر Streamlit الافتراضية */
#MainMenu, footer, header {visibility: hidden;}
.block-container {
    padding-top: 2rem !important;
    max-width: 800px !important;
}

/* العنوان الرئيسي */
.hero-header {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    position: relative;
}

.hero-title {
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(135deg, #a78bfa, #60a5fa, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
    line-height: 1.2;
    animation: shimmer 3s ease-in-out infinite;
    background-size: 200% auto;
}

@keyframes shimmer {
    0% { background-position: 0% center; }
    50% { background-position: 100% center; }
    100% { background-position: 0% center; }
}

.hero-subtitle {
    color: rgba(255,255,255,0.45);
    font-size: 1rem;
    font-weight: 300;
    margin-top: 0.5rem;
    letter-spacing: 1px;
}

.status-dot {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(52, 211, 153, 0.1);
    border: 1px solid rgba(52, 211, 153, 0.3);
    color: #34d399;
    font-size: 0.8rem;
    padding: 4px 14px;
    border-radius: 20px;
    margin-top: 1rem;
}

.status-dot::before {
    content: '';
    width: 7px;
    height: 7px;
    background: #34d399;
    border-radius: 50%;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
}

/* حاوية الرسائل */
.chat-container {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 20px;
    padding: 1.5rem;
    margin: 1rem 0;
    backdrop-filter: blur(10px);
    min-height: 200px;
}

/* رسائل المستخدم */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: linear-gradient(135deg, rgba(99, 52, 255, 0.2), rgba(99, 52, 255, 0.08)) !important;
    border: 1px solid rgba(99, 52, 255, 0.25) !important;
    border-radius: 18px 18px 4px 18px !important;
    padding: 1rem 1.2rem !important;
    margin: 0.5rem 0 0.5rem 2rem !important;
    color: #e2d9ff !important;
    animation: slideInRight 0.3s ease;
}

/* رسائل البوت */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: linear-gradient(135deg, rgba(0, 200, 255, 0.08), rgba(52, 211, 153, 0.05)) !important;
    border: 1px solid rgba(0, 200, 255, 0.15) !important;
    border-radius: 18px 18px 18px 4px !important;
    padding: 1rem 1.2rem !important;
    margin: 0.5rem 2rem 0.5rem 0 !important;
    color: #d1f5ff !important;
    animation: slideInLeft 0.3s ease;
}

@keyframes slideInRight {
    from { opacity: 0; transform: translateX(20px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-20px); }
    to { opacity: 1; transform: translateX(0); }
}

/* حقل الإدخال */
[data-testid="stChatInputContainer"] {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 16px !important;
    padding: 0.3rem 0.5rem !important;
    backdrop-filter: blur(10px);
    transition: border-color 0.3s ease;
}

[data-testid="stChatInputContainer"]:focus-within {
    border-color: rgba(99, 52, 255, 0.5) !important;
    box-shadow: 0 0 20px rgba(99, 52, 255, 0.1) !important;
}

[data-testid="stChatInputContainer"] textarea {
    color: #ffffff !important;
    font-family: 'Tajawal', sans-serif !important;
    font-size: 1rem !important;
    direction: rtl !important;
}

[data-testid="stChatInputContainer"] textarea::placeholder {
    color: rgba(255,255,255,0.3) !important;
}

/* زر الإرسال */
[data-testid="stChatInputContainer"] button {
    background: linear-gradient(135deg, #6334ff, #00c8ff) !important;
    border-radius: 10px !important;
    border: none !important;
    transition: transform 0.2s, box-shadow 0.2s !important;
}

[data-testid="stChatInputContainer"] button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 4px 15px rgba(99, 52, 255, 0.4) !important;
}

/* زر مسح المحادثة */
.stButton button {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: rgba(255,255,255,0.5) !important;
    border-radius: 10px !important;
    font-family: 'Tajawal', sans-serif !important;
    font-size: 0.85rem !important;
    transition: all 0.2s !important;
}

.stButton button:hover {
    background: rgba(255, 60, 60, 0.1) !important;
    border-color: rgba(255, 60, 60, 0.3) !important;
    color: #ff6b6b !important;
}

/* فاصل */
hr {
    border-color: rgba(255,255,255,0.06) !important;
    margin: 1rem 0 !important;
}

/* نص الرسائل */
[data-testid="stMarkdownContainer"] p {
    color: inherit !important;
    line-height: 1.8 !important;
}

/* Spinner */
.stSpinner > div {
    border-top-color: #6334ff !important;
}

/* إحصائيات */
.stats-bar {
    display: flex;
    justify-content: center;
    gap: 2rem;
    padding: 0.8rem;
    background: rgba(255,255,255,0.02);
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.05);
    margin-bottom: 1rem;
}

.stat-item {
    text-align: center;
}

.stat-num {
    font-size: 1.3rem;
    font-weight: 700;
    color: #a78bfa;
}

.stat-label {
    font-size: 0.7rem;
    color: rgba(255,255,255,0.3);
}
</style>
""", unsafe_allow_html=True)

# ===== الهيدر =====
st.markdown("""
<div class="hero-header">
    <h1 class="hero-title">🤖 بوتي</h1>
    <p class="hero-subtitle">مساعدك الذكي · يعمل بتقنية Llama 3.1</p>
    <div class="status-dot">متصل ويعمل</div>
</div>
""", unsafe_allow_html=True)

# ===== الاتصال بـ API =====
try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    st.error("🔐 لم يتم إعداد مفتاح API. راجع إعدادات Secrets.")
    st.stop()

client = Groq(api_key=api_key)

# ===== تهيئة المحادثة =====
if "messages" not in st.session_state:
    st.session_state.messages = []

if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

# ===== الإحصائيات =====
msg_count = len(st.session_state.messages)
user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])

st.markdown(f"""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-num">{user_msgs}</div>
        <div class="stat-label">سؤالك</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">{msg_count}</div>
        <div class="stat-label">إجمالي الرسائل</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">∞</div>
        <div class="stat-label">قدرة البوت</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== عرض الرسائل =====
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ===== رسالة ترحيب =====
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("👋 **أهلاً! أنا بوتي، مساعدك الذكي.**\n\nاسألني عن أي شيء — تقنية، ذكاء اصطناعي، برمجة، أو أي موضوع يخطر على بالك! 🚀")

# ===== حقل الإدخال =====
if prompt := st.chat_input("💬 اكتب سؤالك هنا..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("بوتي يفكر..."):
            try:
                # إرسال كل سياق المحادثة
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {
                            "role": "system",
                            "content": "أنت بوتي، مساعد ذكي ومفيد باللغة العربية. أجب بشكل واضح ومختصر وودود. استخدم الإيموجي بشكل معتدل لتجعل المحادثة حيوية."
                        }
                    ] + [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    temperature=0.7,
                    max_tokens=1024
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"⚠️ خطأ في الاتصال: {e}")

    st.rerun()

# ===== زر مسح المحادثة =====
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    if st.button("🗑️ مسح المحادثة"):
        st.session_state.messages = []
        st.rerun()

