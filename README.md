# VKinder
---
Все слышали про известное приложение для знакомств - Tinder. Приложение предоставляет простой интерфейс для выбора понравившегося человека. Сейчас в Google Play более 100 миллионов установок.

Используя данные из VK, нужно сделать сервис намного лучше, чем Tinder, а именно: чат-бота "VKinder". Бот должен искать людей, подходящих под условия, на основании информации о пользователе из VK:
1. возраст 
2. пол
3. город 
4. семейное положение.

###### У тех людей, которые подошли по требованиям пользователю, получать топ-3 популярных фотографии профиля и отправлять их пользователю в чат вместе со ссылкой на найденного человека.
Популярность определяется по количеству лайков и комментариев.
---
## Входные данные
1. Имя пользователя 
2. id в ВК, для которого мы ищем пару.
---
## Настройка
Файл settings.py содержит переменную DSN. Необходимо изменить в строке пользователя postgresql и пароль, а также название базы данных.
Также в файле settings.py есть 2 функции get_user_token и get_token_group. в строке with open('group token', 'r') as file:
вместо group token пишем название своего файла, куда скопировали токен.
Далее заходим в файл main и запускаем код.