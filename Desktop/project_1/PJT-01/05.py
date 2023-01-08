import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성

# def movie_info(movie):
#     # 해당되는 key를 list에 담기
#     movie_list = ['id', 'title', 'vote_average', 'overview', 'genre_ids']
#     # 새로운 dicionary를 담을 변수 선언
#     movie_info_dict = {}

#     # key_list 요소에 해당하는 정보만 추출
#     for i in movie_list:
#         movie_info_dict[i] = movie[i]
    
#     # 새롭게 재가공한 dictionary 변환
#     return movie_info_dict

# pprint(movie_info(movie), sort_dicts = False)

# ===================================

# 답
new_movie = {
    'id': movie['id'],
    'title': movie['title'],
    'vote_average': movie['vote_average'],
    'overview': movie['overview'],
    'genre_ids': movie['genre_ids'],
}
print(new_movie)