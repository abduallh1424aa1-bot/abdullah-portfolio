import hmac
import html
import json
import re
from datetime import datetime
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Abdullah Al-Qahtani | عبدالله القحطاني",
    page_icon="🧭",
    layout="centered"
)

LINKEDIN = "https://www.linkedin.com/in/abdullah-al-qahtani-878bb32a7"
GPA = "3.71"

# مستويات المهارات: (كلاس التصميم، عرض الشريط)
LEVELS = {"adv": ("adv", 90), "mid": ("mid", 65), "beg": ("beg", 35)}

# ==========================================================
#  تسجيل الزيارات (ملف visits.json في مجلد المشروع)
# ==========================================================
VISITS_FILE = Path(__file__).parent / "visits.json"


def load_visits():
    try:
        return json.loads(VISITS_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_visit(lang, ref):
    visits = load_visits()
    visits.append(
        {
            "time": datetime.now().isoformat(timespec="seconds"),
            "lang": lang,
            "ref": ref,
        }
    )
    VISITS_FILE.write_text(json.dumps(visits, ensure_ascii=False), encoding="utf-8")


def get_admin_password():
    try:
        return str(st.secrets["ADMIN_PASSWORD"]), None
    except Exception as ex:
        return None, type(ex).__name__


# ==========================================================
#  المحتوى باللغتين - عدّل النصوص هنا
#  (أي شي تضيفه في "ar" أضفه في "en" بعد)
# ==========================================================
T = {
    "ar": {
        "dir": "rtl",
        "name": "عبدالله ناصر القحطاني",
        "title": "دعم فني ومراقبة شبكات | مطور ويب وOdoo",
        "tagline": "منفتح على فرص كمطور ويب وفي الشبكات والأمن السيبراني",
        "bio": (
            "خريج دبلوم برمجة وتطوير تطبيقات الويب من المؤسسة العامة للتدريب التقني "
            "والمهني (2024). أشتغل حاليًا في مراقبة الشبكات، وجمعت بين الدعم الفني "
            "وتطوير الويب وOdoo واختبار الجودة. أطور مساري اليوم نحو الأمن السيبراني."
        ),
        "cta": "تواصل معي على لينكدإن",
        "stat_gpa": "معدل الدبلوم من 5",
        "stat_roles": "أدوار وخبرات",
        "stat_certs": "شهادات ودورات",
        "stat_skills": "مهارات تقنية",
        "h_skills": "المهارات",
        "h_edu": "التعليم",
        "h_exp": "الخبرات والمشاريع",
        "h_certs": "الشهادات والدورات",
        "h_lang": "اللغات",
        "level": {"adv": "متقدم", "mid": "متوسط", "beg": "مبتدئ"},
        "skills": [
            ("الدعم الفني وHelp Desk", "adv"),
            ("مراقبة الشبكات واختبارات الاتصال", "adv"),
            ("تثبيت وتحديث Windows وOffice", "adv"),
            ("تطوير وتخصيص Odoo", "mid"),
            ("تطوير الويب", "mid"),
            ("اختبار الجودة QA", "mid"),
            ("أساسيات Linux", "beg"),
            ("أساسيات الأمن السيبراني", "beg"),
            ("إدارة المخاطر", "beg"),
        ],
        "experiences": [
            {
                "role": "أخصائي مراقبة شبكات",
                "org": "الدور الحالي",
                "desc": "مراقبة مستمرة لضمان استمرار الخدمة، واختبارات اتصال وحل الأعطال حتى عودة الاتصال.",
            },
            {
                "role": "أخصائي دعم فني",
                "org": "",
                "desc": "دعم عن بعد وميداني، تثبيت الأنظمة وتفعيل Office، تجهيز وصيانة الحواسيب.",
            },
            {
                "role": "مطور Odoo ومختبر جودة",
                "org": "مشروع مؤسسة الملك عبدالعزيز ورجاله للموهبة والإبداع (موهبة)",
                "desc": "تطوير وتخصيص وحدات وسير عمل Odoo، مع اختبار الجودة (QA) بخبرة عملية تزيد عن سنة.",
            },
            {
                "role": "مطور ويب",
                "org": "الجريسي للخدمات الإلكترونية",
                "desc": "بناء تطبيقات ويب ضمن فريق تقني محترف.",
            },
            {
                "role": "باحث ميداني",
                "org": "الهيئة العامة للإحصاء",
                "desc": "المشاركة في المسوح الاقتصادية والزراعية.",
            },
        ],
        "certs": [
            "Odoo 18 Functional",
            "أساسيات الأمن السيبراني",
            "إدارة المخاطر",
            "أمن الشبكات",
            "أساسيات Linux",
            "مبادئ الذكاء الاصطناعي",
        ],
        "education": {
            "degree": "دبلوم برمجة وتطوير تطبيقات الويب",
            "school": "المؤسسة العامة للتدريب التقني والمهني",
            "meta": f"تخرج 2024 | المعدل {GPA} من 5",
        },
        "languages": {"العربية": "اللغة الأم", "الإنجليزية": "جيد"},
        "footer": "صُممت هذه الصفحة وبُنيت بلغة Python وStreamlit | تُسجل الزيارات بشكل مجهول للإحصاءات",
    },
    "en": {
        "dir": "ltr",
        "name": "Abdullah Nasser Al-Qahtani",
        "title": "Technical Support & Network Monitoring | Web & Odoo Developer",
        "tagline": "Open to opportunities in web development, networking, and cybersecurity",
        "bio": (
            "Graduate of the Web Application Programming and Development diploma at the "
            "Technical and Vocational Training Corporation (2024). I currently work in "
            "network monitoring, with hands-on experience across technical support, web "
            "development, Odoo, and quality assurance. I'm now growing toward cybersecurity."
        ),
        "cta": "Connect with me on LinkedIn",
        "stat_gpa": "Diploma GPA out of 5",
        "stat_roles": "Roles & experiences",
        "stat_certs": "Certificates & courses",
        "stat_skills": "Technical skills",
        "h_skills": "Skills",
        "h_edu": "Education",
        "h_exp": "Experience & Projects",
        "h_certs": "Certificates & Courses",
        "h_lang": "Languages",
        "level": {"adv": "Advanced", "mid": "Intermediate", "beg": "Beginner"},
        "skills": [
            ("Technical Support & Help Desk", "adv"),
            ("Network Monitoring & Connectivity Testing", "adv"),
            ("Windows & Office Installation and Updates", "adv"),
            ("Odoo Development & Customization", "mid"),
            ("Web Development", "mid"),
            ("Quality Assurance (QA) Testing", "mid"),
            ("Linux Fundamentals", "beg"),
            ("Cybersecurity Fundamentals", "beg"),
            ("Risk Management", "beg"),
        ],
        "experiences": [
            {
                "role": "Network Monitoring Specialist",
                "org": "Current role",
                "desc": "Continuous monitoring to keep services running, connectivity testing, and troubleshooting until the connection is restored.",
            },
            {
                "role": "Technical Support Specialist",
                "org": "",
                "desc": "Remote and on-site support, operating system installation, Office activation, and computer setup and maintenance.",
            },
            {
                "role": "Odoo Developer & QA Tester",
                "org": "King Abdulaziz and His Companions Foundation for Giftedness and Creativity (Mawhiba) project",
                "desc": "Developed and customized Odoo modules and workflows, along with QA testing, with over a year of hands-on QA experience.",
            },
            {
                "role": "Web Developer",
                "org": "Al-Jeraisy Electronic Services",
                "desc": "Built web applications as part of a professional technical team.",
            },
            {
                "role": "Field Researcher",
                "org": "General Authority for Statistics",
                "desc": "Took part in economic and agricultural field surveys.",
            },
        ],
        "certs": [
            "Odoo 18 Functional",
            "Cybersecurity Fundamentals",
            "Risk Management",
            "Network Security",
            "Linux Fundamentals",
            "Principles of Artificial Intelligence",
        ],
        "education": {
            "degree": "Diploma in Web Application Programming and Development",
            "school": "Technical and Vocational Training Corporation (TVTC)",
            "meta": f"Graduated 2024 | GPA {GPA} / 5",
        },
        "languages": {"Arabic": "Native", "English": "Good"},
        "footer": "Designed and built with Python and Streamlit | Visits are logged anonymously for statistics",
    },
}

# ==========================================================
#  وضع الأدمن: الرابط ?admin=1 يفعّل لوحة الإحصاءات طول الجلسة
# ==========================================================
if "admin" in st.query_params:
    st.session_state["is_admin"] = True
is_admin_view = st.session_state.get("is_admin", False)

# ==========================================================
#  اختيار اللغة (الرابط ?lang=en يفتح الصفحة بالإنجليزي)
# ==========================================================
default_lang = "en" if st.query_params.get("lang") == "en" else "ar"
choice = st.radio(
    "Language",
    ["العربية", "English"],
    index=0 if default_lang == "ar" else 1,
    horizontal=True,
    label_visibility="collapsed",
)
lang = "ar" if choice == "العربية" else "en"
if is_admin_view:
    st.query_params["admin"] = "1"
st.query_params["lang"] = lang
d = T[lang]

# تسجيل الزيارة مرة وحدة لكل جلسة (زياراتك أنت كأدمن ما تنحسب)
if not is_admin_view and not st.session_state.get("counted"):
    save_visit(lang, st.query_params.get("ref", "direct"))
    st.session_state["counted"] = True

# ==========================================================
#  تحميل التصميم من style.css
# ==========================================================
css_text = (Path(__file__).parent / "style.css").read_text(encoding="utf-8")
css_text = re.sub(r"/\*.*?\*/", "", css_text, flags=re.S)  # حذف التعليقات
css_text = "\n".join(line for line in css_text.splitlines() if line.strip())  # حذف الأسطر الفاضية
st.markdown(f"<style>{css_text}</style>", unsafe_allow_html=True)

# اتجاه الصفحة حسب اللغة
st.markdown(f"<style>.stApp{{direction:{d['dir']};}}</style>", unsafe_allow_html=True)

# ==========================================================
#  بناء الصفحة
# ==========================================================
e = html.escape


def skills_html():
    out = []
    for skill, level in d["skills"]:
        css, width = LEVELS[level]
        out.append(
            f'<div class="sk"><div class="sk-top"><span>{e(skill)}</span>'
            f'<span class="lv lv-{css}">{e(d["level"][level])}</span></div>'
            f'<div class="bar"><i style="width:{width}%"></i></div></div>'
        )
    return '<div class="skgrid">' + "".join(out) + "</div>"


def education_html():
    edu = d["education"]
    return (
        '<div class="two single"><div class="card">'
        f'<div class="t">{e(edu["degree"])}</div>'
        f'<div class="s">{e(edu["school"])}</div>'
        f'<div class="m">{e(edu["meta"])}</div>'
        "</div></div>"
    )


def experience_html():
    out = []
    for x in d["experiences"]:
        org = f'<div class="o">{e(x["org"])}</div>' if x["org"] else ""
        out.append(
            f'<div class="tl-item"><div class="r">{e(x["role"])}</div>{org}'
            f'<div class="d">{e(x["desc"])}</div></div>'
        )
    return '<div class="tl">' + "".join(out) + "</div>"


def chips_html(items):
    return '<div class="chips">' + "".join(f'<span class="chip">{e(i)}</span>' for i in items) + "</div>"


def languages_html():
    langs = "".join(
        f'<div class="lang"><span>{e(k)}</span><span>{e(v)}</span></div>'
        for k, v in d["languages"].items()
    )
    return f'<div class="two single"><div class="card">{langs}</div></div>'


def section(heading, body):
    return f'<section class="sec"><h2>{e(heading)}</h2>{body}</section>'


# ==========================================================
#  الصفحة (ترتيب الأقسام: غيّر ترتيب الأسطر لتغيير الترتيب)
# ==========================================================
page = (
    f'<div class="hero"><div class="open"><i></i>{e(d["tagline"])}</div>'
    f'<h1>{e(d["name"])}</h1><div class="role">{e(d["title"])}</div>'
    f'<p>{e(d["bio"])}</p>'
    f'<a class="cta" href="{e(LINKEDIN)}" target="_blank" rel="noopener">{e(d["cta"])}</a></div>'
    f'<div class="stats">'
    f'<div class="stat"><b>{e(GPA)}</b><span>{e(d["stat_gpa"])}</span></div>'
    f'<div class="stat"><b>{len(d["experiences"])}</b><span>{e(d["stat_roles"])}</span></div>'
    f'<div class="stat"><b>{len(d["certs"])}</b><span>{e(d["stat_certs"])}</span></div>'
    f'<div class="stat"><b>{len(d["skills"])}</b><span>{e(d["stat_skills"])}</span></div></div>'
    + section(d["h_skills"], skills_html())
    + section(d["h_edu"], education_html())
    + section(d["h_exp"], experience_html())
    + section(d["h_certs"], chips_html(d["certs"]))
    + section(d["h_lang"], languages_html())
    + f'<div class="foot">{e(d["footer"])}</div>'
)

st.markdown(page, unsafe_allow_html=True)

# ==========================================================
#  لوحة الإحصاءات (تظهر فقط لو فتحت الرابط بـ ?admin=1)
# ==========================================================
if is_admin_view:
    st.divider()
    pwd = st.text_input("Admin password", type="password")
    real, err = get_admin_password()
    if real is None:
        st.warning(f"التطبيق ما قدر يقرأ كلمة السر من secrets.toml ({err})")
    elif pwd and hmac.compare_digest(pwd.strip(), real.strip()):
        import pandas as pd

        st.success("تم الدخول بنجاح")
        df = pd.DataFrame(load_visits())
        st.write(f"إجمالي الزيارات: {len(df)}")
        if not df.empty:
            df["day"] = df["time"].str[:10]
            st.write("الزيارات حسب اليوم")
            st.bar_chart(df.groupby("day").size())
            st.write("المصدر (ref)")
            st.write(df["ref"].value_counts())
            st.write("اللغة")
            st.write(df["lang"].value_counts())
            st.write("آخر 20 زيارة")
            st.dataframe(df.tail(20))
    elif pwd:
        st.error("كلمة السر غير صحيحة")
