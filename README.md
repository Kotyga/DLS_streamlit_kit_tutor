# DLS_streamlit_kit_tutor
Туториал по работе с Streamlit в рамках курса по CV от DLS

## Подготовка рабочей среды

Streamlit - популярная библиотека Python с открытым исходным кодом, широко используемая разработчиками в ML для показа продукта. Её основное преимущество в том, что для работы с ней **НЕ требуются** специальные знания js/css/html/go и тд для создания сайтов. Достаточно хорошего владения Python и самого фреймворка.

### Создадим виртуальное окружение:
```shell
python -m venv venv
```

### Активируем его:

* Для Linux:

```shell
source venv/bin/activate
```
* Для Windows:

```shell
venv\Scripts\activate
```

### Обновим pip:
```shell
 pip install --upgrade pip
```

### Установим Streamlit:
```shell
 pip install streamlit
```

### Запустим демо библиотеки:
```shell
streamlit hello
```

Если все отработало верно, то откроется демо страница, в котором можно познакомиться с возможностями, предоставляемыми Streamlit

## Hello, world!
Добавим в проект файл `hello.py` следующего содержания:

### импортируем библиотеку streamlit
```python
import streamlit as st
```

### выводим текст
```python
st.text("Hello world!")
```
Выполним в терминале следующую команду:
```shell
streamlit run hello.py
```
Получили простое приложение, к которому можно обратиться локально по адресу `localhost:8501`

Модифицируем `hello.py`

### импортируем библиотеку streamlit
```python
import streamlit as st

if st.button('Click me!'):
    st.write('Hello, DLS Student! 🤖')
```
Посмотреть, что получается, можно все там же `localhost:8501`

## Полезные материалы по Streamlit
* 📍 [Шпаргалка](https://docs.streamlit.io/develop/quick-reference/cheat-sheet) 
* 📍 [Туториал как создать свое первое приложение на Streamlit](https://docs.streamlit.io/get-started/tutorials/create-an-app)
* 📍 [Основные функции фреймворка с примерами кода](https://docs.streamlit.io/develop/api-reference)
* 📍 [Галерея приложений реализованных на Streamlit](https://streamlit.io/gallery)

## Публикация в облако
Так примерно выглядит пайплайн публикации проекта в облако Streamlit. Важное уточнение: это будет малонагруженное приложение на CPU. Если хотите GPU, то надо арендовать виртуалку и с нее делать run вашего приложения.

![](src\pipeline.png)

## Этапы регистрации
Посетите сайт облака https://streamlit.io/cloud

![](src\reg_1.png)

Нажмите `Get Started`

![](src\reg_2.png)

Создаете аккаунт

![](src\reg_3.png)

Обязательно авторизация через `GitHub`

![](src\reg_4.png)
![](src\reg_5.png)

Далее открывается ваша рабочая область с проетками. Для нового проекта нажмите `Create App` в верхнем правом углу

![](src\reg_6.png)

Затем заполняете соответствующие поля. Если основной файл не был найден, Streamlit вам об этом скажет.

![](src\reg_7.png)

Важно уточнить, чтобы ваше приложение задеплоилось корректно в вашем репозитории должно быть:
1. Стартовая страница
2. файл requirements.txt

Если, например, вы хотите создать [многостраничник](https://docs.streamlit.io/develop/concepts/multipage-apps/pages-directory), то структура следующая (названия произвольные):

```
your_working_directory/
├── pages/
│   ├── a_page.py
│   └── another_page.py
└── your_homepage.py
```
