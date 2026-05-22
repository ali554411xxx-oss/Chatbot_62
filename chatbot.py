import streamlit as st
from groq import Groq

st.set_page_config(page_title="بوتي", page_icon="🤖", layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "tab" not in st.session_state:
    st.session_state.tab = "login"
if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;700;900&display=swap");
* { font-family: Tajawal, sans-serif !important; direction: rtl; box-sizing: border-box; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stApp {
    background: #020818;
    background-image:
        radial-gradient(1px 1px at 10% 15%, white 0%, transparent 100%),
        radial-gradient(1px 1px at 25% 40%, white 0%, transparent 100%),
        radial-gradient(1px 1px at 40% 10%, white 0%, transparent 100%),
        radial-gradient(1px 1px at 55% 60%, white 0%, transparent 100%),
        radial-gradient(1px 1px at 70% 25%, white 0%, transparent 100%),
        radial-gradient(1px 1px at 85% 75%, white 0%, transparent 100%),
        radial-gradient(1px 1px at 15% 85%, white 0%, transparent 100%),
        radial-gradient(1px 1px at 90% 45%, white 0%, transparent 100%),
        radial-gradient(1px 1px at 35% 70%, white 0%, transparent 100%),
        radial-gradient(1px 1px at 60% 90%, white 0%, transparent 100%),
        radial-gradient(2px 2px at 5% 50%, rgba(100,180,255,0.9) 0%, transparent 100%),
        radial-gradient(2px 2px at 80% 20%, rgba(180,100,255,0.9) 0%, transparent 100%),
        radial-gradient(2px 2px at 50% 80%, rgba(255,200,100,0.7) 0%, transparent 100%),
        radial-gradient(ellipse at 20% 30%, rgba(80,30,200,0.15) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 70%, rgba(0,100,255,0.1) 0%, transparent 50%);
}
.page { min-height:100vh; display:flex; align-items:center; justify-content:center; padding:1rem; position:relative; z-index:1; }
.glass {
    background: rgba(255,255,255,0.07);
    backdrop-filter: blur(25px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 28px;
    padding: 2.5rem 2rem;
    width: 100%;
    max-width: 420px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.15);
    position: relative;
}
.glass::before {
    content: "";
    position: absolute; top:0; left:10%; right:10%; height:1px;
    background: linear-gradient(90deg, transparent, rgba(167,139,250,0.8), rgba(96,165,250,0.8), transparent);
}
.logo { text-align:center; margin-bottom:1.5rem; }
.logo h1 {
    font-size:2rem; font-weight:900; margin:0.4rem 0 0;
    background: linear-gradient(135deg,#a78bfa,#60a5fa,#34d399);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
    animation: fl 3s ease-in-out infinite;
}
@keyframes fl { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-5px)} }
.logo p { color:rgba(255,255,255,0.4); font-size:0.8rem; margin:0.2rem 0 0; }
.tabs { display:flex; background:rgba(255,255,255,0.05); border-radius:12px; padding:4px; margin-bottom:1.4rem; border:1px solid rgba(255,255,255,0.08); }
.tab { flex:1; text-align:center; padding:8px; border-radius:9px; font-size:0.9rem; font-weight:500; color:rgba(255,255,255,0.4); }
.tab.on { background:linear-gradient(135deg,rgba(99,52,255,0.6),rgba(0,180,255,0.4)); color:#fff; }
.gbtn { width:100%; display:flex; align-items:center; justify-content:center; gap:10px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:14px; padding:12px; color:#fff; font-size:0.95rem; margin-bottom:1.2rem; }
.sep { display:flex; align-items:center; gap:10px; margin-bottom:1.2rem; color:rgba(255,255,255,0.3); font-size:0.8rem; }
.sep::before,.sep::after { content:""; flex:1; height:1px; background:rgba(255,255,255,0.1); }
.stTextInput input { background:rgba(255,255,255,0.07) !important; border:1px solid rgba(255,255,255,0.15) !important; border-radius:12px !important; color:#fff !important; font-family:Tajawal,sans-serif !important; direction:rtl !important; padding:12px 14px !important; }
.stTextInput label { color:rgba(255,255,255,0.6) !important; font-family:Tajawal,sans-serif !important; }
.stButton > button { width:100% !important; background:linear-gradient(135deg,#6334ff,#00c8ff) !important; border:none !important; border-radius:14px !important; padding:13px !important; color:#fff !important; font-size:1rem !important; font-weight:700 !important; font-family:Tajawal,sans-serif !important; box-shadow:0 4px 20px rgba(99,52,255,0.4) !important; }
.chat-header { text-align:center; padding:1rem 0 0.5rem; position:relative; z-index:1; }
.chat-header h1 { font-size:1.8rem; font-weight:900; background:linear-gradient(135deg,#a78bfa,#60a5fa,#34d399); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; margin:0.3rem 0 0; }
.chat-header p { color:rgba(255,255,255,0.4); font-size:0.82rem; margin:0.2rem 0 0.3rem; }
.online { display:inline-flex; align-items:center; gap:5px; background:rgba(52,211,153,0.1); border:1px solid rgba(52,211,153,0.25); color:#34d399; font-size:0.75rem; padding:3px 12px; border-radius:20px; }
.online::before { content:""; width:6px; height:6px; background:#34d399; border-radius:50%; animation:pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.3} }
.stats { display:flex; justify-content:center; gap:1.5rem; padding:0.6rem 1rem; background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.05); border-radius:12px; margin:0.5rem 0; position:relative; z-index:1; }
.stat { text-align:center; }
.stat b { display:block; font-size:1.1rem; font-weight:700; color:#a78bfa; }
.stat small { font-size:0.65rem; color:rgba(255,255,255,0.3); }
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) { background:linear-gradient(135deg,rgba(99,52,255,0.2),rgba(99,52,255,0.08)) !important; border:1px solid rgba(99,52,255,0.25) !important; border-radius:18px 18px 4px 18px !important; padding:1rem 1.2rem !important; margin:0.4rem 0 0.4rem 2rem !important; color:#e2d9ff !important; }
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) { background:linear-gradient(135deg,rgba(0,180,255,0.08),rgba(52,211,153,0.05)) !important; border:1px solid rgba(0,180,255,0.15) !important; border-radius:18px 18px 18px 4px !important; padding:1rem 1.2rem !important; margin:0.4rem 2rem 0.4rem 0 !important; color:#d1f5ff !important; }
[data-testid="stChatInputContainer"] { background:rgba(255,255,255,0.04) !important; border:1px solid rgba(255,255,255,0.1) !important; border-radius:16px !important; padding:0.3rem 0.5rem !important; }
[data-testid="stChatInputContainer"] textarea { color:#fff !important; direction:rtl !important; font-family:Tajawal,sans-serif !important; }
[data-testid="stChatInputContainer"] button { background:linear-gradient(135deg,#6334ff,#00c8ff) !important; border-radius:10px !important; border:none !important; }
[data-testid="stMarkdownContainer"] p { color:inherit !important; line-height:1.8 !important; }
</style>
""", unsafe_allow_html=True)

# ========== صفحة التسجيل ==========
if not st.session_state.logged_in:
    t = st.session_state.tab
    st.markdown(f"""<div class="page"><div class="glass">
        <div class="logo"><h1>🤖 بوتي</h1><p>مساعدك الذكي الشخصي 🚀</p></div>
        <div class="tabs">
            <div class="tab {'on' if t=='login' else ''}">تسجيل الدخول</div>
            <div class="tab {'on' if t=='register' else ''}">حساب جديد</div>
        </div>
        <div class="gbtn">🔵 متابعة مع Google</div>
        <div class="sep">أو</div>
    </div></div>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.5, 3, 0.5])
    with col2:
        if t == "register":
            name = st.text_input("👤 الاسم", placeholder="اكتب اسمك...")
        email = st.text_input("📧 البريد", placeholder="example@email.com")
        pwd = st.text_input("🔒 كلمة السر", placeholder="••••••••", type="password")
        if t == "register":
            pwd2 = st.text_input("🔒 تأكيد السر", placeholder="••••••••", type="password")
        st.markdown("<br>", unsafe_allow_html=True)
        if t == "login":
            if st.button("🚀 دخول"):
                if email and pwd:
                    st.session_state.logged_in = True
                    st.session_state.username = email.split("@")[0]
                    st.rerun()
                else:
                    st.error("أدخل البريد وكلمة السر")
        else:
            if st.button("✨ إنشاء الحساب"):
                if email and pwd:
                    if pwd == pwd2:
                        st.session_state.logged_in = True
                        st.session_state.username = name if name else email.split("@")[0]
                        st.rerun()
                    else:
                        st.error("كلمة السر غير متطابقة")
                else:
                    st.error("أكمل جميع الحقول")
        if t == "login":
            if st.button("ليس لديك حساب؟ سجّل الآن"):
                st.session_state.tab = "register"
                st.rerun()
        else:
            if st.button("لديك حساب؟ سجّل دخولك"):
                st.session_state.tab = "login"
                st.rerun()

# ========== صفحة البوت ==========
else:
    um = len([m for m in st.session_state.messages if m["role"] == "user"])
    tm = len(st.session_state.messages)

    st.markdown(f"""<div class="chat-header">
        <h1>🤖 بوتي</h1>
        <p>أهلاً {st.session_state.username} 👋</p>
        <span class="online">متصل ويعمل</span>
    </div>
    <div class="stats">
        <div class="stat"><b>{um}</b><small>أسئلتك</small></div>
        <div class="stat"><b>{tm}</b><small>الرسائل</small></div>
        <div class="stat"><b>∞</b><small>قدرة بوتي</small></div>
    </div>""", unsafe_allow_html=True)

    c1, c2, c3 = st.columns([3, 1, 1])
    with c3:
        if st.button("🚪 خروج"):
            st.session_state.logged_in = False
            st.session_state.messages = []
            st.rerun()

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if not st.session_state.messages:
        with st.chat_message("assistant"):
            st.markdown(f"👋 **أهلاً {st.session_state.username}! أنا بوتي 🚀**\n\nاسألني عن أي شيء!")

    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except:
        st.error("لم يتم إعداد مفتاح API")
        st.stop()

    client = Groq(api_key=api_key)

    if prompt := st.chat_input("💬 اكتب سؤالك هنا..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("بوتي يفكر..."):
                try:
                    res = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[{"role": "system", "content": "أنت بوتي، مساعد ذكي وودود باللغة العربية."}]
                        + [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                        temperature=0.7, max_tokens=1024
                    )
                    reply = res.choices[0].message.content
                    st.markdown(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                except Exception as e:
                    st.error(f"خطأ: {e}")
        st.rerun()

    c1, c2, c3 = st.columns([2, 1, 2])
    with c2:
        if st.button("🗑️ مسح"):
            st.session_state.messages = []
            st.rerun()



