import os
from django.conf import settings
from django.core.management.base import BaseCommand
from movie.models import Movie


class Command(BaseCommand):
    help = "Assign pre-generated images from media/movie/images/ to each movie"

    def handle(self, *args, **kwargs):
        images_folder = os.path.join(settings.MEDIA_ROOT, 'movie', 'images')

        movies = Movie.objects.all()
        self.stdout.write(f"Found {movies.count()} movies")

        updated_count = 0
        for movie in movies:
            image_filename = f"m_{movie.title}.png"
            image_path_full = os.path.join(images_folder, image_filename)

            if not os.path.exists(image_path_full):
                self.stderr.write(f"Image not found for: {movie.title} ({image_filename})")
                continue

            movie.image = os.path.join('movie/images', image_filename)
            movie.save()
            updated_count += 1
            self.stdout.write(self.style.SUCCESS(f"Updated image for: {movie.title}"))

        self.stdout.write(self.style.SUCCESS(f"Finished updating {updated_count} movies with images from folder."))
