vkAudioSort

Сортировка аудиозаписей ВКонтакте в алфавитном порядке по исполнителю или названию.

VKontakte audio sorting in alphabetic order by artist or title.
===========

Перед началом работы нужно получить token - ключ для доступа к API.

Посылаем такой запрос: 
https://oauth.vk.com/authorize?client_id=4111910&redirect_uri=https://oauth.vk.com/blank.html&scope=12&display=mobile&response_type=token
        
Из ответа вида  https://oauth.vk.com/blank.html#access_token=f18060fc76c927980ba65f828521e47acb8b3b59843d90de54893e9a25cb2c9937304ed926bcf83768a3c&expires_in=86400&user_id=51758590  копируем access_token и свой user_id.
