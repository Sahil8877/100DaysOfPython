import data

def parse_dev_jobs():
    fetch_jobs = data.get_dev_jobs()
    cleaned_job_list = []
    if fetch_jobs:
        for job in fetch_jobs['data']:
            cleaned_job_list.append({
               "Job Title" : job['job_title'],
               "Company" : job['employer_name'],
               "Type" : job['job_employment_type'],
               "Location" : job['job_location'],
               "Apply Link" : job['job_apply_link'],
               "Job Description" : str(job['job_description']).replace("\n",""),
            })
    print(cleaned_job_list)

parse_dev_jobs()