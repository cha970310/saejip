from django.contrib import admin
from blog.models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'modify_dt')
	list_filter = ('modify_dt', )
	search_fields = ('title', 'content')
	prepopulated_fields = {'slug': ('title', )}

	def get_queryset(self, request):
		return super().get_queryset(request).prefetch_related('tags')

	@staticmethod
	def tag_list(obj):
		return ','.join(o.name for o in obj.tags.all())

