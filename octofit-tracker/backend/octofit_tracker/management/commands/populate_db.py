from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data in child-to-parent order
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        tony = User.objects.create(username='ironman', email='tony@stark.com', password='ironman', team=marvel)
        steve = User.objects.create(username='captainamerica', email='steve@rogers.com', password='shield', team=marvel)
        bruce = User.objects.create(username='hulk', email='bruce@banner.com', password='hulk', team=marvel)
        clark = User.objects.create(username='superman', email='clark@kent.com', password='superman', team=dc)
        brucew = User.objects.create(username='batman', email='bruce@wayne.com', password='batman', team=dc)
        diana = User.objects.create(username='wonderwoman', email='diana@themyscira.com', password='lasso', team=dc)

        # Add members to teams
        marvel.members.set([tony, steve, bruce])
        dc.members.set([clark, brucew, diana])

        # Create Workouts
        workout1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio', difficulty='Medium')
        workout2 = Workout.objects.create(name='Strength Training', description='Weight lifting', difficulty='Hard')

        # Create Activities
        Activity.objects.create(user=tony, activity_type='Running', duration=30, calories=300, date='2025-12-24')
        Activity.objects.create(user=steve, activity_type='Cycling', duration=45, calories=400, date='2025-12-23')
        Activity.objects.create(user=clark, activity_type='Swimming', duration=60, calories=500, date='2025-12-22')

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, points=100, rank=1)
        Leaderboard.objects.create(user=steve, points=90, rank=2)
        Leaderboard.objects.create(user=clark, points=80, rank=3)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
