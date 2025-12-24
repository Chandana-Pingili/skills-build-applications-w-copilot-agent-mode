from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    is_superhero = models.BooleanField(default=True)
        def __str__(self):
            return self.username

    from djongo import models

    class User(models.Model):
        username = models.CharField(max_length=150, unique=True)
        email = models.EmailField(unique=True)
        password = models.CharField(max_length=128)
        team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL)
        def __str__(self):
            return self.username

    class Team(models.Model):
        name = models.CharField(max_length=100, unique=True)
        members = models.ArrayReferenceField(to=User)
        def __str__(self):
            return self.name

    class Activity(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        type = models.CharField(max_length=50)
        duration = models.IntegerField()  # minutes
        calories = models.IntegerField()
        date = models.DateField()
        def __str__(self):
            return f"{self.user.username} - {self.type}"

    class Workout(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        difficulty = models.CharField(max_length=50)
        def __str__(self):
            return self.name

    class Leaderboard(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        points = models.IntegerField(default=0)
        rank = models.IntegerField(default=0)
        def __str__(self):
            return f"{self.user.username} - {self.points}"
class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} - {self.activity_type}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team}: {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)
    def __str__(self):
        return self.name
