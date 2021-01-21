from enum import IntEnum

from django.db import models

#
# class CategoryMaster(models.Model):
#     Name = models.CharField(verbose_name='Category Name', unique=True)
#     CE = models.BooleanField(verbose_name='Construction Equipment', default=False)
#     CV = models.BooleanField(verbose_name='Commercial Vehicle', default=False)
#
#     class Meta:
#         verbose_name_plural = "Asset_Master_Data - Categories"
#
#
# class Model(models.Model):
#     Name = models.CharField(verbose_name='Model Name', unique=True)
#     Category = models.ForeignKey(CategoryMaster, on_delete=models.PROTECT)
#
#     class Meta:
#         verbose_name_plural = "Asset_Master_Data - Models"
#
#
# class GroupMaster(models.Model):
#     Name = models.CharField(verbose_name='Product Group Name', unique=True)
#
#     class Meta:
#         verbose_name_plural = "Product Groups"
#
#
# class BrandsMaster(models.Model):
#     Name = models.CharField(verbose_name='Product Brand Name')
#     ID = models.CharField(verbose_name='Product Brand ID', unique=True)
#     Product_Group = models.ForeignKey(GroupMaster, on_delete=models.PROTECT)
#     Category = models.ForeignKey(CategoryMaster, on_delete=models.PROTECT)
#     # Used = models.BooleanField(default=False)
#     # New = models.BooleanField(default=False)
#
#     # @property
#     # def Both(self):
#     #     if self.Used and self.New:
#     #         return True
#     #     return False
#
#     def __str__(self):
#         return self.Name
#
#     class Meta:
#         verbose_name_plural = "Product Brands"
#
#
# class FieldTypes(IntEnum):
#     Text = 1
#     Numeric = 2
#
#     @classmethod
#     def choices(cls):
#         return [(key.value, key.name) for key in cls]
#
#
# class CategoryTechSpecification(models.Model):
#     Field_Name = models.CharField(verbose_name='Field Name')
#     Field_Type = models.PositiveIntegerField(choices=FieldTypes.choices(), default=FieldTypes.Text)
#     Category = models.ForeignKey(CategoryMaster, on_delete=models.PROTECT)
#     UpdatedAt = models.DateTimeField(auto_now=True)
#     CreatedAt = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name_plural = "CategoryTechSpecifications"
#         unique_together = [['Field_Name', 'Category']]
#
#
# class BrandTechSpecification(models.Model):
#     Field_Name = models.CharField(verbose_name='Field Name')
#     Field_Type = models.PositiveIntegerField(choices=FieldTypes.choices(), default=FieldTypes.Text)
#     Field_Value = models.CharField(verbose_name='Field Value')
#     Category = models.ForeignKey(CategoryMaster, on_delete=models.PROTECT)
#     Brand = models.ForeignKey(BrandsMaster, on_delete=models.PROTECT)
#     Model = models.ForeignKey(Model, on_delete=models.PROTECT)
#     Visible_on_Front = models.BooleanField(default=True)
#     UpdatedAt = models.DateTimeField(auto_now=True)
#     CreatedAt = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name_plural = "CategoryTechSpecifications"
#         unique_together = [['Field_Name', 'Category', 'Brand', 'Model']]
#
#
# class ModelMaster(models.Model):
#     Model_Code = models.CharField(verbose_name='Model Code')
#     Model_Desc = models.TextField(verbose_name='Model Description')
#     Model = models.ForeignKey(Model, on_delete=models.PROTECT)
#     Product_Group = models.ForeignKey(GroupMaster, on_delete=models.PROTECT)
#     Category = models.ForeignKey(CategoryMaster, on_delete=models.PROTECT)
#     Brand = models.ForeignKey(BrandsMaster, on_delete=models.PROTECT)
#     Used = models.BooleanField(default=False)
#     New = models.BooleanField(default=False)
#     Capacity_Group = models.CharField(verbose_name='Capacity Group')
#     Sub_Category = models.CharField(verbose_name='Sub Category')
#     Capacity = models.CharField(verbose_name='Capacity')
#
#
#     @property
#     def Both(self):
#         if self.Used and self.New:
#             return True
#         return False
