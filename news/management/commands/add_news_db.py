from django.core.management.base import BaseCommand
from news.models import News


class Command(BaseCommand):
    help = 'Load sample news into the News model'

    SAMPLE_NEWS = [
        {
            'headline': 'Silent film festival announces 2026 lineup',
            'body': 'This year\'s program highlights rediscovered short films from the earliest era of cinema, including several titles from this dataset.',
            'date': '2026-06-15',
        },
        {
            'headline': 'Georges Melies retrospective opens at the museum',
            'body': 'A new exhibit gathers restored prints, production sketches, and hand-painted frames from the pioneering French filmmaker.',
            'date': '2026-05-02',
        },
        {
            'headline': 'Archivists digitize 1890s actuality films',
            'body': 'A joint preservation effort has produced new 4K scans of dozens of one-minute actuality films from the dawn of cinema.',
            'date': '2026-03-18',
        },
    ]

    def handle(self, *args, **kwargs):
        created_count = 0
        for item in self.SAMPLE_NEWS:
            obj, created = News.objects.update_or_create(
                headline=item['headline'],
                defaults={
                    'body': item['body'],
                    'date': item['date'],
                }
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Import completed. Created: {created_count}')
        )
