from django import forms
from jigosho.models import jigo_Mst, jigo_Tag, shogai_shubetu_Tag


class jigo_MstSearchForm(forms.Form):
    '''
    事業所マスタ検索フォーム
    '''
    jigo_name = forms.CharField(
        label='事業所名検索',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                      'autocomplete': 'off',
                                      'placeholder': '事業所名',
                                      })
    )

    search_jigo_Tag = forms.ModelChoiceField(
        label='事業形態での絞り込み',
        required=False,
        queryset=jigo_Tag.objects.order_by('name'),
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )

    search_shogai_shubetu_Tag = forms.ModelChoiceField(
        label='障害種別での絞り込み',
        required=False,
        queryset=shogai_shubetu_Tag.objects.order_by('name'),
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )

class jigo_MstForm(forms.ModelForm):
    '''
    事業所マスタフォーム
    '''
    class Meta:
        #モデルを指定
        model = jigo_Mst
        #表示するモデル項目名を指定
        fields = {'jigo_name', 'url', 'mail', 'tel', 'zip_code', 'address1', 'address2', 'address3', 'biko', 'biko_meisai', 'jigo_tags', 'shogai_shubetu_tags'}
        #class:CSSのクラス名(今回はBootstrap) placeholder:枠内の文字 autocomplete:入力補助機能
        widgets ={
            'jigo_name': forms.TextInput(attrs={'autocomplete': 'off',
                                   'placeholder': 'xxxx株式会社',
                                   'class': 'form-control'}),
            'url': forms.URLInput(attrs={'placeholder': 'https://www.google.com/',
                                   'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'autocomplete': 'off',
                                   'placeholder': 'xx@sample.com',
                                   'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'autocomplete': 'off',
                                   'placeholder': '999-9999-9999',
                                   'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'autocomplete': 'off',
                                   'placeholder': '記入例:1050012',
                                   'class': 'form-control'}),
            'address1': forms.TextInput(attrs={'autocomplete': 'off',
                                   'placeholder': 'xx県',
                                   'class': 'form-control'}),
            'address2': forms.TextInput(attrs={'autocomplete': 'off',
                                   'placeholder': 'xx市99-9-9',
                                   'class': 'form-control'}),
            'address3': forms.TextInput(attrs={'autocomplete': 'off',
                                   'placeholder': 'xxアパート1階',
                                   'class': 'form-control'}),
            'biko': forms.Textarea(attrs={'autocomplete': 'off',
                                   'placeholder': '事業所紹介文',
                                   'class': 'form-control',
                                   'rows': '2'}),
            'biko_meisai': forms.Textarea(attrs={'autocomplete': 'off',
                                   'placeholder': '事業所紹介文(詳細)',
                                   'class': 'form-control',
                                   'rows': '2'}),
            #'jigo_tags': forms.Select(attrs={'class': 'form-select'}),
            #'shogai_shubetu_tags': forms.Select(attrs={'class': 'form-select'}),
        }

    #フィールドの並び替え
    field_order = ['jigo_name', 'url', 'mail', 'tel', 'zip_code', 'address1', 'address2', 'address3', 'biko', 'biko_meisai', 'jigo_tags', 'shogai_shubetu_tags']