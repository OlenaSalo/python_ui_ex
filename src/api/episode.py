import requests


def api_create_episode(name):
    data = {"name": name}
    res = requests.post("http://localhost:8087/api/episodes", json=data, headers={
        "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiaXNBZG1pbiI6dHJ1ZSwibmFtZSI6ImFkbWluIiwiaWF0IjoxNjg2MzMxNzI5LCJleHAiOjE2ODY5MzY1Mjl9.NO5gghKyu00DQUYH4h1KnwLLVL4ama17AkeHbQOmSp_B7kr0qLNOPE16pKy4SvpScHY3x70DTdzpbhKlUGsUbQ"
    })
    assert res.status_code == 200