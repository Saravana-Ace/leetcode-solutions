retrieve_latest_submission_id = """
query recentAcSubmissions($username: String!) {
    recentAcSubmissionList(username: $username, limit: 1) {
        id
        title
    }
}
"""

retrieve_latest_submission_code = """
query recentAcSubmissionCode($submissionId: Int!) {
    submissionDetails(submissionId: $submissionId) {
        code
    }
}
"""