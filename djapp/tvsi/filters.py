from django_filters import FilterSet, CharFilter, OrderingFilter
from django.db.models import Count
from .models import Episode


class EpisodeFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    order_likes = OrderingFilter(fields=(
        ('order by number of likes', 'order_by_number_of_likes'),
    ), choices=(
        ('ase', 'number of likes asc'),
        ('desc', 'number of likes desc'),
    ), method='order_by_number_of_likes')

    class Meta:
        model = Episode
        fields = ('name',)

    def order_by_number_of_likes(self, queryset, name, value):
        qs = queryset.annotate(Count('user_liked'))
        match value:
            case ['ase']:
                return qs.order_by('user_liked__count')
            case ['desc']:
                return qs.order_by('-user_liked__count')
            case _:
                return qs
