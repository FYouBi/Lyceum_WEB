from requests import get, post

print(post('http://localhost:5000/api/new_job', json={'job': 'gruzchik',
                                                      'work_size': '20',
                                                      'collaborators': 'Shamil Ivan',
                                                      'is_finished': False,
                                                      'team_leader': 'ya'}).json())
print(post('http://localhost:5000/api/new_job').json())
print(post('http://localhost:5000/api/new_job',  json={'job': 'gruzchik',
                                                      'work_size': '20'}).json())