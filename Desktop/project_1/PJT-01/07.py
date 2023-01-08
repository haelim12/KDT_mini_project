import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성 

# movies_list = json.load(movie_json)

# def movie_info(movies, genres):

#     movies_info_dict = []

#     for movie in movies:
#         genre_ids = movie['genre_ids']

#         gerne_names = []

#         for genre in gerne_names:

#             if genre['id'] in genre_ids:
#                 gerne_names.append(genre['name'])
            
#         key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'gerne_ids']

#         movie_info_dict = {}
        
#         for key in key_list:
#             movie_info_dict[key] = movie[key]
        
#         movie_info_dict['gerne_names'] = gerne_names

#         movies_info_dict.append(movie_info_dict)
    
#     return movies_info_dict

# pprint(movie_info(movies_list,genres_list), sort_dicts = False)

# ===================================

# 답
genre_ids = movie['genre_ids']

genre_list = []
for genre_id in genre_ids:
    for genre_dict in genres_list:
        if genre_id == genre_dict['id']:
            genre_list.append(genre_dict['name'])

print(genre_list)