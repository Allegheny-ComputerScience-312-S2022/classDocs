
@echo  [+]  Setting up your working container.
# docker run --rm -it -v %cd%:/root devi
# docker run --rm -it -v "%cd%:/root" devi
docker run --rm -it -p 8501:8501 -v $PWD:/root devi
