# DLS_streamlit_kit_tutor
Tutorial on working with Streamlit as part of the Computer Vision course from the Deep Learning School (MIPT)

## Preparation of the working environment

Streamlit is a popular open source Python library widely used by ML developers to show the product. Its main advantage is that working with it ** DOES NOT require** special knowledge of js/css/html/go and so on to create websites. A good command of Python and the framework itself is enough.

### Creating a virtual environment:
```shell
python -m venv venv
```

### Activate it:

* Linux:

```shell
source venv/bin/activate
```
* Windows:

```shell
venv\Scripts\activate
```

### Upgrade pip:
```shell
 pip install --upgrade pip
```

### Install Streamlit:
```shell
 pip install streamlit
```

### Let's launch the demo library:
```shell
streamlit hello
```

If everything worked out correctly, a demo page will open where you can get acquainted with the features provided by Streamlit.

## Hello, world!
Adding a file to the project `hello.py ` of the following content:

* Importing the streamlit library
```python
import streamlite as st
```

* Output text
```python
st.text("Hello world!")
```
* Run the following command in the terminal:
```shell
streamlit run hello.py
```
We got a simple application that can be accessed locally at `localhost:8501`

* Modify `hello.py `

```python
import streamlit as st

if st.button('Click me!'):
    st.write('Hello, DLS Student! 🤖')
```
* You can still see what happens in the same place `localhost:8501`

## Useful materials on Streamlit
* 📍 [Cheat Sheet](https://docs.streamlet.io/develop/quick-reference/cheat-sheet )
* 📍 [Tutorial on how to create your first app on Streamlit](https://docs.streamlit.io/get-started/tutorials/create-an-app )
* 📍 [The main functions of the framework with code examples](https://docs.streamlit.io/develop/api-reference )
* 📍 [Gallery of applications implemented on Streamlit](https://streamlit.io/gallery )

## Publishing to the cloud
This is what the pipeline for publishing a project to the Streamlit cloud looks like. Important clarification: it will be a low-load application on the CPU. If you want a GPU, then you need to rent a virtual machine and run your application from it.
![](https://github.com/Kotyga/DLS_streamlit_kit_tutor/blob/main/src/pipeline.png)

## Registration stages
Visit the cloud's website https://streamlit.io/cloud

![](https://github.com/Kotyga/DLS_streamlit_kit_tutor/blob/main/src/reg_1.png)

Click `Get started`

![](https://github.com/Kotyga/DLS_streamlit_kit_tutor/blob/main/src/reg_2.png)

Creating an account

![](https://github.com/Kotyga/DLS_streamlit_kit_tutor/blob/main/src/reg_3.png)

Authorization via GitHub is required

![](https://github.com/Kotyga/DLS_streamlit_kit_tutor/blob/main/src/reg_4.png)
![](https://github.com/Kotyga/DLS_streamlit_kit_tutor/blob/main/src/reg_5.png)

Next, your workspace opens with projects. For a new project, click `Create App` in the upper right corner

![](https://github.com/Kotyga/DLS_streamlit_kit_tutor/blob/main/src/reg_6.png)

Then fill in the appropriate fields. If the main file was not found, Streamlit will tell you about it.

![](https://github.com/Kotyga/DLS_streamlit_kit_tutor/blob/main/src/reg_7.png)

It is important to clarify that in order for your application to be installed correctly, your repository must have:
1. Start page
2. The file requirements.txt

If, for example, you want to create a [multipage](https://docs.streamlet.io/develop/concepts/multipage-apps/pages-directory), then the structure is as follows (names are arbitrary):
```
your_working_directory/
├── pages/
│   ├── a_page.py
│   └── another_page.py
└── your_homepage.py
```
