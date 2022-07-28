from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views import View
from .models import jigo_Mst
from .services.service import jigo_MstService

from .forms.jigosho_form import jigo_MstForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class jigo_MstListView(View):
    """
    一覧
    """
    # 一覧を表示するモデルを指定する
    #model = jigo_Mst
    # 1ページの件数
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        '''
        事業所一覧画面-初期表示処理
        '''
        # raise ApplicationException() # 例外テスト
        service = jigo_MstService(self.request)
        params = {
            'jigo_mst_list': service.retrievejigo_MstList()
        }

        return render(request, 'jigosho/jigosho_list.html', params)


class jigo_MstCreateView(CreateView):
    """
    新規作成(事業所マスタ)
    """
    template_name = 'jigosho/jigosho_create.html'
    form_class = jigo_MstForm
    model = jigo_Mst
    success_url = reverse_lazy('jigosho:jigo_mst_list_view')

    def get_initial(self):
        """デフォルト値(画面)の設定"""
        initial = super().get_initial()
        #initial['regist_user'] = self.request.user  # 登録ユーザにログインユーザーに設定
        return initial
    
    def post(self, request, **kwargs):
        """
        作成者と修正者およびワークスペースの自動入力
        """
        request.POST = request.POST.copy()
        # ログインユーザー情報の取得
        user = request.user
        # 登録ユーザと更新ユーザにログインユーザーを入力
        request.POST['regist_user'] = user.username
        request.POST['update_user'] = user.username

        return super().post(request, **kwargs)
    
    def form_valid(self, form):
        """
        フォーム入力後の処理(保存時の前処理)
        """
        # ユーザーを投稿者として保存できるようにする
        object = form.save(commit=False)
        object.regist_user = self.request.user.username
        object.update_user = self.request.user.username
        object.save()
        return super().form_valid(form)