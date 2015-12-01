from django.db import models
import random

class ArrayGenerator(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    size = models.IntegerField(default=10)
    min_num = models.IntegerField(default=0)
    max_num = models.IntegerField(default=100)
    unsorted_file = models.FileField(null=True)
    sorted_file = models.FileField(null=True)
    median_maintenance = models.FileField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def generate_unsorted(self, size=10, min_num=0, max_num=100):
        if not self.size:
            self.size = size
        if not self.min_num:
            self.min_num = min_num
        if not self.max_num:
            self.max_num = max_num

        alist = []
        while len(alist) < self.size:
            alist.append(random.randint(self.min_num, self.max_num))
        print alist

    def __str__(self):
        return "id: %s\nsize: %s\nmin_num: %s\nmax_num: %s\n" % (str(self.id), str(self.size), str(self.min_num), str(self.max_num))