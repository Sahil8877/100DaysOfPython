import data

def parse_jobs(querystring):
    fetch_jobs = data.get_jobs(querystring)
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
    # print(cleaned_job_list)
    return cleaned_job_list


