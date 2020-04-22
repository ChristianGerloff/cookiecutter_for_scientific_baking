# Welcome !
enjoyed the lecture

## Introduction

The talk will focus on data science practices, including version control, reproducible code examples, testing and the influence of the technical environment

## Useage
### Jupyter file
you can use the jupyter file in `src/notebooks/`

### Docker
If you have docker, you can simply clone or download the repo and start the build with

```
docker build -f Dockerfile -t cookiecutter_for_scientific_baking .
```
and run the repo

```
docker run -it -p 8888:8888  -d -v /$(pwd)/notebooks:/notebooks cookiecutter_for_scientific_baking
```

Now you can connect via your browser to the repo 127.0.0.1:8888.
The required token is located in `config/jupyter_notebook_config.py`