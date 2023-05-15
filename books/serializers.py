from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Books


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('id', 'title', 'context', 'subtitle', 'author', 'isbn', 'price',)

    def valid(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'Message': 'Kitobni sarlavhasi harflardan tashkel topgan bo\'lishi kerak!'
                }
            )

        if Books.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'Message': 'Kitobni sarlavhasi va muallifi bir xil bo\'lgan kitobni saqlay olmisiz'
                }
            )

        return data

    def validate_price(self, price):
        if price < 0 or price > 999999999:
            raise ValidationError(
                {
                    'status': False,
                    'Message': 'Narx noto\'g\'ri kiritilgan!'
                }
            )

