from rest_framework import serializers
from .models import Artist, Song



class SongSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        read_only=True
    )
    class Meta:
        model = Song
        fields = ('id', 'artist', 'title', 'album', 'preview_url',)


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    songs = SongSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Artist
        fields =('id', 'photo_url', 'nationality', 'name', 'songs')


