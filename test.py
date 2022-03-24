from requests import get, post

print(post('http://localhost:5000/api/new_job', json={'id': 10,
                                                      'job': 'gruzchik',
                                                      'work_size': '20',
                                                      'collaborators': 'Shamil Ivan',
                                                      'is_finished': False,
                                                      'team_leader': 'ya'}).json())  # корректный запрос
print(post('http://localhost:5000/api/new_job').json())  # пустой запрос
print(post('http://localhost:5000/api/new_job',  json={'job': 'gruzchik',
                                                       'work_size': '20'}).json())  # неполный запрос
print(post('http://localhost:5000/api/new_job',  json={'id': 1,
                                                       'job': 'gruzchik',
                                                       'work_size': '20',
                                                       'collaborators': 'Shamil Ivan',
                                                       'is_finished': False,
                                                       'team_leader': 'ya'}).json())  # запрос с существующим id