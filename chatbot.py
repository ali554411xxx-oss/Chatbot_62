<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;900&display=swap');
* { font-family: 'Tajawal', sans-serif !important; direction: rtl; }

.stApp {
    background: #020818;
    min-height: 100vh;
}
.stApp::before {
    content: '';
    position: fixed;
    top:0;left:0;right:0;bottom:0;
    background-image:
        radial-gradient(1px 1px at 10% 15%, rgba(255,255,255,0.9) 0%, transparent 100%),
        radial-gradient(1px 1px at 20% 35%, rgba(255,255,255,0.7) 0%, transparent 100%),
        radial-gradient(1px 1px at 30% 10%, rgba(255,255,255,0.8) 0%, transparent 100%),
        radial-gradient(1px 1px at 40% 50%, rgba(255,255,255,0.6) 0%, transparent 100%),
        radial-gradient(1px 1px at 50% 25%, rgba(255,255,255,0.9) 0%, transparent 100%),
        radial-gradient(1px 1px at 60% 70%, rgba(255,255,255,0.7) 0%, transparent 100%),
        radial-gradient(1px 1px at 70% 5%,  rgba(255,255,255,0.8) 0%, transparent 100%),
        radial-gradient(1px 1px at 80% 45%, rgba(255,255,255,0.6) 0%, transparent 100%),
        radial-gradient(1px 1px at 90% 20%, rgba(255,255,255,0.9) 0%, transparent 100%),
        radial-gradient(1px 1px at 15% 80%, rgba(255,255,255,0.7) 0%, transparent 100%),
        radial-gradient(1px 1px at 25% 60%, rgba(255,255,255,0.5) 0%, transparent 100%),
        radial-gradient(1px 1px at 35% 90%, rgba(255,255,255,0.8) 0%, transparent 100%),
        radial-gradient(1px 1px at 45% 75%, rgba(255,255,255,0.6) 0%, transparent 100%),
        radial-gradient(1px 1px at 55% 40%, rgba(255,255,255,0.9) 0%, transparent 100%),
        radial-gradient(1px 1px at 65% 85%, rgba(255,255,255,0.7) 0%, transparent 100%),
        radial-gradient(1px 1px at 75% 55%, rgba(255,255,255,0.5) 0%, transparent 100%),
        radial-gradient(1px 1px at 85% 30%, rgba(255,255,255,0.8) 0%, transparent 100%),
        radial-gradient(1px 1px at 95% 65%, rgba(255,255,255,0.6) 0%, transparent 100%),
        radial-gradient(2px 2px at 5%  50%, rgba(100,180,255,0.8) 0%, transparent 100%),
        radial-gradient(2px 2px at 88% 88%, rgba(180,100,255,0.8) 0%, transparent 100%),
        radial-gradient(2px 2px at 33% 33%, rgba(255,200,100,0.6) 0%, transparent 100%),
        radial-gradient(2px 2px at 77% 22%, rgba(100,255,200,0.6) 0%, transparent 100%),
        radial-gradient(ellipse at 20% 30%, rgba(80,30,200,0.1) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 70%, rgba(0,100,255,0.07) 0%, transparent 50%);
    pointer-events: none;
    z-index: 0;
    animation: twinkle 4s ease-in-out infinite alternate;
}
@keyframes twinkle { 0%{opacity:0.7} 100%{opacity:1} }

#MainMenu, footer, header {visibility: hidden;}
.block-container { padding-top:1rem !important; max-width:750px !important; position:relative; z-index:1; }

.robot-header { text-align:center; padding:1.2rem 1rem 0.8rem; }
.robot-img-container { position:relative; display:inline-block; margin-bottom:0.5rem; }
.robot-img {
    width:110px; height:110px; object-fit:contain;
    filter: drop-shadow(0 0 20px rgba(99,52,255,0.7)) drop-shadow(0 0 40px rgba(0,200,255,0.4));
    animation: float 3s ease-in-out infinite;
}
@keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }

.robot-glow {
    position:absolute; bottom:-8px; left:50%; transform:translateX(-50%);
    width:80px; height:12px;
    background:radial-gradient(ellipse, rgba(99,52,255,0.5) 0%, transparent 70%);
    filter:blur(4px);
    animation: gpulse 3s ease-in-out infinite;
}
@keyframes gpulse { 0%,100%{opacity:0.5;transform:translateX(-50%) scaleX(1)} 50%{opacity:1;transform:translateX(-50%) scaleX(1.4)} }

.hero-title {
    font-size:2.2rem; font-weight:900; margin:0.3rem 0 0;
    background:linear-gradient(135deg,#a78bfa,#60a5fa,#34d399,#f472b6);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
    background-clip:text; background-size:300% auto;
    animation:shimmer 4s ease-in-out infinite;
}
@keyframes shimmer { 0%{background-position:0% center} 50%{background-position:100% center} 100%{background-position:0% center} }

.hero-subtitle { color:rgba(255,255,255,0.4); font-size:0.85rem; font-weight:300; margin:0.2rem 0 0.5rem; letter-spacing:2px; }
.status-badge {
    display:inline-flex; align-items:center; gap:6px;
    background:rgba(52,211,153,0.1); border:1px solid rgba(52,211,153,0.25);
    color:#34d399; font-size:0.75rem; padding:3px 12px; border-radius:20px;
}
.status-badge::before { content:''; width:6px; height:6px; background:#34d399; border-radius:50%; animation:pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.4;transform:scale(0.7)} }

.stats-bar {
    display:flex; justify-content:center; gap:1.5rem; padding:0.6rem 1rem;
    background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.05);
    border-radius:12px; margin:0.5rem 0;
}
.stat-item { text-align:center; }
.stat-num { font-size:1.1rem; font-weight:700; color:#a78bfa; }
.stat-label { font-size:0.65rem; color:rgba(255,255,255,0.3); }

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background:linear-gradient(135deg,rgba(99,52,255,0.2),rgba(99,52,255,0.08)) !important;
    border:1px solid rgba(99,52,255,0.25) !important;
    border-radius:18px 18px 4px 18px !important;
    padding:1rem 1.2rem !important;
    margin:0.4rem 0 0.4rem 2rem !important;
    color:#e2d9ff !important;
    animation:slideInRight 0.3s ease;
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background:linear-gradient(135deg,rgba(0,180,255,0.08),rgba(52,211,153,0.05)) !important;
    border:1px solid rgba(0,180,255,0.15) !important;
    border-radius:18px 18px 18px 4px !important;
    padding:1rem 1.2rem !important;
    margin:0.4rem 2rem 0.4rem 0 !important;
    color:#d1f5ff !important;
    animation:slideInLeft 0.3s ease;
}
@keyframes slideInRight { from{opacity:0;transform:translateX(15px)} to{opacity:1;transform:translateX(0)} }
@keyframes slideInLeft  { from{opacity:0;transform:translateX(-15px)} to{opacity:1;transform:translateX(0)} }

[data-testid="stChatInputContainer"] {
    background:rgba(255,255,255,0.04) !important;
    border:1px solid rgba(255,255,255,0.1) !important;
    border-radius:16px !important;
    padding:0.3rem 0.5rem !important;
}
[data-testid="stChatInputContainer"]:focus-within {
    border-color:rgba(99,52,255,0.5) !important;
    box-shadow:0 0 20px rgba(99,52,255,0.1) !important;
}
[data-testid="stChatInputContainer"] textarea {
    color:#ffffff !important; direction:rtl !important;
    font-family:'Tajawal',sans-serif !important;
}
[data-testid="stChatInputContainer"] textarea::placeholder { color:rgba(255,255,255,0.25) !important; }
[data-testid="stChatInputContainer"] button {
    background:linear-gradient(135deg,#6334ff,#00c8ff) !important;
    border-radius:10px !important; border:none !important;
}
.stButton button {
    background:rgba(255,255,255,0.04) !important;
    border:1px solid rgba(255,255,255,0.08) !important;
    color:rgba(255,255,255,0.4) !important;
    border-radius:10px !important;
    font-family:'Tajawal',sans-serif !important;
    font-size:0.8rem !important;
}
[data-testid="stMarkdownContainer"] p { color:inherit !important; line-height:1.8 !important; }
</style>
""", unsafe_allow_html=True)

# ===== هيدر الروبوت =====
st.markdown(f"""
<div class="robot-header">
    <div class="robot-img-container">
        <img src="data:image/jpeg;base64,{ROBOT_B64}" class="robot-img" alt="بوتي"/>
        <div class="robot-glow"></div>
    </div>
    <h1 class="hero-title">بوتي</h1>
    <p class="hero-subtitle">مساعدك الذكي · powered by Llama 3.1</p>
    <span class="status-badge">متصل ويعمل</span>
</div>

