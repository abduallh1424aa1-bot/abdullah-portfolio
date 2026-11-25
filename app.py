import hmac
import html
import json
import re
from datetime import datetime
from pathlib import Path
CV_FILE = Path(__file__).parent / "CV.pdf"


import streamlit as st

st.set_page_config(
    page_title="Abdullah Al-Qahtani | عبدالله القحطاني",
    page_icon="🧭",
    layout="centered",
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
#  المهارات المكتسبة لكل خبرة (مشتركة بين العربي والإنجليزي)
# ==========================================================
SK_NET = [
    "Network Monitoring",
    "Network Troubleshooting",
    "Connectivity Testing",
    "Ping Commands",
]
SK_IT = [
    "IT Technical Support",
    "Windows Installation & Configuration",
    "Microsoft Office Installation & Activation",
    "Active Directory & Domain Join",
    "PC & Laptop Troubleshooting",
    "Hardware & Software Maintenance",
    "Remote Technical Support",
    "IT Incident Management",
]
SK_ODOO = [
    "Odoo ERP",
    "Software Quality Assurance (QA)",
    "Functional Testing",
    "BRD Analysis & Requirements Validation",
    "Approval Workflows",
    "Dashboard Testing",
    "Bug Tracking & Reporting",
    "Microsoft Excel",
    "Team Coordination",
    "Project Progress Tracking",
]

# ==========================================================
#  المحتوى باللغتين - عدّل النصوص هنا
#  (أي شي تضيفه في "ar" أضفه في "en" بعد)
# ==========================================================
T = {
    # ------------------------------ العربي ------------------------------
    "ar": {
        "dir": "rtl",
        "name": "عبدالله ناصر القحطاني",
        "title": "دعم فني ومراقبة شبكات | مطور ويب وOdoo",
        "tagline": "متاح على فرص كمطور ويب وفي الشبكات والأمن السيبراني",
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
        "h_tasks": "المهام والمسؤوليات",
        "h_gained": "المهارات المكتسبة",
        "level": {"adv": "متقدم", "mid": "متوسط", "beg": "مبتدئ"},
        "skills": [
            ("مراقبة الشبكات واختبارات الاتصال", "adv"),
            ("تثبيت وتحديث Windows وOffice", "adv"),
            ("اختبار الجودة QA", "adv"),
            ("تطويرodoo ", "mid"),
            ("الدعم الفني وHelp Desk", "mid"),
            ("أساسيات Linux", "mid"),
            ("أساسيات الأمن السيبراني", "beg"),
            ("إدارة المخاطر", "beg"),
        ],
        "experiences": [
    {
        "role": "أخصائي مراقبة شبكات العملاء",
        "org": "شركة الجريسي للخدمات الإلكترونية",
        "date": "تاريخ الانضمام: 18 أغسطس 2024",
        "desc": "مراقبة شبكات وخدمات العملاء بشكل مستمر ومتابعة الأعطال حتى استعادة الخدمة.",
        "tasks": [
            # اترك مهامك الحالية كما هي
        ],
        "skills": SK_NET,
    },  {
        "role": "أخصائي دعم فني وتقنية معلومات",
        "org": "شركة الجريسي للخدمات الإلكترونية",
        "date": "تاريخ الانضمام: 18 أغسطس 2024",
        "desc": "دعم المستخدمين عن بعد وحضوريًا، وتجهيز الأجهزة وصيانتها وربطها بالشبكة.",
        "tasks": [
            # اترك مهامك الحالية كما هي
        ],
        "skills": SK_IT,
    },
            {
                "role": "مطور ومختبر Odoo",
                "org": "شركة الجريسي للخدمات الإلكترونية",
                "date": "تاريخ الانضمام: 18 أغسطس 2024",
                "desc": "التنسيق بين فريق التطوير وفريق الجودة، واختبار خدمات Odoo في أكثر من 5 لوحات تحكم.",
                "tasks": [
                    # اترك مهامك الحالية كما هي
                ],

                "skills": SK_ODOO,
            },
            {
                "role": "باحث ميداني",
                "org": "الهيئة العامة للإحصاء",
                "desc": "المشاركة في المسح الزراعي والمسح التجاري وجمع البيانات الميدانية.",
                "groups": [
                    {
                        "title": "المسح الزراعي",
                        "tasks": [
                            "حصر أعداد أشجار النخيل والأشجار والآبار الزراعية.",
                            "جمع بيانات الثروة الداجنة وتصنيفها إلى دواجن لاحم وبياض وأمهات.",
                            "تسجيل أنواع الأنشطة الزراعية ومكونات المزارع وبيانات ملكيتها.",
                            "جمع بيانات الدخل والإيرادات والمصروفات والتكاليف التشغيلية للمزارع.",
                            "تغطية مناطق جغرافية متعددة، بما فيها المناطق النائية، وتنفيذ الزيارات الميدانية.",
                        ],
                    },
                    {
                        "title": "المسح التجاري",
                        "tasks": [
                            "تنفيذ المسح التجاري ميدانيًا وزيارة وجمع بيانات أكثر من 1,000 محل ومنشأة تجارية.",
                            "تصنيف المحلات حسب نوع النشاط وطبيعة الخدمات أو المنتجات المقدمة.",
                            "جمع بيانات الإيرادات والدخل والتحقق من المعلومات التجارية.",
                            "تسجيل البيانات الميدانية والتحقق من اكتمالها ودقتها.",
                        ],
                    },
                ],
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
        "languages": {"العربية :": "اللغة الأم", "الإنجليزية :": "جيد"},
    },
    # ---------------------------- الإنجليزي ----------------------------
    "en": {
        "dir": "ltr",
        "name": "Abdullah Nasser Al-Qahtani",
        "title": "Technical Support & Network Monitoring | Web & Odoo Developer" ,
        "org": "Al-Jreisi Electronic Services Company",
        "date": "Joined: 18 August 2024",
        "tagline": "Open to opportunities in web development, networking, and cybersecurity",
        "org": "Al-Jreisi Electronic Services Company",
        "date": "Joined: 18 August 2024",
        "org": "Al-Jreisi Electronic Services Company",
        "date": "Joined: 18 August 2024",
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
        "h_tasks": "Responsibilities",
        "h_gained": "Skills gained",
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
                "role": "Customer Network Monitoring Specialist",
                "org": "Service provider | Current role",
                "desc": "Continuous monitoring of customer networks and services, following faults until service is restored.",
                "tasks": [
                    "Continuously monitoring customer networks and services, and detecting service outages (Down).",
                    "Performing troubleshooting to identify and resolve faults.",
                    "Using network commands such as Ping to verify connectivity and measure device response.",
                    "Running connectivity tests and analyzing results to help identify the causes of faults.",
                    "Opening technical support tickets for faults and tracking their numbers and handling status.",
                    "Coordinating with technical teams and service providers to follow up on issues and escalate them when needed.",
                    "Following faults continuously until connectivity is restored and service is confirmed back.",
                ],
                "skills": SK_NET,
            },
            {
                "role": "IT Technical Support Specialist",
                "org": "",
                "desc": "Remote and on-site user support, device setup and maintenance, and network connection.",
                "tasks": [
                    "Providing remote and on-site technical support to users and resolving technical issues.",
                    "Installing, reconfiguring, and updating Windows operating systems.",
                    "Installing and activating Microsoft Office and desktop applications.",
                    "Preparing and configuring desktop and laptop computers for employees.",
                    "Joining computers to the company domain (Active Directory).",
                    "Diagnosing and repairing faults in desktop and laptop computers and their components.",
                    "Maintaining computers and resolving performance and operation issues.",
                    "Setting up devices and connecting them to the network, services, and internal systems.",
                    "Receiving technical incident reports and following them up until resolved.",
                    "Helping users resolve software, system, and hardware issues.",
                ],
                "skills": SK_IT,
            },
            {
                "role": "Odoo Systems Coordinator & QA Tester",
                "org": "King Abdulaziz and His Companions Foundation for Giftedness and Creativity (Mawhiba) project",
                "desc": "Coordinating between the development and QA teams, and testing Odoo services across 5+ dashboards.",
                "tasks": [
                    "Coordinating between Mawhiba's internal development team and the quality assurance (QA) team.",
                    "Working on more than 5 dashboards for different services within the Odoo system.",
                    "Handling services that rely on approval workflows, as well as services without approval chains.",
                    "Reviewing Business Requirements Documents (BRD) and analyzing functional requirements before testing begins.",
                    "Verifying that the developed services match the requirements defined in the BRD.",
                    "Testing services and functions after development is complete, and verifying results and workflow integrity.",
                    "Performing functional testing and verifying that requests move correctly between workflow and approval stages.",
                    "Detecting, documenting, and reporting bugs and observations to the development team for resolution.",
                    "Retesting services after fixes to confirm that the issues were resolved.",
                    "Preparing and updating Microsoft Excel files to document delivered services, test status, and observations.",
                    "Tracking work progress and coordinating service status between the development team, the project manager, and the Mawhiba team.",
                    "Preparing and sharing progress updates and keeping the status of services and tests clear.",
                ],
                "skills": SK_ODOO,
            },
            {
                "role": "Field Researcher",
                "org": "General Authority for Statistics",
                "desc": "Took part in the agricultural and commercial surveys, collecting field data.",
                "groups": [
                    {
                        "title": "Agricultural Survey",
                        "tasks": [
                            "Counting palm trees, other trees, and agricultural wells.",
                            "Collecting poultry data and classifying it into broilers, layers, and breeders.",
                            "Recording types of agricultural activity, farm components, and ownership data.",
                            "Collecting income, revenue, expense, and operating cost data for farms.",
                            "Covering multiple geographic areas, including remote regions, through field visits.",
                        ],
                    },
                    {
                        "title": "Commercial Survey",
                        "tasks": [
                            "Conducting field visits and collecting data from more than 1,000 shops and commercial establishments.",                            "Collecting commercial registration data and the economic activities of establishments.",
                            "Classifying shops by activity type and the nature of the services or products offered.",
                            "Collecting revenue and income data and verifying commercial information.",
                            "Recording field data and verifying its completeness and accuracy.",
                        ],
                    },
                ],
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
#  دوال بناء الأقسام
# ==========================================================
e = html.escape


def chips_html(items):
    return '<div class="chips">' + "".join(f'<span class="chip">{e(i)}</span>' for i in items) + "</div>"


def tasks_html(items):
    return "<ul>" + "".join(f"<li>{e(t)}</li>" for t in items) + "</ul>"


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

        org = (
            f'<div class="o">{e(x["org"])}</div>'
            if x.get("org") else ""
        )

        date = (
            f'<div class="date">{e(x["date"])}</div>'
            if x.get("date") else ""
        )

        body = ""

        if x.get("tasks"):
            body += f'<div class="mh">{e(d["h_tasks"])}</div>'
            body += tasks_html(x["tasks"])

        for g in x.get("groups", []):
            body += f'<div class="mh">{e(g["title"])}</div>'
            body += tasks_html(g["tasks"])

        if x.get("skills"):
            body += f'<div class="mh">{e(d["h_gained"])}</div>'
            body += chips_html(x["skills"])

        out.append(
            f'<details class="tl-item">'
            f'<summary>'
            f'<div class="r">{e(x["role"])}</div>'
            f'</summary>'
            f'<div class="more">'
            f'{org}'
            f'{date}'
            f'<div class="d">{e(x["desc"])}</div>'
            f'{body}'
            f'</div>'
            f'</details>'
        )

    return '<div class="tl">' + "".join(out) + '</div>'




def languages_html():
    langs = "".join(
        '<div class="lang">'
        f'<span class="lang-name">{e(k)}</span>'
        f'<span class="lang-level">{e(v)}</span>'
        "</div>"
        for k, v in d["languages"].items()
    )
    return (
        '<div class="two single">'
        f'<div class="card languages-list" dir="{d["dir"]}">{langs}</div>'
        "</div>"
    )


def section(heading, body):
    return f'<section class="sec"><h2>{e(heading)}</h2>{body}</section>'


# ==========================================================
#  الصفحة (ترتيب الأقسام: غيّر ترتيب الأسطر لتغيير الترتيب)
# ==========================================================



# ==========================================================
# الصفحة الرئيسية
# ==========================================================

# أزرار التواصل وتحميل السيرة الذاتية
# الصفحة الرئيسية

hero = (
    f'<div class="hero"><div class="open"><i></i>{e(d["tagline"])}</div>'
    f'<h1>{e(d["name"])}</h1><div class="role">{e(d["title"])}</div>'
    f'<p>{e(d["bio"])}</p></div>'
)

st.markdown(hero, unsafe_allow_html=True)

# أزرار التواصل وتحميل السيرة الذاتية
col_cv, col_linkedin = st.columns(2)

with col_cv:
    if CV_FILE.is_file():
        st.download_button(
            label="📄 تحميل السيرة الذاتية" if lang == "ar" else "📄 Download CV",
            data=CV_FILE.read_bytes(),
            file_name="Abdullah_Alqahtani_CV.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
    else:
        st.warning("ملف CV.pdf غير موجود")

with col_linkedin:
    st.link_button(
        label=d["cta"],
        url=LINKEDIN,
        use_container_width=True,
    )

# بقية أقسام الصفحة
page = (
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



