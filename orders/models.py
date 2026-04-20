from django.db import models

class Order(models.Model):
    sales_order_number = models.CharField(max_length=100)
    sold_to_name = models.CharField(max_length=255)
    ship_to_name = models.CharField(max_length=255)

    production_block = models.CharField(max_length=100)
    block_type = models.CharField(max_length=100, blank=True)

    document_cutoff_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.sales_order_number
    

class OrderNote(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='notes')
    note_date = models.DateTimeField()
    note_text = models.TextField()

    def __str__(self):
        return f"{self.order.sales_order_number} - {self.note_date}"