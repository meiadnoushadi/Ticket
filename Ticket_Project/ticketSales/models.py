from django.db import models

# Create your models here.
class ConcertModel(models.Model):
    class Meta:
        verbose_name='کنسرت'
        verbose_name_plural='کنسرت ها'
    name=models.CharField(max_length=100,verbose_name='نام')
    SingerName=models.CharField(max_length=100,verbose_name='نام خواننده')
    lenght=models.IntegerField(verbose_name='مدت زمان کنسرت')
    poster=models.ImageField(upload_to='concertImages/',null=True,verbose_name='عکس پوستر')
    
    
    def __str__(self) -> str:
        return self.SingerName
    
class LocationModel(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=500,default='تهران برج میلاد')
    phone=models.CharField(max_length=11,null=True)
    capacity=models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class TimeModel(models.Model):
    concertmodel=models.ForeignKey(to=ConcertModel,on_delete=models.PROTECT)
    locationmodel=models.ForeignKey(to=LocationModel,on_delete=models.PROTECT)
    startDateTime=models.DateTimeField()
    seats=models.IntegerField()
    start=1
    end=2
    cancel=3
    sales=4
    status_choices=[('start','فروش بلیط شروع شده است'),('end','فروش بلیط پایان یافته است'),('cancel','این سانس لغو شده است'),('sales','در حال فروش بلیط'),]
    status=models.IntegerField(choices=status_choices)

    def __str__(self) -> str:
        return f"time : {self.startDateTime} | concert name : {self.concertmodel.name} | location : {self.locationmodel.name}"
    
    
class ProfileModel(models.Model):
    name=models.CharField(max_length=100)
    family=models.CharField(max_length=100)
    man=1
    woman=2
    status_chioces=[('man','مرد'),('woman','زن'),]
    gender=models.IntegerField(choices=status_chioces)
    profileImages=models.ImageField(upload_to='profileImages/',null=True)
    
    def __str__(self) -> str:
        return f"full name : {self.name} {self.family}"

class TicketModel(models.Model):
    profileModel=models.ForeignKey(to=ProfileModel,on_delete=models.PROTECT)
    timeModel=models.ForeignKey(to=TimeModel,on_delete=models.PROTECT)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    ticketImages=models.ImageField(upload_to='ticketImages/',null=True)
    
    def __str__(self) -> str:
        return f"ticket info : profile {ProfileModel.__str__} concert info {TimeModel.__str__}"
    