import streamlit as st
from groq import Groq

st.set_page_config(page_title="بوت خدمة العملاء", page_icon="🏢")
st.title("🏢 بوت خدمة العملاء - شركة تقنيات المستقبل")

api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

# تعليمات صارمة وواضحة للبوت
SYSTEM_PROMPT = """
أنت بوت خدمة عملاء رسمي لشركة "تقنيات المستقبل" (FutureTech).

معلومات الشركة:
- النشاط: تطوير تطبيقات الهاتف ومواقع الويب وحلول الذكاء الاصطناعي
- ساعات العمل: الأحد إلى الخميس 9ص-5م
- التواصل: support@futuretech.com

أهم القواعد:
1. لا تسأل العميل "ماذا تريد؟" أو "كيف يمكنني مساعدتك؟" أكثر من مرة.
2. لا تتحدث عن مواضيع خارج نطاق الشركة (مثل التسويق العام، الموارد البشرية، تحسين الإنتاجية العامة).
3. إذا سأل العميل عن شيء لا تعرفه، قل: "سأحولك إلى فريق الدعم البشري فوراً".
4. كن مباشراً ومفيداً. قدم إجابات قصيرة وعملية.
5. لا تطرح أسئلة استفسارية مفتوحة مثل "هل تريد أن تعرف المزيد عن...؟".

ردودك يجب أن تكون احترافية ومحددة.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# عرض المحادثة السابقة
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# إدخال المستخدم
if prompt := st.chat_input("اكتب سؤالك عن خدمات الشركة..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages,
                temperature=0.5  # أقل من 0.7 لجعل الردود أكثر تحديداً وأقل عشوائية
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
