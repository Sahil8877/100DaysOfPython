import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

url = "https://jsearch.p.rapidapi.com/search"

headers = {
	"x-rapidapi-key": os.getenv("RAPID_API_KEY"),
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

def get_dev_jobs():

    querystring = {"query":"python developer jobs in uk","page":"1","num_pages":"1","country":"uk","date_posted":"all","employment_types":"FULLTIME,INTERN","job_requirements":"under_3_years_experience"}

    # response = requests.get(url, headers=headers, params=querystring)
    # print(response.status_code)

    # json_data = response.json()
    # json_formatted = json.dumps(json_data,indent=4)

    data = {
    "status": "OK",
    "request_id": "ec30003e-4216-472d-ac49-8632a1bbc263",
    "parameters": {
        "query": "python developer jobs in uk",
        "page": 1,
        "num_pages": 1,
        "date_posted": "all",
        "employment_types": [
        "INTERN",
        "FULLTIME"
        ],
        "job_requirements": [
        "under_3_years_experience"
        ],
        "country": "uk",
        "language": "en"
    },
    "data": [
        {
        "job_id": "Qyb3ZycYqXW9S60iAAAAAA==",
        "job_title": "Software Engineer | React & Python (full stack)",
        "employer_name": "Senzo",
        "employer_logo": "null",
        "employer_website": "https://www.senzo.com",
        "job_publisher": "LinkedIn",
        "job_employment_type": "Full–time",
        "job_employment_types": [
            "FULLTIME"
        ],
        "job_apply_link": "https://uk.linkedin.com/jobs/view/software-engineer-react-python-full-stack-at-senzo-4371896633?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
        "job_apply_is_direct": False,
        "apply_options": [
            {
            "publisher": "LinkedIn",
            "apply_link": "https://uk.linkedin.com/jobs/view/software-engineer-react-python-full-stack-at-senzo-4371896633?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Talents By StudySmarter",
            "apply_link": "https://talents.studysmarter.co.uk/companies/law-school-admission-council/software-engineer-full-stack-green-team-6888557/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            }
        ],
        "job_description": "Software Engineer | React / Python | Real-time Data Intelligence Platform\n\nFull stack (flexible on split)\n\nLocation: Hybrid (London, Oxford or Cambridge)\n\nWe’re working with an early stage technology company building a production grade data platform for real time systems and analytics at scale. While the business has roots in autonomous systems, the core value sits firmly in the software platform that turns live data into usable insight.\n\nAs customer adoption grows, the team is expanding its product engineering capability and hiring Software Engineers to help build and evolve customer facing features on top of the core platform.\n\nThis is a role for full stack Software Engineer who enjoy working across the stack in early stage environments. You will be building real features used by customers, helping shape how new capabilities are developed, and feeding improvements back into the central platform as the product matures.\n\nThe business is well funded, gaining strong client traction, and building toward a significant scale up phase over the next 12 to 24 months.\n\nWhat you’ll get\n\n• Hands on ownership of end to end product features used by real customers\n\n• Exposure to a data intensive, real time platform\n\n• The chance to shape how new features are built and integrated into the core system\n\n• Close collaboration with architecture, cloud, and platform teams\n\n• A high ownership engineering environment with room to grow\n\nWhat you’ll be doing\n\n• Building full stack features across React front end and Python backend services\n\n• Developing customer focused functionality on top of a shared data platform\n\n• Working with AWS infrastructure to deploy and support new capabilities\n\n• Collaborating with platform engineers to fold successful features back into the core product\n\n• Contributing to code structure, patterns, and engineering standards as the system evolves\n\n• Supporting debugging, performance improvements, and production reliability\n\n• Working in small teams where engineers own features from design through delivery\n\nThis is not a narrowly siloed role. You will work across front end, backend, and cloud, with flexibility to lean into your strengths while developing breadth across the stack.\n\nWhat we’re looking for\n\n• 5+ years working as a Software Engineer building production ready systems\n\n• Strong fundamentals in either React front end or Python backend (ideally both), with working ability across both\n\n• Practical experience deploying and supporting applications in AWS\n\n• Comfort working in early stage environments with ambiguity and high ownership\n\n• A production first mindset focused on reliability, clarity, and maintainability\n\nEngineers may lean slightly frontend or backend, but should be comfortable operating across the stack and collaborating closely with other specialists. The company plans to hire 2-3 so would look to balance the indvidual leaning across the hires.\n\nNice to haves\n\n• Experience building customer facing SaaS platforms\n\n• Exposure to data heavy or real time systems\n\n• Familiarity with modern frontend patterns and API driven architectures\n\nInterested?\n\nIf you’re looking for a Software Engineer role with real ownership and long term impact, I’d be happy to share more context.\n\nSalary: £60,000 to £70,000 plus benefits\n\nImportant:\n\nNo sponsorship available\n\nApplicants must already be in the UK to apply",
        "job_is_remote": False,
        "job_posted_at": "15 hours ago",
        "job_posted_at_timestamp": 1771142400,
        "job_posted_at_datetime_utc": "2026-02-15T08:00:00.000Z",
        "job_location": "United Kingdom",
        "job_city": "null",
        "job_state": "null",
        "job_country": "GB",
        "job_latitude": 55.378051,
        "job_longitude": -3.4359729999999997,
        "job_benefits": "null",
        "job_google_link": "https://www.google.com/search?q=jobs&gl=uk&hl=en&udm=8#vhid=vt%3D20/docid%3DQyb3ZycYqXW9S60iAAAAAA%3D%3D&vssid=jobs-detail-viewer",
        "job_min_salary": "null",
        "job_max_salary": "null",
        "job_salary_period": "YEAR",
        "job_highlights": {},
        "job_onet_soc": "15113300",
        "job_onet_job_zone": "4"
        },
        {
        "job_id": "AkHDqxokwhpBVi_HAAAAAA==",
        "job_title": "Junior Python Developer Computer Science",
        "employer_name": "Client Server",
        "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSIBNsvJ7DsrIOE0Kx2aDinpZk_jhuGx1B9l4C&s=0",
        "employer_website": "https://www.client-server.com",
        "job_publisher": "Totaljobs",
        "job_employment_type": "Full–time",
        "job_employment_types": [
            "FULLTIME"
        ],
        "job_apply_link": "https://www.totaljobs.com/job/junior-python-developer-computer-science/client-server-job106719880?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
        "job_apply_is_direct": True,
        "apply_options": [
            {
            "publisher": "Totaljobs",
            "apply_link": "https://www.totaljobs.com/job/junior-python-developer-computer-science/client-server-job106719880?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": True
            },
            {
            "publisher": "BeBee GB",
            "apply_link": "https://gb.bebee.com/job/4d4ad8f92c019b9ff33d7771c82a9b48?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Talents By StudySmarter",
            "apply_link": "https://talents.studysmarter.co.uk/companies/lorien/junior-python-developer-fintech-platform-with-mentorship-19861845/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            }
        ],
        "job_description": "Junior Python Developer / Engineer (Computer Science) London / WFH to £65k\n\nDo you have a first class Computer Science education combined with backend Python coding skills?\n\nYou could be progressing your career at a successful and growing technology company that have recently received £30 million of series B funding.\n\nThe core product allows business users to capture data via integrated mobile services utilising video analytics and speech recognition to analyse and categorise information within the workflows of large field workforces (field engineers, field service, auditing, reporting, health-and-safety, sales, etc.); customers are typically large multinationals: utilities, telecoms, manufacturing and facilities management companies.\n\nAs a Junior Python Developer you'll design and develop new features and enhancements to the core platform and APIs working with Python within an AWS environment. You'll work across the full software development lifecycle to design robust, scalable, performant and secure implementations for new features.\n\nYou'll be continually learning and enhancing your skills as part of a highly talented remote team.\n\nLocation / WFH:\n\nYou can work from home / remotely form anywhere in the UK.\n\nAbout you:\n• You are degree educated in Computer Science, having achieved a 2.1 or above from a top tier university (e.g. Russel Group)\n• You have commercial backend Python development experience\n• You have a good knowledge of databases, PostgreSQL preferred\n• You have a good understanding of Web API architecture e.g. REST APIs and messaging systems\n• You are familiar with SaaS, big data and analytics, machine learning, computer vision and AI algorithms\n• You're a collaborative problem solver with great communication skills\n• Experience with video and audio processing or video streaming would be great but not essential\n\nWhat's in it for you:\n• Salary to £65k\n• Remote working plus flexible, family friendly working hours\n• Stock ownership plan\n• Private Healthcare\n• Pension\n\nApply now to find out more about this Junior Python Developer / Engineer (Computer Science) opportunity.\n\nAt Client Server we believe in a diverse workplace that allows people to play to their strengths and continually learn. We're an equal opportunities employer whose people come from all walks of life and will never discriminate based on race, colour, religion, sex, gender identity or expression, sexual orientation, national origin, genetics, disability, age, or veteran status. The clients we work with share our values.",
        "job_is_remote": True,
        "job_posted_at": "4 days ago",
        "job_posted_at_timestamp": 1770768000,
        "job_posted_at_datetime_utc": "2026-02-11T00:00:00.000Z",
        "job_location": "London",
        "job_city": "London",
        "job_state": "null",
        "job_country": "GB",
        "job_latitude": 51.5072178,
        "job_longitude": -0.12758619999999998,
        "job_benefits": "null",
        "job_google_link": "https://www.google.com/search?q=jobs&gl=uk&hl=en&udm=8#vhid=vt%3D20/docid%3DAkHDqxokwhpBVi_HAAAAAA%3D%3D&vssid=jobs-detail-viewer",
        "job_salary": "null",
        "job_min_salary": "null",
        "job_max_salary": "null",
        "job_salary_period": "null",
        "job_highlights": {},
        "job_onet_soc": "15113200",
        "job_onet_job_zone": "4"
        },
        {
        "job_id": "dRqF-NfWjppstsVIAAAAAA==",
        "job_title": "Junior Python Developer",
        "employer_name": "Lorien",
        "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQ02yUGnkuH2qc_AjTKlqHvDRoKkWDpbnBzr7c&s=0",
        "employer_website": "https://www.lorienglobal.com",
        "job_publisher": "Talents By StudySmarter",
        "job_employment_type": "Full–time",
        "job_employment_types": [
            "FULLTIME"
        ],
        "job_apply_link": "https://talents.studysmarter.co.uk/companies/lorien/basildon/junior-python-developer-22230598/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
        "job_apply_is_direct": False,
        "apply_options": [
            {
            "publisher": "Talents By StudySmarter",
            "apply_link": "https://talents.studysmarter.co.uk/companies/lorien/basildon/junior-python-developer-22230598/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            }
        ],
        "job_description": "Junior Python Developer (FinTech, FX Trading) — London Hybrid\n\nEmployment: Permanent, Full‑time\n\nLocation: Bank, London — 3 days on‑site (Tue/Wed/Thu) + 2 days WFH\n\nSalary: £40,000 + training & benefits\n\nAbout:\n\nA startup fintech building a next‑generation FX trading & settlement platform—connecting onboarding, dealing, risk, settlement, reporting and client portals into one system. This is an awesome opportunity to help build an FX Trading platform from the ground up.\n\nThe Opportunity:\n\nYou’ll create, build and deploy using Infrastructure‑as‑Code (IaC) while working across the full stack. Expect extensive training and hands‑on exposure to Azure and Salesforce, plus mentorship from experienced engineers.\n\nWhat you’ll do:\n• Develop and optimise platform components in Python\n• Write and tune SQL Server queries, views & stored procedures\n• Build REST APIs for internal/external integrations\n• Learn and contribute to event‑driven pipelines (e.g., Kafka/RabbitMQ)\n• Apply IaC and contribute to CI/CD releases\n• Collaborate with Product, Operations & Compliance on mission‑critical features\n\nWhat you’ll bring:\n• 1–2 years’ commercial experience with Python and SQL (or strong projects/internships)\n• Understanding of APIs, data modelling and secure access controls\n• Curiosity, problem‑solving mindset, and clear communication\n• Nice to have: Kafka or message queues, Azure, Salesforce (Apex/Flows), Docker, Azure DevOps/GitHub Actions\n• GitHub/portfolio link welcome (not mandatory)\n\nWhy join:\n• Build high‑impact fintech systems that move money & markets\n• Modern stack (Python, Kafka, SQL Server, REST, Azure, Salesforce)\n• Professional training & certification support\n• Clear growth path as the platform scales globally\n\nEligibility:\n• Right to work in the UK (sponsorship not available)\n• Commutable to London for 3 on‑site days (Tue/Wed/Thu)\n• Permanent only (no contractors)\n\nApply now:\n\nSend your CV (and GitHub if available) with the subject line: Junior Python Developer – Fiscal FX.",
        "job_is_remote": False,
        "job_posted_at": "null",
        "job_posted_at_timestamp": "null",
        "job_posted_at_datetime_utc": "null",
        "job_location": "Basildon",
        "job_city": "Basildon",
        "job_state": "null",
        "job_country": "GB",
        "job_latitude": 51.576083999999994,
        "job_longitude": 0.488736,
        "job_benefits": "null",
        "job_google_link": "https://www.google.com/search?q=jobs&gl=uk&hl=en&udm=8#vhid=vt%3D20/docid%3DdRqF-NfWjppstsVIAAAAAA%3D%3D&vssid=jobs-detail-viewer",
        "job_salary": "null",
        "job_min_salary": "null",
        "job_max_salary": "null",
        "job_salary_period": "null",
        "job_highlights": {},
        "job_onet_soc": "15113200",
        "job_onet_job_zone": "4"
        },
        {
        "job_id": "9UMlSvzOIVwTgFCyAAAAAA==",
        "job_title": "Software Engineer (Go/ Python/ AWS) - Scale Up Tech Company - £90k",
        "employer_name": "La Fosse",
        "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfzooJ8CfW0-Kg7jLiDa8Ix-ho_3HkUHFNyMkE&s=0",
        "employer_website": "https://www.lafosse.com",
        "job_publisher": "LinkedIn",
        "job_employment_type": "Full–time",
        "job_employment_types": [
            "FULLTIME"
        ],
        "job_apply_link": "https://uk.linkedin.com/jobs/view/software-engineer-go-python-aws-scale-up-tech-company-%C2%A390k-at-la-fosse-4371739817?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
        "job_apply_is_direct": False,
        "apply_options": [
            {
            "publisher": "LinkedIn",
            "apply_link": "https://uk.linkedin.com/jobs/view/software-engineer-go-python-aws-scale-up-tech-company-%C2%A390k-at-la-fosse-4371739817?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            }
        ],
        "job_description": "London • £90k • Start‑Up Culture • Greenfield • Product‑Led Tech Company\n\nI am recruiting for a fast‑growing tech scale‑up that’s transforming how hospitality and retail businesses manage flexible staffing. They are a proper product‑driven technology company building a platform that connects businesses with high‑quality staff.\n\nYou’ll be joining one of three cross‑functional engineering squads, each owning its own roadmap and delivering new greenfield features across mobile, backend services, and internal tools. It’s a place where engineers have real influence, ship fast, and work closely with product and design to solve meaningful operational challenges at scale.\n\nThe Stack:\n• Go - Microservices\n• Python - Monolith\n• AWS\n\nYou’ll fit well if you enjoy:\n• Working in a collaborative squad alongside product, design, and data.\n• Solving complex problems with simple, elegant solutions.\n• Building high‑quality software in a high‑trust engineering culture.\n• Contributing to greenfield product development in a company that values autonomy, ownership, and velocity.\n• £90k salary\n• On‑site in London with a tight‑knit, high‑energy team\n• Start‑up culture with genuine ownership\n• Opportunity to work across mobile, backend, and platform\n• Build meaningful, impactful features used in the real world every day\n• Join a tech organisation that actually behaves like one — engineering‑led, product‑focused, and innovation‑driven",
        "job_is_remote": False,
        "job_posted_at": "3 days ago",
        "job_posted_at_timestamp": 1770854400,
        "job_posted_at_datetime_utc": "2026-02-12T00:00:00.000Z",
        "job_location": "United Kingdom",
        "job_city": "null",
        "job_state": "null",
        "job_country": "GB",
        "job_latitude": 55.378051,
        "job_longitude": -3.4359729999999997,
        "job_benefits": "null",
        "job_google_link": "https://www.google.com/search?q=jobs&gl=uk&hl=en&udm=8#vhid=vt%3D20/docid%3D9UMlSvzOIVwTgFCyAAAAAA%3D%3D&vssid=jobs-detail-viewer",
        "job_min_salary": "null",
        "job_max_salary": "null",
        "job_salary_period": "YEAR",
        "job_highlights": {},
        "job_onet_soc": "15113200",
        "job_onet_job_zone": "4"
        },
        {
        "job_id": "JbgpJ_CjjVjSpq8dAAAAAA==",
        "job_title": "Junior AWS/Python Developer – Flexible Cloud Growth",
        "employer_name": "University of Sheffield",
        "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs2Ub6ue1hAjBS7q2TxIUrIt3x6hhayhowogxE&s=0",
        "employer_website": "https://sheffield.ac.uk",
        "job_publisher": "Talents By StudySmarter",
        "job_employment_type": "Full–time",
        "job_employment_types": [
            "FULLTIME"
        ],
        "job_apply_link": "https://talents.studysmarter.co.uk/companies/university-of-sheffield/sheffield/junior-aws-python-developer-flexible-cloud-growth-24799575/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
        "job_apply_is_direct": False,
        "apply_options": [
            {
            "publisher": "Talents By StudySmarter",
            "apply_link": "https://talents.studysmarter.co.uk/companies/university-of-sheffield/sheffield/junior-aws-python-developer-flexible-cloud-growth-24799575/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            }
        ],
        "job_description": "A leading educational institution in the UK is seeking a Junior AWS/Python Developer to join their Enterprise Systems team. This role involves developing applications and maintaining systems that support student services, while working in a modern cloud environment. The position offers the chance to grow skills in AWS, automation, and software best practices while contributing to meaningful projects for a vibrant university community.\n#J-18808-Ljbffr",
        "job_is_remote": False,
        "job_posted_at": "18 days ago",
        "job_posted_at_timestamp": 1769558400,
        "job_posted_at_datetime_utc": "2026-01-28T00:00:00.000Z",
        "job_location": "Sheffield",
        "job_city": "null",
        "job_state": "null",
        "job_country": "GB",
        "job_latitude": 53.381128999999994,
        "job_longitude": -1.4700849999999999,
        "job_benefits": "null",
        "job_google_link": "https://www.google.com/search?q=jobs&gl=uk&hl=en&udm=8#vhid=vt%3D20/docid%3DJbgpJ_CjjVjSpq8dAAAAAA%3D%3D&vssid=jobs-detail-viewer",
        "job_salary": "null",
        "job_min_salary": "null",
        "job_max_salary": "null",
        "job_salary_period": "null",
        "job_highlights": {},
        "job_onet_soc": "15113200",
        "job_onet_job_zone": "4"
        },
        {
        "job_id": "owKYseAcc8nMwO-WAAAAAA==",
        "job_title": "Junior Python Developer 🏆",
        "employer_name": "Information Tech Consultants",
        "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRl5gjNxP6p3_2T0FdhOZWzKR3ERDYPJZAzs0kE&s=0",
        "employer_website": "https://www.informationtechconsultants.co.uk",
        "job_publisher": "DevITJobs.uk",
        "job_employment_type": "Full–time",
        "job_employment_types": [
            "FULLTIME"
        ],
        "job_apply_link": "https://devitjobs.uk/jobs/Information-Tech-Consultants-Junior-Python-Developer?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
        "job_apply_is_direct": False,
        "apply_options": [
            {
            "publisher": "DevITJobs.uk",
            "apply_link": "https://devitjobs.uk/jobs/Information-Tech-Consultants-Junior-Python-Developer?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Talents By StudySmarter",
            "apply_link": "https://talents.studysmarter.co.uk/companies/durlston-partners/junior-python-data-developer-6125714/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "BeBee GB",
            "apply_link": "https://gb.bebee.com/job/7aa30db6aaa6cfbfd99cf4a90cfd507f?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Jobijoba UK",
            "apply_link": "https://www.jobijoba.co.uk/detail/92/8bd38dc65ec0f84f9b3312c0957a477d?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "ClimateTechList",
            "apply_link": "https://www.climatetechlist.com/job/carbonchain-junior-python-developer-iVXdyttI0IVKT2?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Palpable Jobs",
            "apply_link": "https://www.bepalpable.com/entry-level-jobs/junior-python-developer-v4hxn?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Jobilize",
            "apply_link": "https://www.jobilize.com/job/gb-london-junior-python-developer-clearroute-hiring-now-job-immediately?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            }
        ],
        "job_description": "Junior Python Developer 💰 Salary: £35,000 - 45,000 per year\n\nAt Information Tech Consultants we are looking for a Python engineer!\n\n🛠️ Our tech stack:\nAI, AWS, Azure, Cloud, GCP, Git, Support, Jupyter, Machine Learning, PyTorch, Python, SQL, TensorFlow, numpy, pandas\n\n📝 Rquirements:\n- Masters degree in Computer Science, Data Science, Statistics, Mathematics, or a related field\n- Strong proficiency in Python and key data science libraries (NumPy, pandas, scikit-learn, Matplotlib, Seaborn)\n- Basic understanding of supervised and unsupervised learning algorithms (e.g., regression, classification, clustering)\n- Knowledge of data querying and manipulation using SQL\n- Familiarity with Jupyter Notebooks, Git, and version control workflows\n- Strong analytical thinking and problem-solving skills\n- Eagerness to learn, collaborate, and apply new technologies in real-world projects\n- Experience with deep learning frameworks such as TensorFlow or PyTorch (preferred)\n- Exposure to cloud platforms (AWS, GCP, or Azure) (preferred)\n- Understanding of model evaluation and deployment best practices (preferred)\n- Internship or project experience in machine learning, data analytics, or AI applications (preferred)\n\n👩‍💻👨‍💻 Your responsibilities are:\n- Support the design, development, and testing of machine learning models and data analytics solutions\n- Perform data cleaning, preprocessing, and transformation using Python libraries such as pandas and NumPy\n- Conduct exploratory data analysis (EDA) to identify trends, patterns, and correlations\n- Assist in feature selection and engineering to improve model performance\n- Evaluate model performance using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC\n- Help build and maintain automated data pipelines and model deployment scripts\n- Collaborate with data engineers and senior data scientists to integrate models into production\n- Create clear and concise data visualizations and communicate insights to technical and non-technical stakeholders\n\nView this job and over 500 other transparent jobs with salaries (💰💰💰) & tech stacks (🛠️) on DevITJobs.uk\n\nCategory: Python Developer / Engineer\nLocation address: Chalk Farm Road 49, London, United Kingdom\n\nSalary: £35,000 - 45,000 per year\n\nBenefits & perks that we offer:\n\nInformation Tech Consultants - More about us and the role:\nWe are looking for a motivated and detail-oriented Junior Data Scientist with a strong foundation in Machine Learning and Python programming to join our Data Science team in London. In this role, you will assist in developing and deploying data-driven solutions that help shape business strategy and improve decision-making. We offer mentorship from experienced data scientists, opportunities to work on impactful real-world ML projects, access to cutting-edge tools and training resources, a competitive salary, and a supportive environment that encourages continuous learning and experimentation.\n\nAre you looking for Python jobs in London?",
        "job_is_remote": False,
        "job_posted_at": "19 days ago",
        "job_posted_at_timestamp": 1769472000,
        "job_posted_at_datetime_utc": "2026-01-27T00:00:00.000Z",
        "job_location": "London",
        "job_city": "London",
        "job_state": "null",
        "job_country": "GB",
        "job_latitude": 51.5072178,
        "job_longitude": -0.12758619999999998,
        "job_benefits": "null",
        "job_google_link": "https://www.google.com/search?q=jobs&gl=uk&hl=en&udm=8#vhid=vt%3D20/docid%3DowKYseAcc8nMwO-WAAAAAA%3D%3D&vssid=jobs-detail-viewer",
        "job_min_salary": "null",
        "job_max_salary": "null",
        "job_salary_period": "YEAR",
        "job_highlights": {},
        "job_onet_soc": "15113200",
        "job_onet_job_zone": "4"
        },
        {
        "job_id": "yAZrfgmYcf7QZO_vAAAAAA==",
        "job_title": "Junior Python Developer",
        "employer_name": "Lloyds",
        "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS55E4-2jZc_Up8OlAe6AkaQk02aq3Tz0OsldF4&s=0",
        "employer_website": "https://www.lloyds.com",
        "job_publisher": "Welcome To The Jungle | Login",
        "job_employment_type": "Full–time",
        "job_employment_types": [
            "FULLTIME"
        ],
        "job_apply_link": "https://app.welcometothejungle.com/jobs/Ao6OOnRj?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
        "job_apply_is_direct": False,
        "apply_options": [
            {
            "publisher": "Welcome To The Jungle | Login",
            "apply_link": "https://app.welcometothejungle.com/jobs/Ao6OOnRj?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Learn4Good",
            "apply_link": "https://www.learn4good.com/jobs/cardiff/uk/software_development/4819705804/e/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Expertini",
            "apply_link": "https://cardiff.uk.expertini.com/job/junior-python-developer-cardiff-lloyds-banking-group-766-14717752/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "LifeworQ",
            "apply_link": "https://lifeworq.com/job/89d6e281-896b-47a9-b79b-ab1443a488d5?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            }
        ],
        "job_description": "Requirements\n• Experience of Python model development and implementation,\n• A basic understanding of core software development principles,\n• An interest in working with data and/or financial models,\n• Familiarity with common Python tooling and best practices, including:,\n• Virtual environments,\n• Package management (e.g. uv, pip, poetry),\n• Source control (e.g., Git/GitHub) for collaborative development,\n• CI/CD pipelines for automated testing and deployment,\n• Testing frameworks (e.g. pytest, unittest),\n• Code quality (e.g. flake8, black, isort, mypy, ruff),\n• Documentation tools (e.g., MkDocs, Sphinx) for maintainable technical documentation,\n• Good communication and presentation skills,\n• Passion for learning and staying ahead of the curve, and an ambition to become an experienced Python developer,\n• And any experience of these would be really useful,\n• Experience or interest in business analysis,\n• Exposure to front-end technologies e.g. React,\n• Curiosity about data processing and validation libraries (Polars, Pandera), numerical computing (NumPy, Numba), and API frameworks (FastAPI)\n\nWhat the job involves\n• HOURS: Full Time, 35 hours per week,\n• Are you passionate about learning Python development and keen to build your skills in automation and financial modelling? Do you want to contribute to meaningful change in Retail Finance? If so, we’d love to hear from you!,\n• We’re looking for a Junior Python Developer to join our Retail Finance Change team and support the delivery of innovative financial solutions. You’ll bring curiosity, a willingness to learn, and a collaborative mindset as we work on a strategic backlog of development and optimisation,\n• Support the design, build, UAT and ongoing maintenance of Python-based financial models and automation tools,\n• Work closely with experienced developers, Business Analysts, and domain experts to translate business needs into technical solutions,\n• Contribute to developing efficient, maintainable code for financial models and automation tasks,\n• Support the creation of user-friendly interfaces for model execution and reporting,\n• Help ensure code quality through unit, integration, and system tests,\n• Participate in design forums and peer code reviews,\n• Collaborate in agile delivery, including planning, backlog refinement, demos and retros, and helping prioritise work that drives measurable business value,\n• Demonstrate a proactive commitment to continuous learning and professional growth, seeking opportunities to expand your technical expertise and contribute to team success",
        "job_is_remote": False,
        "job_posted_at": "20 days ago",
        "job_posted_at_timestamp": 1769385600,
        "job_posted_at_datetime_utc": "2026-01-26T00:00:00.000Z",
        "job_location": "United Kingdom",
        "job_city": "null",
        "job_state": "null",
        "job_country": "GB",
        "job_latitude": 55.378051,
        "job_longitude": -3.4359729999999997,
        "job_benefits": "null",
        "job_google_link": "https://www.google.com/search?q=jobs&gl=uk&hl=en&udm=8#vhid=vt%3D20/docid%3DyAZrfgmYcf7QZO_vAAAAAA%3D%3D&vssid=jobs-detail-viewer",
        "job_salary": "null",
        "job_min_salary": "null",
        "job_max_salary": "null",
        "job_salary_period": "null",
        "job_highlights": {},
        "job_onet_soc": "15113200",
        "job_onet_job_zone": "4"
        },
        {
        "job_id": "lxfTBen95HChGayIAAAAAA==",
        "job_title": "Junior Python Developer – FastAPI Backend & APIs",
        "employer_name": "Knowledge Bank",
        "employer_logo": "null",
        "employer_website": "https://www.knowledge-bank.net",
        "job_publisher": "Talents By StudySmarter",
        "job_employment_type": "Full–time",
        "job_employment_types": [
            "FULLTIME"
        ],
        "job_apply_link": "https://talents.studysmarter.co.uk/companies/knowledge-bank/barnsley/junior-python-developer-fastapi-backend-apis-19865260/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
        "job_apply_is_direct": False,
        "apply_options": [
            {
            "publisher": "Talents By StudySmarter",
            "apply_link": "https://talents.studysmarter.co.uk/companies/knowledge-bank/barnsley/junior-python-developer-fastapi-backend-apis-19865260/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            }
        ],
        "job_description": "A UK fintech company is seeking a Junior Python Developer to join their award-winning team. You will be tasked with building, migrating, and maintaining backend services in Python, specifically utilizing FastAPI. This role involves contributing to software and product design, including the development of web apps and APIs. If you are passionate about clean, user-focused engineering and enjoy solving real problems, this could be your next career move. #J-18808-Ljbffr",
        "job_is_remote": False,
        "job_posted_at": "null",
        "job_posted_at_timestamp": "null",
        "job_posted_at_datetime_utc": "null",
        "job_location": "Barnsley",
        "job_city": "Barnsley",
        "job_state": "null",
        "job_country": "GB",
        "job_latitude": 53.55263,
        "job_longitude": -1.4797259999999999,
        "job_benefits": "null",
        "job_google_link": "https://www.google.com/search?q=jobs&gl=uk&hl=en&udm=8#vhid=vt%3D20/docid%3DlxfTBen95HChGayIAAAAAA%3D%3D&vssid=jobs-detail-viewer",
        "job_min_salary": "null",
        "job_max_salary": "null",
        "job_salary_period": "YEAR",
        "job_highlights": {},
        "job_onet_soc": "15113200",
        "job_onet_job_zone": "4"
        },
        {
        "job_id": "PElUZNtZA1ZG7UkEAAAAAA==",
        "job_title": "Sr. Python Developer",
        "employer_name": "Ascendion",
        "employer_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmH6BHc4fe-fG4vytfqWcRBvZ7Q7tEI84xg95j&s=0",
        "employer_website": "https://ascendion.com",
        "job_publisher": "LinkedIn",
        "job_employment_type": "Full–time",
        "job_employment_types": [
            "FULLTIME"
        ],
        "job_apply_link": "https://uk.linkedin.com/jobs/view/sr-python-developer-at-ascendion-4371052150?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
        "job_apply_is_direct": False,
        "apply_options": [
            {
            "publisher": "LinkedIn",
            "apply_link": "https://uk.linkedin.com/jobs/view/sr-python-developer-at-ascendion-4371052150?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Adzuna",
            "apply_link": "https://www.adzuna.co.uk/jobs/details/5627955038?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Talents By StudySmarter",
            "apply_link": "https://talents.studysmarter.co.uk/companies/ascendion/sr-python-developer-18279647/?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "BeBee GB",
            "apply_link": "https://gb.bebee.com/job/5070211bbd8b1938e437dfa4e6f8cb22?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Jobilize",
            "apply_link": "https://www.jobilize.com/job/gb-london-area-sr-python-developer-stockley-park-ascendion-hiring?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            },
            {
            "publisher": "Recruit.net",
            "apply_link": "https://www.recruit.net/job/sr-python-developer-jobs/216B2D1575852565?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            }
        ],
        "job_description": "We are looking for Sr. Python developer for our Banking partner in Bromley, UK !\n\nFull-time role with Ascendion (AI-first, 30% YoY growth, FS focused)\n\n3 days onsite role in Bromley\n\nThis role is suited to a Senior Software Engineer with experience building enterprise‑wide applications in a front‑office financial services domain.\n• Design and implement backend Python software solutions within the SP pre-trade domain.\n• Collaborate on React UI app, ensuring clean API contracts and integration with backend services.\n• Define, evolve, and maintain structured products data models defined as JSON schemas.\n• Contribute to system design and architecture decisions for a globally distributed FO platform.\n• Knowledge of Structured Products (Notes, Warrants, Certificates)\n\nDesirable Skills:\n• Familiarity with financial services, particularly structured notes and equity derivatives.\n• Knowledge of front-office sales and trading workflows.\n• Familiarity with messaging or event-driven systems.\n• Experience mentoring junior engineers or leading technical initiatives.\n• Linux command line experience.",
        "job_is_remote": False,
        "job_posted_at": "5 days ago",
        "job_posted_at_timestamp": 1770681600,
        "job_posted_at_datetime_utc": "2026-02-10T00:00:00.000Z",
        "job_location": "United Kingdom",
        "job_city": "null",
        "job_state": "null",
        "job_country": "GB",
        "job_latitude": 55.378051,
        "job_longitude": -3.4359729999999997,
        "job_benefits": "null",
        "job_google_link": "https://www.google.com/search?q=jobs&gl=uk&hl=en&udm=8#vhid=vt%3D20/docid%3DPElUZNtZA1ZG7UkEAAAAAA%3D%3D&vssid=jobs-detail-viewer",
        "job_salary": "null",
        "job_min_salary": "null",
        "job_max_salary": "null",
        "job_salary_period": "null",
        "job_highlights": {},
        "job_onet_soc": "15113200",
        "job_onet_job_zone": "4"
        },
        {
        "job_id": "pjh19ipOqCWEb4FaAAAAAA==",
        "job_title": "Junior Software Developers Java, C#, Python - London in London - Vantage Point",
        "employer_name": "Vantage Point",
        "employer_logo": "null",
        "employer_website": "https://vantagepoint.io",
        "job_publisher": "Java Works - WorksHub",
        "job_employment_type": "Full–time",
        "job_employment_types": [
            "FULLTIME"
        ],
        "job_apply_link": "https://java.works-hub.com/jobs/junior-software-developers-java-c-number-python-london-7ac?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
        "job_apply_is_direct": False,
        "apply_options": [
            {
            "publisher": "Java Works - WorksHub",
            "apply_link": "https://java.works-hub.com/jobs/junior-software-developers-java-c-number-python-london-7ac?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic",
            "is_direct": False
            }
        ],
        "job_description": "We are recruiting for a wide range of entry-level and experienced roles in technology, such as:\n\nSoftware Developers (Java, C#, Python): Write and maintain code for innovative applications and systems.\n\nWhat will you be learning?\n\nAs part of your journey...",
        "job_is_remote": False,
        "job_posted_at": "null",
        "job_posted_at_timestamp": "null",
        "job_posted_at_datetime_utc": "null",
        "job_location": "London",
        "job_city": "London",
        "job_state": "null",
        "job_country": "GB",
        "job_latitude": 51.5072178,
        "job_longitude": -0.12758619999999998,
        "job_benefits": "null",
        "job_google_link": "https://www.google.com/search?q=jobs&gl=uk&hl=en&udm=8#vhid=vt%3D20/docid%3Dpjh19ipOqCWEb4FaAAAAAA%3D%3D&vssid=jobs-detail-viewer",
        "job_salary": "null",
        "job_min_salary": "null",
        "job_max_salary": "null",
        "job_salary_period": "null",
        "job_highlights": {},
        "job_onet_soc": "15113200",
        "job_onet_job_zone": "4"
        }
    ]
    }
    # json_data = json.dumps(json_formatted)
    # print(json_formatted)
    return data

# get_dev_jobs()