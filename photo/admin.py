from django.contrib import admin
# from django.contrib.auth.models import User
from .models import Photo, User


# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']  # photo에 관해 adminPage에서 띄울 목록
    raw_id_fields = ['author']  # admin의 고유 번호로 입력 할 수 있음
    list_filter = ['created', 'updated',
                   'author']  # 정해놓은대로(created, updated, author) 필터링해서 목록으로 보여줌 (author가 1개인 경우는 뜨지 않음)
    search_fields = ['text', 'created']  # 정해놓은대로 (text, created) 검색해서 목록으로 보여줌
    ordering = ['-updated', '-created']  # 정해놓은대로 (앞에서부터 순서대로) default: 오름차순, - : 내림차순 정렬


admin.site.register(Photo, PhotoAdmin)
admin.site.register(User)
