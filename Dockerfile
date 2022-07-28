FROM python:3.10.5 
ENV PYTHONUNBUFFERED 1 

RUN python -m pip install --upgrade pip

COPY /requirements.txt ./

# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install -r requirements.txt

# RUN pip install django
# RUN pip install mysqlclient
# #Django REST Framework
# RUN pip install djangorestframework
# #
# RUN pip install django-widget-tweaks
# #ImageField用ライブラリ
# RUN pip install Pillow
# #電話番号用ライブラリ
# #RUN pip install django-phonenumber-field[phonenumberslite]

# #認証用ライブラリ
# RUN pip install django-allauth