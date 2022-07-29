from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views import View
from .models import jigo_Mst
from .services.service import jigo_MstService

from .forms.jigosho_form import jigo_MstForm, jigo_MstSearchForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class jigo_MstListView(ListView):
    """
    一覧
    """
    # 一覧を表示するモデルを指定する
    model = jigo_Mst
    # 1ページの件数
    paginate_by = 5
    template_name = 'jigosho/jigosho_list.html'

    # def get(self, request, *args, **kwargs):
    #     '''
    #     事業所一覧画面-初期表示処理
    #     '''
    #     # raise ApplicationException() # 例外テスト
    #     service = jigo_MstService(self.request)
    #     params = {
    #         'jigo_mst_list': service.retrievejigo_MstList()
    #     }

    #     return render(request, 'jigosho/jigosho_list.html', params)

    # 検索が実行された時の絞り込み処理
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = form = jigo_MstSearchForm(self.request.GET or None)

        if form.is_valid():
            jigo_name = form.cleaned_data.get('jigo_name')
            if jigo_name:
                # 空白で区切られていた場合は分割して繰り返す、and検索
                for word in jigo_name.split():
                    #部分検索 filter(モデル項目__icontains=画面値)
                    queryset = queryset.filter(jigo_name__icontains=word)

            search_jigo_Tag = form.cleaned_data.get('search_jigo_Tag')
            if search_jigo_Tag:
                #完全一致 filter(モデル項目=画面値)
                queryset = queryset.filter(jigo_tags=search_jigo_Tag)

            search_shogai_shubetu_Tag = form.cleaned_data.get('search_shogai_shubetu_Tag')
            if search_shogai_shubetu_Tag:
                #完全一致 filter(モデル項目=画面値)
                queryset = queryset.filter(shogai_shubetu_tags=search_shogai_shubetu_Tag)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        return context

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