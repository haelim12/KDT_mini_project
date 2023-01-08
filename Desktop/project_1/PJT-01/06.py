import json
from pprint import pprint

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성

# def movie_info(movies_list):

#     key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
#     movie_info_dict = {}

#     for key in key_list:
#         movie_info_dict[key] = movies_list[key]
    
#     return movie_info_dict

# pprint(movie_info(movies_list))


# def movie_info(movies, genres):

#     movies_info_dict = []

#     for movie in movies:
#         genre_ids = movie['genre_ids']

#         gerne_names = []

#         for genre in gerne_names:

#             if ['id'] in genre_ids:
#                 gerne_names.append(genre['name'])
            
#         key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'gerne_ids']

#         movie_info_dict = {}
        
#         for key in key_list:
#             movie_info_dict[key] = movie[key]
        
#         movie_info_dict['gerne_names'] = gerne_names

#         movies_info_dict.append(movie_info_dict)
    
#     return movies_info_dict


key_list = ["id", "title", "vote_average", "overview", "genre_ids"]
check_list = []
check_dict = {}
for movie in movies_list:
    for key in key_list:
        check_dict[key] = movie[key]
    check_list.append(check_dict)
    check_dict = {}
pprint(check_list, sort_dicts=False)

# ===================================

# 답
new_movie_list = []

for movie in movies_list:
    new_movie = {
        'id': movie['id'],
        'title': movie['title'],
        'poster_path': movie['poster_path'],
        'vote_average': movie['vote_average'],
        'overview': movie['overview'],
        'genre_ids': movie['genre_ids'],
    }
    new_movie_list.append(new_movie)

print(new_movie_list)
