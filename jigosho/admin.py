from django.contrib import admin
from .models import jigo_Tag, shogai_shubetu_Tag, jigo_Mst #追加部分

# 管理画面にjigo_Tagモデルを登録
admin.site.register(jigo_Tag)
# 管理画面にshogai_shubetu_Tagモデルを登録
admin.site.register(shogai_shubetu_Tag)
# 管理画面にjigo_Mstモデルを登録
admin.site.register(jigo_Mst)