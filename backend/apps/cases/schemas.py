import coreapi
import coreschema

from rest_framework.schemas import ManualSchema

vuetable_schema = ManualSchema(
    fields=[
        coreapi.Field(
            name='query',
            location='query',
            schema=coreschema.String(
                title='query',
                description='搜尋字串，篩選按案件標題/內容/類型/相關地址/地區/狀態、處理進度標題/內容',
                default='',
            ),
        ),
        coreapi.Field(
            name='sort',
            location='query',
            schema=coreschema.String(
                title='sort',
                description='排序欄位根據，id/state/type/create_time',
                default='id',
            ),
        ),
        coreapi.Field(
            name='ascending',
            location='query',
            schema=coreschema.String(
                title='ascending',
                description='順逆排，asc/desc',
                default='desc',
            ),
        ),
        coreapi.Field(
            name='limit',
            location='query',
            schema=coreschema.Number(
                title='limit',
                description='單頁回傳筆數',
                default=10,
            ),
        ),
        coreapi.Field(
            name='page',
            location='query',
            schema=coreschema.Number(
                title='page',
                description='回傳第幾頁結果',
                default=1,
            ),
        ),
    ],
    description='Custom API for vuetable-2 server-side datable, See: https://www.vuetable.com/',
)
