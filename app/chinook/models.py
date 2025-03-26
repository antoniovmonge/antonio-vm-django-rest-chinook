from django.db import models


class Album(models.Model):
    album_id = models.AutoField(db_column="AlbumId", primary_key=True)
    title = models.TextField(db_column="Title")
    artistid = models.ForeignKey("Artist", models.DO_NOTHING, db_column="ArtistId")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        managed = False
        db_table = "albums"


class Artist(models.Model):
    artistid = models.AutoField(db_column="ArtistId", primary_key=True)
    name = models.TextField(db_column="Name", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = "artists"


class Customer(models.Model):
    customerid = models.AutoField(db_column="CustomerId", primary_key=True)
    firstname = models.TextField(db_column="FirstName")
    lastname = models.TextField(db_column="LastName")
    company = models.TextField(db_column="Company", blank=True, null=True)
    address = models.TextField(db_column="Address", blank=True, null=True)
    city = models.TextField(db_column="City", blank=True, null=True)
    state = models.TextField(db_column="State", blank=True, null=True)
    country = models.TextField(db_column="Country", blank=True, null=True)
    postalcode = models.TextField(db_column="PostalCode", blank=True, null=True)
    phone = models.TextField(db_column="Phone", blank=True, null=True)
    fax = models.TextField(db_column="Fax", blank=True, null=True)
    email = models.TextField(db_column="Email")
    supportrepid = models.ForeignKey(
        "Employee", models.DO_NOTHING, db_column="SupportRepId", blank=True, null=True
    )

    def __str__(self):
        return f"{self.email}"

    class Meta:
        managed = False
        db_table = "customers"


class Employee(models.Model):
    employeeid = models.AutoField(db_column="EmployeeId", primary_key=True)
    lastname = models.TextField(db_column="LastName")
    firstname = models.TextField(db_column="FirstName")
    title = models.TextField(db_column="Title", blank=True, null=True)
    reportsto = models.ForeignKey(
        "self", models.DO_NOTHING, db_column="ReportsTo", blank=True, null=True
    )
    birthdate = models.DateTimeField(db_column="BirthDate", blank=True, null=True)
    hiredate = models.DateTimeField(db_column="HireDate", blank=True, null=True)
    address = models.TextField(db_column="Address", blank=True, null=True)
    city = models.TextField(db_column="City", blank=True, null=True)
    state = models.TextField(db_column="State", blank=True, null=True)
    country = models.TextField(db_column="Country", blank=True, null=True)
    postalcode = models.TextField(db_column="PostalCode", blank=True, null=True)
    phone = models.TextField(db_column="Phone", blank=True, null=True)
    fax = models.TextField(db_column="Fax", blank=True, null=True)
    email = models.TextField(db_column="Email", blank=True, null=True)

    def __str__(self):
        return f"{self.email}"

    class Meta:
        managed = False
        db_table = "employees"


class Genre(models.Model):
    genreid = models.AutoField(db_column="GenreId", primary_key=True)
    name = models.TextField(db_column="Name", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = "genres"


class InvoiceItem(models.Model):
    invoicelineid = models.AutoField(db_column="InvoiceLineId", primary_key=True)
    invoiceid = models.ForeignKey("Invoice", models.DO_NOTHING, db_column="InvoiceId")
    trackid = models.ForeignKey("Track", models.DO_NOTHING, db_column="TrackId")
    unitprice = models.TextField(db_column="UnitPrice")
    quantity = models.IntegerField(db_column="Quantity")

    class Meta:
        managed = False
        db_table = "invoice_items"


class Invoice(models.Model):
    invoiceid = models.AutoField(db_column="InvoiceId", primary_key=True)
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column="CustomerId")
    invoicedate = models.DateTimeField(db_column="InvoiceDate")
    billingaddress = models.TextField(db_column="BillingAddress", blank=True, null=True)
    billingcity = models.TextField(db_column="BillingCity", blank=True, null=True)
    billingstate = models.TextField(db_column="BillingState", blank=True, null=True)
    billingcountry = models.TextField(db_column="BillingCountry", blank=True, null=True)
    billingpostalcode = models.TextField(
        db_column="BillingPostalCode", blank=True, null=True
    )
    total = models.TextField(db_column="Total")

    class Meta:
        managed = False
        db_table = "invoices"


class MediaType(models.Model):
    mediatypeid = models.AutoField(db_column="MediaTypeId", primary_key=True)
    name = models.TextField(db_column="Name", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = "media_types"


class PlaylistTrack(models.Model):
    playlistid = models.OneToOneField(
        "Playlist", models.DO_NOTHING, db_column="PlaylistId", primary_key=True
    )
    trackid = models.ForeignKey("Track", models.DO_NOTHING, db_column="TrackId")

    class Meta:
        managed = False
        db_table = "playlist_track"


class Playlist(models.Model):
    playlistid = models.AutoField(db_column="PlaylistId", primary_key=True)
    name = models.TextField(db_column="Name", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "playlists"


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)
    idx = models.TextField(blank=True, null=True)
    stat = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sqlite_stat1"


class Track(models.Model):
    trackid = models.AutoField(db_column="TrackId", primary_key=True)
    name = models.TextField(db_column="Name")
    albumid = models.ForeignKey(
        Album, models.DO_NOTHING, db_column="AlbumId", blank=True, null=True
    )
    mediatypeid = models.ForeignKey(
        MediaType, models.DO_NOTHING, db_column="MediaTypeId"
    )
    genreid = models.ForeignKey(
        Genre, models.DO_NOTHING, db_column="GenreId", blank=True, null=True
    )
    composer = models.TextField(db_column="Composer", blank=True, null=True)
    milliseconds = models.IntegerField(db_column="Milliseconds")
    bytes = models.IntegerField(db_column="Bytes", blank=True, null=True)
    unitprice = models.TextField(db_column="UnitPrice")

    class Meta:
        managed = False
        db_table = "tracks"
