## School Event Manager

📌 Efficient Event and Task Management for Schools
Project Overview
School Event Manager is a web-based application designed to streamline school event organization, task management, and user collaboration. It allows administrators, teachers, students, and parents to plan events, track assignments, and enhance communication within the school community.

Key Features
✅ Event Creation – Schedule and manage school events (exams, meetings, sports activities). ✅ Task Management – Assign, track, and complete tasks linked to events. ✅ User Roles – Different access levels for students, parents, and teachers. ✅ Participant Tracking – Add participants to events and update their status (accepted/declined). ✅ Notifications – Automated alerts for upcoming events and task updates. How It Works?
1️⃣ User Authentication – Users register and log in to access the system. 2️⃣ Event Creation – Admins and teachers add events to the calendar. 3️⃣ Task Assignment – Users can create tasks and link them to events. 4️⃣ Progress Monitoring – The system updates event and task statuses for tracking. 5️⃣ Interaction & Feedback – Users can comment on events.

Technologies Used
🐍 Backend: Django

🎨 Frontend: HTML, CSS, Bootstrap

📅 Database: SQLite / PostgreSQL

⚡ Additional: Django Auth, Ajax, JSON

Installation & Setup
```
git clone https://github.com/yourusername/school-event-manager.git
cd school-event-manager
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Then, open http://127.0.0.1:8000/ in your browser.
```