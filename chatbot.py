import streamlit as st
from groq import Groq

st.set_page_config(page_title="بوت شركتي", page_icon="🏢")
st.title("🏢 بوت خدمة العملاء")

api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

# تعريف شخصية البوت ومعلومات الشركة
SYSTEM_PROMPT = """
أنت مساعد ذكي لشركة "تقنيات المستقبل". شركتنا تعمل في مجال البرمجة والذكاء الاصطناعي.
خدماتنا:
- تطوير تطبيقات الهاتف
- تصميم مواقع الويب
- استشارات تقنية

ساعات العمل: من الأحد إلى الخميس، 9 صباحاً إلى 5 مساءً.
مقر الشركة: الرياض، المملكة العربية السعودية.

رد على العملاء بلباقة واحترافية. إذا سألك العميل عن شيء خارج نطاق الشركة، قل له "سأحولك إلى فريق الدعم البشري".
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

if prompt := st.chat_input("اكتب سؤالك عن الشركة:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
