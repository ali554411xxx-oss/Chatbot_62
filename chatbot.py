import os
import streamlit as st
from groq import Groq

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="بوت المحادثة الذكي",
    page_icon="🤖",
    layout="centered"
)

# --- العنوان والوصف ---
st.markdown("# 🤖 بوت المحادثة الذكي")
st.markdown("بوت محادثة قوي وسريع يعمل بواسطة **Groq API** و **Llama 3**")

# --- تهيئة مفتاح API ---
def get_groq_api_key():
    try:
        # استخدم secrets من Streamlit Cloud
        api_key = st.secrets["GROQ_API_KEY"]
        return api_key
    except:
        # أو استخدم متغيرات البيئة محلياً
        api_key = os.environ.get("GROQ_API_KEY")
        if api_key is None:
            st.error("⚠️ لم يتم العثور على مفتاح API. تأكد من إضافة `GROQ_API_KEY` إلى secrets.")
            st.stop()
        return api_key

GROQ_API_KEY = get_groq_api_key()

# --- تهيئة عميل Groq ---
@st.cache_resource
def init_groq_client():
    return Groq(api_key=GROQ_API_KEY)

client = init_groq_client()

# --- تهيئة سجل المحادثة ---
if "messages" not in st.session_state:
    # تعريف شخصية البوت (System Prompt)
    SYSTEM_PROMPT = (
        "أنت مساعد ذكي ومفيد، اسمك 'بوت المحادثة'. أنت خبير في تقديم المعلومات والإجابة على "
        "الأسئلة بأسلوب ودود وسهل الفهم. هدفك هو مساعدة المستخدمين بأفضل صورة ممكنة."
    )
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# --- عرض سجل المحادثة القديم ---
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- إدخال المستخدم ---
if prompt := st.chat_input("اكتب سؤالك هنا..."):
    # عرض رسالة المستخدم
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # عرض رد البوت
    with st.chat_message("assistant"):
        # إظهار مؤشر الكتابة
        with st.spinner("جاري الكتابة..."):
            # إرسال الرسائل إلى Groq API
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=st.session_state.messages,
                temperature=0.7,
                max_tokens=1024,
                stream=False
            )
            bot_reply = response.choices[0].message.content
            st.markdown(bot_reply)

    # حفظ رد البوت في السجل
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # تحديث الصفحة لعرض السجل
    st.rerun()
