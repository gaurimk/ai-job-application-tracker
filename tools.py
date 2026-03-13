import sqlite3

DB_NAME = "jobs.db"


def add_job_application(company, role, status, date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO applications (company, role, status, date) VALUES (?, ?, ?, ?)",
        (company, role, status, date),
    )

    conn.commit()
    conn.close()

    return {"message": "Job application added successfully"}


def list_applications():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM applications")
    jobs = cursor.fetchall()

    conn.close()

    return jobs


def update_status(job_id, new_status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE applications SET status=? WHERE id=?",
        (new_status, job_id),
    )

    conn.commit()
    conn.close()

    return {"message": "Application status updated"}


def summarize_applications():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT status, COUNT(*) FROM applications GROUP BY status"
    )

    summary = cursor.fetchall()

    conn.close()

    return summary

def delete_application(job_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM applications WHERE id=?",
        (job_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Application deleted"}