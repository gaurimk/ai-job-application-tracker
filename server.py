from fastmcp import FastMCP
from tools import (
    add_job_application,
    list_applications,
    update_status,
    summarize_applications,
    delete_application
)

mcp = FastMCP("AI Job Application Tracker")


@mcp.tool()
def add_application(company: str, role: str, status: str, date: str):
    """Add a new job application"""
    return add_job_application(company, role, status, date)


@mcp.tool()
def get_applications():
    """List all job applications"""
    return list_applications()


@mcp.tool()
def change_status(job_id: int, new_status: str):
    """Update application status"""
    return update_status(job_id, new_status)


@mcp.tool()
def application_summary():
    """Summarize job application statuses"""
    return summarize_applications()


@mcp.tool()
def remove_application(job_id: int):
    """Delete a job application"""
    return delete_application(job_id)


if __name__ == "__main__":
    mcp.run()