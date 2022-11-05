# test_tasks_shop
Тестовые задания для выхода в младшую лигу

* Задача №1 (test_1) Разработать функцию определения счета в игре 

В примере кода генерируется список фиксаций состояния счета игры в течение матча.
Необходимо разработать функцию get_score(game_stamps, offset), которая вернет счет на момент offset в списке game_stamps.

* Задача №2 (test_2) Разработать тесты для функции определения счета в игре  

Для разработанной в предыдущем задании функции get_score(game_stamps, offset) необходимо разработать unit-тесты на фреймворке unittest.
Тесты должны учитывать все возможные случаи использования функции, концентрироваться на проверке одного случая, не повторяться, название тестов должно отражать суть выполняемой проверки.

* Задача №3 (test_3) Разработать парсер смартфонов

Разработать парсер, который будет собирать информацию о версиях операционных систем в топ-100 смартфонах с самым высоким рейтингом пользователей в каталоге ozon.ru.
На сайте ozon.ru в категории “Электроника -> Телефоны и смарт-часы” с сортировкой “Высокий рейтинг” нужно собрать информацию о первых 100 смартфонах попавших в выборку. Перейти на страницу с каждым из них и забрать информацию о версии операционной системы из характеристик. По собранным данным построить распределение моделей по версиям операционных систем в порядке убывания, например:

Android 8 — 12  
Android 10 — 9  
iOS 14 — 8  
…  

Для парсинга следует использовать язык программирования Python, фреймворк Scrapy, для скачивания динамических частей сайта следует использовать Scrapy+Selenium. В выполнении задания может помочь scrapy proxy rotation middleware.
Для расчета распределения следует использовать фреймворк Pandas. 
