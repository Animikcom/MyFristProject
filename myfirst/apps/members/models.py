from django.db import models


class Tblaccount(models.Model):
    account = models.SmallIntegerField(db_column='ACCOUNT', primary_key=True)  # Field name made lowercase.
    family = models.CharField(db_column='FAMILY', max_length=20, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
    second = models.CharField(db_column='SECOND', max_length=20, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
    pasport = models.CharField(db_column='PASPORT', max_length=120, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
    born = models.DateTimeField(db_column='BORN', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=20, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime', blank=True, null=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='HostName', max_length=20, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=128, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
         return self.username
     
    # class Meta:
    #     managed = False
    #     db_table = 'tblAccount'


# class Tblbuilding(models.Model):
#     street = models.OneToOneField('Tblstreet', models.DO_NOTHING, db_column='STREET', primary_key=True)  # Field name made lowercase.
#     house = models.SmallIntegerField(db_column='HOUSE')  # Field name made lowercase.
#     district = models.ForeignKey('Tbldistrict', models.DO_NOTHING, db_column='DISTRICT', blank=True, null=True)  # Field name made lowercase.
#     land = models.IntegerField(db_column='LAND', blank=True, null=True)  # Field name made lowercase.
#     year = models.SmallIntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
#     material = models.ForeignKey('Tblwall', models.DO_NOTHING, db_column='MATERIAL', blank=True, null=True)  # Field name made lowercase.
#     comment = models.TextField(db_column='COMMENT', db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     wear = models.SmallIntegerField(db_column='WEAR', blank=True, null=True)  # Field name made lowercase.
#     cost = models.IntegerField(db_column='COST', blank=True, null=True)  # Field name made lowercase.
#     line = models.IntegerField(db_column='LINE', blank=True, null=True)  # Field name made lowercase.
#     square = models.IntegerField(db_column='SQUARE', blank=True, null=True)  # Field name made lowercase.
#     picture = models.CharField(db_column='PICTURE', max_length=8, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     kind = models.SmallIntegerField(db_column='KIND', blank=True, null=True)  # Field name made lowercase.
#     elevator = models.BooleanField(db_column='ELEVATOR')  # Field name made lowercase.
#     inspector = models.CharField(db_column='INSPECTOR', max_length=15, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     date_up = models.DateTimeField(db_column='DATE_UP', blank=True, null=True)  # Field name made lowercase.
#     time_up = models.CharField(db_column='TIME_UP', max_length=8, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     flats = models.SmallIntegerField(db_column='FLATS', blank=True, null=True)  # Field name made lowercase.
#     upsize_ts = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'tblBuilding'
#         unique_together = (('street', 'house'),)


# class Tbldistrict(models.Model):
#     district = models.SmallIntegerField(db_column='DISTRICT', primary_key=True)  # Field name made lowercase.
#     area = models.CharField(db_column='AREA', max_length=15, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblDistrict'


# class Tblexcel(models.Model):
#     inn = models.CharField(db_column='INN', max_length=13, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     num_treaty = models.CharField(db_column='NUM_TREATY', max_length=10, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     data_zap = models.DateTimeField(db_column='DATA_ZAP', blank=True, null=True)  # Field name made lowercase.
#     contents = models.CharField(db_column='CONTENTS', max_length=12, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     nach = models.FloatField(db_column='NACH', blank=True, null=True)  # Field name made lowercase.
#     ymyb = models.FloatField(db_column='YMYB', blank=True, null=True)  # Field name made lowercase.
#     ypvs = models.FloatField(db_column='YPVS', blank=True, null=True)  # Field name made lowercase.
#     ypdona = models.FloatField(db_column='YPDONA', blank=True, null=True)  # Field name made lowercase.
#     ypnedo = models.FloatField(db_column='YPNEDO', blank=True, null=True)  # Field name made lowercase.
#     vpe = models.FloatField(db_column='VPE', blank=True, null=True)  # Field name made lowercase.
#     saldo = models.FloatField(db_column='SALDO', blank=True, null=True)  # Field name made lowercase.
#     npe = models.FloatField(db_column='NPE', blank=True, null=True)  # Field name made lowercase.
#     raypvo = models.FloatField(db_column='RAYPVO', blank=True, null=True)  # Field name made lowercase.
#     ostpe = models.FloatField(db_column='OSTPE', blank=True, null=True)  # Field name made lowercase.
#     shna = models.FloatField(db_column='SHNA', blank=True, null=True)  # Field name made lowercase.
#     shypvo = models.FloatField(db_column='SHYPVO', blank=True, null=True)  # Field name made lowercase.
#     ostsh = models.FloatField(db_column='OSTSH', blank=True, null=True)  # Field name made lowercase.
#     countfam = models.CharField(db_column='COUNTFAM', max_length=12, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     countday = models.DateTimeField(db_column='COUNTDAY', blank=True, null=True)  # Field name made lowercase.
#     counttime = models.CharField(db_column='COUNTTIME', max_length=8, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     remark = models.CharField(db_column='REMARK', max_length=27, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblExcel'


# class Tblflats(models.Model):
#     street = models.OneToOneField(Tblbuilding, models.DO_NOTHING, db_column='STREET', primary_key=True)  # Field name made lowercase.
#     house = models.ForeignKey(Tblbuilding, models.DO_NOTHING, db_column='HOUSE')  # Field name made lowercase.
#     flat = models.SmallIntegerField(db_column='FLAT')  # Field name made lowercase.
#     storey = models.SmallIntegerField(db_column='STOREY', blank=True, null=True)  # Field name made lowercase.
#     rooms = models.SmallIntegerField(db_column='ROOMS', blank=True, null=True)  # Field name made lowercase.
#     squareflat = models.FloatField(db_column='SQUAREFLAT')  # Field name made lowercase.
#     dwell = models.FloatField(db_column='DWELL')  # Field name made lowercase.
#     branch = models.FloatField(db_column='BRANCH')  # Field name made lowercase.
#     balcony = models.FloatField(db_column='BALCONY')  # Field name made lowercase.
#     height = models.FloatField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
#     decoration = models.SmallIntegerField(db_column='DECORATION', blank=True, null=True)  # Field name made lowercase.
#     cost = models.DecimalField(db_column='COST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     twolevel = models.SmallIntegerField(db_column='TWOLEVEL', blank=True, null=True)  # Field name made lowercase.
#     account = models.OneToOneField(Tblaccount, models.DO_NOTHING, db_column='ACCOUNT')  # Field name made lowercase.
#     upsize_ts = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'tblFlats'
#         unique_together = (('street', 'house', 'flat'),)


# class Tblnumeral(models.Model):
#     cnumeral = models.CharField(db_column='cNumeral', max_length=12, db_collation='Cyrillic_General_CS_AS')  # Field name made lowercase.
#     dnumeral = models.IntegerField(db_column='dNumeral')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblNumeral'


# class Tblowners(models.Model):
#     street = models.OneToOneField(Tblflats, models.DO_NOTHING, db_column='STREET', primary_key=True)  # Field name made lowercase.
#     house = models.ForeignKey(Tblflats, models.DO_NOTHING, db_column='HOUSE')  # Field name made lowercase.
#     flat = models.ForeignKey(Tblflats, models.DO_NOTHING, db_column='FLAT')  # Field name made lowercase.
#     number = models.SmallIntegerField(db_column='NUMBER')  # Field name made lowercase.
#     family = models.CharField(db_column='FAMILY', max_length=20, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=15, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     second = models.CharField(db_column='SECOND', max_length=15, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     born = models.DateTimeField(db_column='BORN', blank=True, null=True)  # Field name made lowercase.
#     document = models.CharField(db_column='DOCUMENT', max_length=120, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='STATUS', max_length=20, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblOwners'
#         unique_together = (('street', 'house', 'flat', 'number'),)


# class Tblstreet(models.Model):
#     street = models.SmallIntegerField(db_column='STREET', primary_key=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=20, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     sign = models.CharField(db_column='SIGN', max_length=10, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     first = models.BooleanField(db_column='FIRST')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblStreet'


# class Tbluser(models.Model):
#     lastname = models.CharField(db_column='LastName', primary_key=True, max_length=15, db_collation='Cyrillic_General_CS_AS')  # Field name made lowercase.
#     firstname = models.CharField(db_column='FirstName', max_length=12, db_collation='Cyrillic_General_CS_AS')  # Field name made lowercase.
#     secondname = models.CharField(db_column='SecondName', max_length=15, db_collation='Cyrillic_General_CS_AS')  # Field name made lowercase.
#     post = models.CharField(db_column='Post', max_length=25, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     password = models.CharField(db_column='PassWord', max_length=10, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     filephoto = models.CharField(db_column='FilePhoto', max_length=8, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     access01 = models.BooleanField(db_column='Access01')  # Field name made lowercase.
#     access02 = models.BooleanField(db_column='Access02')  # Field name made lowercase.
#     access03 = models.BooleanField(db_column='Access03')  # Field name made lowercase.
#     access04 = models.BooleanField(db_column='Access04')  # Field name made lowercase.
#     access05 = models.BooleanField(db_column='Access05')  # Field name made lowercase.
#     access06 = models.BooleanField(db_column='Access06')  # Field name made lowercase.
#     access07 = models.BooleanField(db_column='Access07')  # Field name made lowercase.
#     access08 = models.BooleanField(db_column='Access08')  # Field name made lowercase.
#     access09 = models.BooleanField(db_column='Access09')  # Field name made lowercase.
#     access10 = models.BooleanField(db_column='Access10')  # Field name made lowercase.
#     access11 = models.BooleanField(db_column='Access11')  # Field name made lowercase.
#     access12 = models.BooleanField(db_column='Access12')  # Field name made lowercase.
#     access13 = models.BooleanField(db_column='Access13')  # Field name made lowercase.
#     access14 = models.BooleanField(db_column='Access14')  # Field name made lowercase.
#     inspector = models.CharField(db_column='Inspector', max_length=255, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     date_up = models.DateTimeField(db_column='Date_up', blank=True, null=True)  # Field name made lowercase.
#     time_up = models.CharField(db_column='Time_up', max_length=255, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.
#     range = models.FloatField(db_column='Range', blank=True, null=True)  # Field name made lowercase.
#     upsize_ts = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'tblUser'
#         unique_together = (('lastname', 'firstname', 'secondname'),)


# class Tblwall(models.Model):
#     material = models.SmallIntegerField(db_column='MATERIAL', primary_key=True)  # Field name made lowercase.
#     wall = models.CharField(db_column='WALL', max_length=15, db_collation='Cyrillic_General_CS_AS', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblWall'
