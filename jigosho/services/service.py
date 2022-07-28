from ..models import jigo_Mst
from django.utils import timezone
from datetime import datetime

class jigo_MstService:
    '''
    事業所管理用サービスクラス
    '''
    def __init__(self, request):
        self.request = request

    def retrievejigo_MstList(self):
        '''
        事業所一覧情報を検索する
        '''
        jigo_mstList = (jigo_Mst.objects
            #.filter(belong_user=self.request.user.email)
            .values('jigo_name', 'url', 'mail', 'tel', 'biko')
            .order_by('jigo_name')
        )
        return jigo_mstList