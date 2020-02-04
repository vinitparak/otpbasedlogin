import django_filters
from .models import city


class UserFilter(django_filters.FilterSet):
	Name = django_filters.CharFilter(lookup_expr='icontains')
	CountryCode = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = city
		fields = ('Name', 'CountryCode')
