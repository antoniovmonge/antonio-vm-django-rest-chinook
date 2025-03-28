from django.db import models


class Album(models.Model):
    album_id = models.AutoField(db_column="AlbumId", primary_key=True)
    title = models.CharField(max_length=200, db_column="Title")
    artist_id = models.ForeignKey("Artist", models.DO_NOTHING, db_column="ArtistId")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        managed = False
        db_table = "albums"
        ordering = ["album_id"]


class Artist(models.Model):
    artist_id = models.AutoField(db_column="ArtistId", primary_key=True)
    name = models.CharField(max_length=200, db_column="Name", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = "artists"
        ordering = ["artist_id"]


class Customer(models.Model):
    customer_id = models.AutoField(db_column="CustomerId", primary_key=True)
    firstname = models.CharField(max_length=200, db_column="FirstName")
    lastname = models.CharField(max_length=200, db_column="LastName")
    company = models.CharField(
        max_length=200, db_column="Company", blank=True, null=True
    )
    address = models.CharField(
        max_length=200, db_column="Address", blank=True, null=True
    )
    city = models.CharField(max_length=200, db_column="City", blank=True, null=True)
    state = models.CharField(max_length=200, db_column="State", blank=True, null=True)
    country = models.CharField(
        max_length=200, db_column="Country", blank=True, null=True
    )
    postalcode = models.CharField(
        max_length=200, db_column="PostalCode", blank=True, null=True
    )
    phone = models.CharField(max_length=200, db_column="Phone", blank=True, null=True)
    fax = models.CharField(max_length=200, db_column="Fax", blank=True, null=True)
    email = models.CharField(max_length=200, db_column="Email")
    supportrepid = models.ForeignKey(
        "Employee", models.DO_NOTHING, db_column="SupportRepId", blank=True, null=True
    )

    def __str__(self):
        return f"{self.email}"

    class Meta:
        managed = False
        db_table = "customers"
        ordering = ["customer_id"]


class Employee(models.Model):
    employee_id = models.AutoField(db_column="EmployeeId", primary_key=True)
    lastname = models.CharField(max_length=200, db_column="LastName")
    firstname = models.CharField(max_length=200, db_column="FirstName")
    title = models.CharField(max_length=200, db_column="Title", blank=True, null=True)
    reportsto = models.ForeignKey(
        "self", models.DO_NOTHING, db_column="ReportsTo", blank=True, null=True
    )
    birthdate = models.DateTimeField(db_column="BirthDate", blank=True, null=True)
    hiredate = models.DateTimeField(db_column="HireDate", blank=True, null=True)
    address = models.CharField(
        max_length=200, db_column="Address", blank=True, null=True
    )
    city = models.CharField(max_length=200, db_column="City", blank=True, null=True)
    state = models.CharField(max_length=200, db_column="State", blank=True, null=True)
    country = models.CharField(
        max_length=200, db_column="Country", blank=True, null=True
    )
    postalcode = models.CharField(
        max_length=200, db_column="PostalCode", blank=True, null=True
    )
    phone = models.CharField(max_length=200, db_column="Phone", blank=True, null=True)
    fax = models.CharField(max_length=200, db_column="Fax", blank=True, null=True)
    email = models.CharField(max_length=200, db_column="Email", blank=True, null=True)

    def __str__(self):
        return f"{self.email}"

    class Meta:
        managed = False
        db_table = "employees"
        ordering = ["employee_id"]


class Genre(models.Model):
    genre_id = models.AutoField(db_column="GenreId", primary_key=True)
    name = models.CharField(max_length=200, db_column="Name", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = "genres"


class InvoiceItem(models.Model):
    invoicelineid = models.AutoField(db_column="InvoiceLineId", primary_key=True)
    invoice_id = models.ForeignKey("Invoice", models.DO_NOTHING, db_column="InvoiceId")
    track_id = models.ForeignKey("Track", models.DO_NOTHING, db_column="TrackId")
    unitprice = models.CharField(max_length=200, db_column="UnitPrice")
    quantity = models.IntegerField(db_column="Quantity")

    class Meta:
        managed = False
        db_table = "invoice_items"


class Invoice(models.Model):
    invoice_id = models.AutoField(db_column="InvoiceId", primary_key=True)
    customer_id = models.ForeignKey(Customer, models.DO_NOTHING, db_column="CustomerId")
    invoicedate = models.DateTimeField(db_column="InvoiceDate")
    billingaddress = models.CharField(
        max_length=200, db_column="BillingAddress", blank=True, null=True
    )
    billingcity = models.CharField(
        max_length=200, db_column="BillingCity", blank=True, null=True
    )
    billingstate = models.CharField(
        max_length=200, db_column="BillingState", blank=True, null=True
    )
    billingcountry = models.CharField(
        max_length=200, db_column="BillingCountry", blank=True, null=True
    )
    billingpostalcode = models.CharField(
        max_length=200, db_column="BillingPostalCode", blank=True, null=True
    )
    total = models.CharField(max_length=200, db_column="Total")

    class Meta:
        managed = False
        db_table = "invoices"


class MediaType(models.Model):
    mediatypeid = models.AutoField(db_column="MediaTypeId", primary_key=True)
    name = models.CharField(max_length=200, db_column="Name", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = "media_types"


class PlaylistTrack(models.Model):
    playlist_id = models.OneToOneField(
        "Playlist", models.DO_NOTHING, db_column="PlaylistId", primary_key=True
    )
    track_id = models.ForeignKey("Track", models.DO_NOTHING, db_column="TrackId")

    class Meta:
        managed = False
        db_table = "playlist_track"


class Playlist(models.Model):
    playlist_id = models.AutoField(db_column="PlaylistId", primary_key=True)
    name = models.CharField(max_length=200, db_column="Name", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "playlists"


class SqliteStat1(models.Model):
    tbl = models.CharField(max_length=200, blank=True, null=True)
    idx = models.CharField(max_length=200, blank=True, null=True)
    stat = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sqlite_stat1"


class Track(models.Model):
    track_id = models.AutoField(db_column="TrackId", primary_key=True)
    name = models.CharField(max_length=200, db_column="Name")
    albumid = models.ForeignKey(
        Album, models.DO_NOTHING, db_column="AlbumId", blank=True, null=True
    )
    mediatypeid = models.ForeignKey(
        MediaType, models.DO_NOTHING, db_column="MediaTypeId"
    )
    genre_id = models.ForeignKey(
        Genre, models.DO_NOTHING, db_column="GenreId", blank=True, null=True
    )
    composer = models.CharField(
        max_length=200, db_column="Composer", blank=True, null=True
    )
    milliseconds = models.IntegerField(db_column="Milliseconds")
    bytes = models.IntegerField(db_column="Bytes", blank=True, null=True)
    unitprice = models.CharField(max_length=200, db_column="UnitPrice")

    class Meta:
        managed = False
        db_table = "tracks"
        ordering = ["track_id"]
