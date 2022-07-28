from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

#tagモデル(事業形態)
class jigo_Tag(models.Model):
    name = models.CharField(verbose_name='事業形態', max_length=200)
    regist_date = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    regist_user = models.CharField(verbose_name='登録ユーザ', max_length=50)
    update_date = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    update_user = models.CharField(verbose_name='更新ユーザ', max_length=50, null=True)

    def __str__(self):
        return self.name


#tagモデル(障害種別)
class shogai_shubetu_Tag(models.Model):
    name = models.CharField(verbose_name='障害種別', max_length=200)
    regist_date = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    regist_user = models.CharField(verbose_name='登録ユーザ', max_length=50)
    update_date = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    update_user = models.CharField(verbose_name='更新ユーザ', max_length=50, null=True)

    def __str__(self):
        return self.name


#モデル(事業所マスタ)
class jigo_Mst(models.Model):

    #数字チェック用
    number_regex = RegexValidator(regex='^[0-9]+$', message='数字のみ入力してください。')

    # #画像イメージ
    # jigo_img = models.ImageField(
    #     upload_to='files/',
    #     verbose_name='アイコン',
    #     height_field='url_height',
    #     width_field='url_width',
    #     blank=True,
    # )
    # #登録時にurl_height と url_width に高さと幅が保存される
    # url_height = models.IntegerField(
    #     editable=False,
    # )
    # url_width = models.IntegerField(
    #     editable=False,
    # )

    jigo_name = models.CharField(verbose_name='事業所名', max_length=400)
    url = models.URLField(verbose_name='URL', max_length=512, blank=True)
    mail = models.EmailField(
        verbose_name='メールアドレス', 
        max_length=256,
        blank=True,
    )
    
    tel = models.CharField(validators=[number_regex], max_length=15, verbose_name='電話番号', blank = True)

    #住所
    zip_code = models.CharField(
        verbose_name='郵便番号', max_length=8, blank=True, validators=[number_regex],
    )
    address1 = models.CharField(
        verbose_name='都道府県', max_length=40, blank=True,
    )
    address2 = models.CharField(
        verbose_name='市区町村番地', max_length=40, blank=True,
    )
    address3 = models.CharField(
        verbose_name='建物名',max_length=40,blank=True,
    )

    biko = models.TextField(verbose_name='紹介文', max_length=4096, blank=True)
    biko_meisai = models.TextField(verbose_name='備考', max_length=4096, blank=True)

    regist_date = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    regist_user = models.CharField(verbose_name='登録ユーザ', max_length=50)
    update_date = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    update_user = models.CharField(verbose_name='更新ユーザ', max_length=50, null=True)

    #事業モデルを紐づけ
    jigo_tags = models.ManyToManyField(jigo_Tag, verbose_name='事業タグ')
    #事業モデルを紐づけ
    shogai_shubetu_tags = models.ManyToManyField(shogai_shubetu_Tag, verbose_name='障害区分タグ')
    # 管理サイト上の表示設定
    def __str__(self):
        return '{}, {}, {}'.format(self.jigo_name, self.jigo_tags, self.shogai_shubetu_tags)