from django.db import models

# Create your models here.

class StaffInfo(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/')
    staff_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    designation = models.CharField(max_length=255)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.staff_name

class CowInfo(models.Model):
    CONTROL_NUMBER_CHOICES = [
        ('sold', 'Sold'),
        ('available', 'Available'),
    ]

    cow_control_number = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='cow_images/')
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    cow_type = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    animal_status = models.CharField(max_length=20, choices=CONTROL_NUMBER_CHOICES)

    def __str__(self):
        return f"Cow {self.cow_control_number}"


class VaccineMonitoring(models.Model):
    cow_number = models.ForeignKey(CowInfo, on_delete=models.CASCADE)
    date = models.DateField()
    remarks = models.TextField()

    def __str__(self):
        return f"Vaccine record for Cow {self.cow_number.cow_control_number} on {self.date}"


class FeedMonitoring(models.Model):
    cow_number = models.ForeignKey(CowInfo, on_delete=models.CASCADE)
    date = models.DateField()
    remarks = models.TextField()
    food_item = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    feeding_time = models.TimeField()

    def __str__(self):
        return f"Feed record for Cow {self.cow_number.cow_control_number} on {self.date} at {self.feeding_time}"


class MilkCollection(models.Model):
    cow_number = models.ForeignKey(CowInfo, on_delete=models.CASCADE)
    collection_id = models.CharField(max_length=20, unique=True)
    date = models.DateField()
    liter = models.DecimalField(max_digits=5, decimal_places=2)
    price_per_liter = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Milk collection record for Cow {self.cow_number.cow_control_number} on {self.date}"


class MilkSale(models.Model):
    collection_number = models.ForeignKey(MilkCollection, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    liter = models.DecimalField(max_digits=5, decimal_places=2)
    price_per_liter = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Milk sale record for Collection {self.collection_number.collection_id} on {self.date}"


class MilkSaleReport(models.Model):
    cow_number = models.ForeignKey(CowInfo, on_delete=models.CASCADE)
    liter = models.DecimalField(max_digits=5, decimal_places=2)
    price_per_liter = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Milk sale report for Cow {self.cow_number.cow_control_number} on {self.date}"


class CowSale(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    date = models.DateField()
    cow_number = models.ForeignKey(CowInfo, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    customer_name = models.CharField(max_length=255)
    customer_contact = models.CharField(max_length=15)
    customer_email = models.EmailField()
    remarks = models.TextField()

    def __str__(self):
        return f"Cow sale record for Cow {self.cow_number.cow_control_number} on {self.date}"


class CowSaleReport(models.Model):
    cow_number = models.ForeignKey(CowInfo, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Cow sale report for Cow {self.cow_number.cow_control_number} on {self.date}"