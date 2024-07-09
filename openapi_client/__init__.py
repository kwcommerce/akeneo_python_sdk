# coding: utf-8

# flake8: noqa

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.asset_api import AssetApi
from openapi_client.api.asset_attribute_api import AssetAttributeApi
from openapi_client.api.asset_attribute_option_api import AssetAttributeOptionApi
from openapi_client.api.asset_family_api import AssetFamilyApi
from openapi_client.api.asset_media_file_api import AssetMediaFileApi
from openapi_client.api.association_type_api import AssociationTypeApi
from openapi_client.api.attribute_api import AttributeApi
from openapi_client.api.attribute_group_api import AttributeGroupApi
from openapi_client.api.attribute_option_api import AttributeOptionApi
from openapi_client.api.authentication_api import AuthenticationApi
from openapi_client.api.catalog_products_api import CatalogProductsApi
from openapi_client.api.catalogs_api import CatalogsApi
from openapi_client.api.category_api import CategoryApi
from openapi_client.api.channel_api import ChannelApi
from openapi_client.api.currency_api import CurrencyApi
from openapi_client.api.family_api import FamilyApi
from openapi_client.api.family_variant_api import FamilyVariantApi
from openapi_client.api.locale_api import LocaleApi
from openapi_client.api.mapping_schema_for_products_api import MappingSchemaForProductsApi
from openapi_client.api.measure_family_api import MeasureFamilyApi
from openapi_client.api.measurement_family_api import MeasurementFamilyApi
from openapi_client.api.overview_api import OverviewApi
from openapi_client.api.pam_asset_api import PAMAssetApi
from openapi_client.api.pam_asset_category_api import PAMAssetCategoryApi
from openapi_client.api.pam_asset_reference_file_api import PAMAssetReferenceFileApi
from openapi_client.api.pam_asset_tag_api import PAMAssetTagApi
from openapi_client.api.pam_asset_variation_file_api import PAMAssetVariationFileApi
from openapi_client.api.product_identifier_api import ProductIdentifierApi
from openapi_client.api.product_uuid_api import ProductUuidApi
from openapi_client.api.product_media_file_api import ProductMediaFileApi
from openapi_client.api.product_model_api import ProductModelApi
from openapi_client.api.published_product_api import PublishedProductApi
from openapi_client.api.reference_entity_api import ReferenceEntityApi
from openapi_client.api.reference_entity_attribute_api import ReferenceEntityAttributeApi
from openapi_client.api.reference_entity_attribute_option_api import ReferenceEntityAttributeOptionApi
from openapi_client.api.reference_entity_media_file_api import ReferenceEntityMediaFileApi
from openapi_client.api.reference_entity_record_api import ReferenceEntityRecordApi
from openapi_client.api.system_api import SystemApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.app_catalog_list import AppCatalogList
from openapi_client.models.asset import Asset
from openapi_client.models.asset_all_of_embedded import AssetAllOfEmbedded
from openapi_client.models.asset_all_of_embedded_items_inner import AssetAllOfEmbeddedItemsInner
from openapi_client.models.asset_all_of_embedded_items_inner_all_of_values import AssetAllOfEmbeddedItemsInnerAllOfValues
from openapi_client.models.asset_all_of_embedded_items_inner_all_of_values_attribute_code_inner import AssetAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner
from openapi_client.models.asset_families import AssetFamilies
from openapi_client.models.asset_families_all_of_embedded import AssetFamiliesAllOfEmbedded
from openapi_client.models.asset_families_all_of_embedded_items_inner import AssetFamiliesAllOfEmbeddedItemsInner
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_labels import AssetFamiliesAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_naming_convention import AssetFamiliesAllOfEmbeddedItemsInnerAllOfNamingConvention
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_product_link_rules_inner import AssetFamiliesAllOfEmbeddedItemsInnerAllOfProductLinkRulesInner
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_product_link_rules_inner_assign_assets_to_inner import AssetFamiliesAllOfEmbeddedItemsInnerAllOfProductLinkRulesInnerAssignAssetsToInner
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_product_link_rules_inner_product_selections_inner import AssetFamiliesAllOfEmbeddedItemsInnerAllOfProductLinkRulesInnerProductSelectionsInner
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_transformations_inner import AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInner
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_transformations_inner_operations import AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInnerOperations
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_transformations_inner_operations_parameters import AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInnerOperationsParameters
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_transformations_inner_source import AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInnerSource
from openapi_client.models.asset_families_all_of_embedded_items_inner_all_of_transformations_inner_target import AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInnerTarget
from openapi_client.models.asset_family_item_list import AssetFamilyItemList
from openapi_client.models.asset_family_list import AssetFamilyList
from openapi_client.models.asset_family_list_all_of_naming_convention import AssetFamilyListAllOfNamingConvention
from openapi_client.models.asset_item_list import AssetItemList
from openapi_client.models.asset_list import AssetList
from openapi_client.models.asset_list_all_of_values import AssetListAllOfValues
from openapi_client.models.asset_list_all_of_values_attribute_code import AssetListAllOfValuesAttributeCode
from openapi_client.models.association_type import AssociationType
from openapi_client.models.association_type_list import AssociationTypeList
from openapi_client.models.association_types import AssociationTypes
from openapi_client.models.association_types_all_of_embedded import AssociationTypesAllOfEmbedded
from openapi_client.models.association_types_all_of_embedded_items_inner import AssociationTypesAllOfEmbeddedItemsInner
from openapi_client.models.association_types_all_of_embedded_items_inner_all_of_labels import AssociationTypesAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.association_types_post_request import AssociationTypesPostRequest
from openapi_client.models.attribute import Attribute
from openapi_client.models.attribute_group import AttributeGroup
from openapi_client.models.attribute_group_list import AttributeGroupList
from openapi_client.models.attribute_groups import AttributeGroups
from openapi_client.models.attribute_groups_all_of_embedded import AttributeGroupsAllOfEmbedded
from openapi_client.models.attribute_groups_all_of_embedded_items_inner import AttributeGroupsAllOfEmbeddedItemsInner
from openapi_client.models.attribute_groups_all_of_embedded_items_inner_all_of_labels import AttributeGroupsAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.attribute_groups_post_request import AttributeGroupsPostRequest
from openapi_client.models.attribute_list import AttributeList
from openapi_client.models.attribute_option import AttributeOption
from openapi_client.models.attribute_option_list import AttributeOptionList
from openapi_client.models.attribute_options import AttributeOptions
from openapi_client.models.attribute_options_all_of_embedded import AttributeOptionsAllOfEmbedded
from openapi_client.models.attribute_options_all_of_embedded_items_inner import AttributeOptionsAllOfEmbeddedItemsInner
from openapi_client.models.attribute_options_all_of_embedded_items_inner_all_of_labels import AttributeOptionsAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.attributes import Attributes
from openapi_client.models.attributes_all_of_embedded import AttributesAllOfEmbedded
from openapi_client.models.attributes_all_of_embedded_items_inner import AttributesAllOfEmbeddedItemsInner
from openapi_client.models.attributes_all_of_embedded_items_inner_all_of_group_labels import AttributesAllOfEmbeddedItemsInnerAllOfGroupLabels
from openapi_client.models.attributes_all_of_embedded_items_inner_all_of_labels import AttributesAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.attributes_all_of_embedded_items_inner_all_of_table_configuration_inner import AttributesAllOfEmbeddedItemsInnerAllOfTableConfigurationInner
from openapi_client.models.attributes_all_of_embedded_items_inner_all_of_table_configuration_inner_labels import AttributesAllOfEmbeddedItemsInnerAllOfTableConfigurationInnerLabels
from openapi_client.models.attributes_all_of_embedded_items_inner_all_of_table_configuration_inner_validations import AttributesAllOfEmbeddedItemsInnerAllOfTableConfigurationInnerValidations
from openapi_client.models.catalogs import Catalogs
from openapi_client.models.catalogs_all_of_embedded import CatalogsAllOfEmbedded
from openapi_client.models.catalogs_all_of_embedded_items_inner import CatalogsAllOfEmbeddedItemsInner
from openapi_client.models.categories import Categories
from openapi_client.models.categories_all_of_embedded import CategoriesAllOfEmbedded
from openapi_client.models.categories_all_of_embedded_items_inner import CategoriesAllOfEmbeddedItemsInner
from openapi_client.models.categories_all_of_embedded_items_inner_all_of_labels import CategoriesAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.categories_all_of_embedded_items_inner_all_of_values import CategoriesAllOfEmbeddedItemsInnerAllOfValues
from openapi_client.models.categories_all_of_embedded_items_inner_all_of_values_attribute_code_attribute_uuid_channel_code_locale_code_inner import CategoriesAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeAttributeUuidChannelCodeLocaleCodeInner
from openapi_client.models.category import Category
from openapi_client.models.category_list import CategoryList
from openapi_client.models.category_list_all_of_values import CategoryListAllOfValues
from openapi_client.models.category_list_all_of_values_attribute_code_attribute_uuid_channel_code_locale_code import CategoryListAllOfValuesAttributeCodeAttributeUuidChannelCodeLocaleCode
from openapi_client.models.category_update import CategoryUpdate
from openapi_client.models.channel import Channel
from openapi_client.models.channel_list import ChannelList
from openapi_client.models.channels import Channels
from openapi_client.models.channels_all_of_embedded import ChannelsAllOfEmbedded
from openapi_client.models.channels_all_of_embedded_items_inner import ChannelsAllOfEmbeddedItemsInner
from openapi_client.models.channels_all_of_embedded_items_inner_all_of_conversion_units import ChannelsAllOfEmbeddedItemsInnerAllOfConversionUnits
from openapi_client.models.channels_all_of_embedded_items_inner_all_of_labels import ChannelsAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.channels_post_request import ChannelsPostRequest
from openapi_client.models.currencies import Currencies
from openapi_client.models.currencies_all_of_embedded import CurrenciesAllOfEmbedded
from openapi_client.models.currencies_all_of_embedded_items_inner import CurrenciesAllOfEmbeddedItemsInner
from openapi_client.models.currencies_get200_response import CurrenciesGet200Response
from openapi_client.models.currency import Currency
from openapi_client.models.currency_list import CurrencyList
from openapi_client.models.deprecated_asset import DeprecatedAsset
from openapi_client.models.deprecated_asset_category import DeprecatedAssetCategory
from openapi_client.models.deprecated_asset_category_list import DeprecatedAssetCategoryList
from openapi_client.models.deprecated_asset_list import DeprecatedAssetList
from openapi_client.models.deprecated_asset_reference_file import DeprecatedAssetReferenceFile
from openapi_client.models.deprecated_asset_reference_file_upload_warning import DeprecatedAssetReferenceFileUploadWarning
from openapi_client.models.deprecated_asset_tag import DeprecatedAssetTag
from openapi_client.models.deprecated_asset_tag_list import DeprecatedAssetTagList
from openapi_client.models.deprecated_asset_variation_file import DeprecatedAssetVariationFile
from openapi_client.models.error import Error
from openapi_client.models.error_by_line import ErrorByLine
from openapi_client.models.error_by_line_product_uuid import ErrorByLineProductUuid
from openapi_client.models.families import Families
from openapi_client.models.families_all_of_embedded import FamiliesAllOfEmbedded
from openapi_client.models.families_all_of_embedded_items_inner import FamiliesAllOfEmbeddedItemsInner
from openapi_client.models.families_all_of_embedded_items_inner_all_of_attribute_requirements import FamiliesAllOfEmbeddedItemsInnerAllOfAttributeRequirements
from openapi_client.models.families_all_of_embedded_items_inner_all_of_labels import FamiliesAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.family import Family
from openapi_client.models.family_list import FamilyList
from openapi_client.models.family_variant import FamilyVariant
from openapi_client.models.family_variant_list import FamilyVariantList
from openapi_client.models.family_variants import FamilyVariants
from openapi_client.models.family_variants_all_of_embedded import FamilyVariantsAllOfEmbedded
from openapi_client.models.family_variants_all_of_embedded_items_inner import FamilyVariantsAllOfEmbeddedItemsInner
from openapi_client.models.family_variants_all_of_embedded_items_inner_all_of_labels import FamilyVariantsAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.family_variants_all_of_embedded_items_inner_all_of_variant_attribute_sets_inner import FamilyVariantsAllOfEmbeddedItemsInnerAllOfVariantAttributeSetsInner
from openapi_client.models.get_app_catalogs_mapping_schema_product200_response import GetAppCatalogsMappingSchemaProduct200Response
from openapi_client.models.get_asset_families_code_attributes200_response_inner import GetAssetFamiliesCodeAttributes200ResponseInner
from openapi_client.models.get_asset_family_attributes_attribute_code_options200_response_inner import GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner
from openapi_client.models.get_asset_family_code200_response import GetAssetFamilyCode200Response
from openapi_client.models.get_asset_tags_code200_response import GetAssetTagsCode200Response
from openapi_client.models.get_assets_code200_response import GetAssetsCode200Response
from openapi_client.models.get_categories_code200_response import GetCategoriesCode200Response
from openapi_client.models.get_endpoints200_response import GetEndpoints200Response
from openapi_client.models.get_locales_code200_response import GetLocalesCode200Response
from openapi_client.models.get_media_files_code200_response import GetMediaFilesCode200Response
from openapi_client.models.get_media_files_code200_response_all_of_links import GetMediaFilesCode200ResponseAllOfLinks
from openapi_client.models.get_products_uuid401_response import GetProductsUuid401Response
from openapi_client.models.get_published_products_code200_response import GetPublishedProductsCode200Response
from openapi_client.models.get_reference_entities_code200_response import GetReferenceEntitiesCode200Response
from openapi_client.models.get_reference_entities_code200_response_all_of_links import GetReferenceEntitiesCode200ResponseAllOfLinks
from openapi_client.models.get_reference_entities_code_attributes200_response_inner import GetReferenceEntitiesCodeAttributes200ResponseInner
from openapi_client.models.get_reference_entity_attributes_attribute_code_options200_response_inner import GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner
from openapi_client.models.get_reference_entity_attributes_code200_response import GetReferenceEntityAttributesCode200Response
from openapi_client.models.get_reference_entity_records_code200_response import GetReferenceEntityRecordsCode200Response
from openapi_client.models.get_reference_files_locale_code200_response import GetReferenceFilesLocaleCode200Response
from openapi_client.models.get_reference_files_locale_code200_response_link import GetReferenceFilesLocaleCode200ResponseLink
from openapi_client.models.get_system_information200_response import GetSystemInformation200Response
from openapi_client.models.get_variation_files_channel_code_locale_code200_response import GetVariationFilesChannelCodeLocaleCode200Response
from openapi_client.models.get_variation_files_channel_code_locale_code200_response_link import GetVariationFilesChannelCodeLocaleCode200ResponseLink
from openapi_client.models.item_list import ItemList
from openapi_client.models.locale import Locale
from openapi_client.models.locale_list import LocaleList
from openapi_client.models.locales import Locales
from openapi_client.models.locales_all_of_embedded import LocalesAllOfEmbedded
from openapi_client.models.locales_all_of_embedded_items_inner import LocalesAllOfEmbeddedItemsInner
from openapi_client.models.measure_families import MeasureFamilies
from openapi_client.models.measure_families_all_of_embedded import MeasureFamiliesAllOfEmbedded
from openapi_client.models.measure_families_all_of_embedded_items_inner import MeasureFamiliesAllOfEmbeddedItemsInner
from openapi_client.models.measure_families_all_of_embedded_items_inner_all_of_units_inner import MeasureFamiliesAllOfEmbeddedItemsInnerAllOfUnitsInner
from openapi_client.models.measure_families_get200_response import MeasureFamiliesGet200Response
from openapi_client.models.measure_family import MeasureFamily
from openapi_client.models.measure_family_list import MeasureFamilyList
from openapi_client.models.measure_family_list_all_of_units import MeasureFamilyListAllOfUnits
from openapi_client.models.measurement_families_get_list200_response import MeasurementFamiliesGetList200Response
from openapi_client.models.measurement_families_get_list200_response_labels import MeasurementFamiliesGetList200ResponseLabels
from openapi_client.models.measurement_families_get_list200_response_units import MeasurementFamiliesGetList200ResponseUnits
from openapi_client.models.measurement_families_get_list200_response_units_unit_code import MeasurementFamiliesGetList200ResponseUnitsUnitCode
from openapi_client.models.measurement_families_get_list200_response_units_unit_code_convert_from_standard_inner import MeasurementFamiliesGetList200ResponseUnitsUnitCodeConvertFromStandardInner
from openapi_client.models.measurement_families_get_list200_response_units_unit_code_labels import MeasurementFamiliesGetList200ResponseUnitsUnitCodeLabels
from openapi_client.models.measurement_family import MeasurementFamily
from openapi_client.models.measurement_family_list import MeasurementFamilyList
from openapi_client.models.media_file import MediaFile
from openapi_client.models.media_file_item_list import MediaFileItemList
from openapi_client.models.media_file_list import MediaFileList
from openapi_client.models.media_files import MediaFiles
from openapi_client.models.media_files_all_of_embedded import MediaFilesAllOfEmbedded
from openapi_client.models.media_files_all_of_embedded_items_inner import MediaFilesAllOfEmbeddedItemsInner
from openapi_client.models.media_files_all_of_embedded_items_inner_all_of_links import MediaFilesAllOfEmbeddedItemsInnerAllOfLinks
from openapi_client.models.media_files_all_of_embedded_items_inner_all_of_links_download import MediaFilesAllOfEmbeddedItemsInnerAllOfLinksDownload
from openapi_client.models.media_files_all_of_embedded_items_inner_all_of_links_self import MediaFilesAllOfEmbeddedItemsInnerAllOfLinksSelf
from openapi_client.models.pam_asset_categories import PAMAssetCategories
from openapi_client.models.pam_asset_categories_all_of_embedded import PAMAssetCategoriesAllOfEmbedded
from openapi_client.models.pam_asset_categories_all_of_embedded_items_inner import PAMAssetCategoriesAllOfEmbeddedItemsInner
from openapi_client.models.pam_asset_categories_all_of_embedded_items_inner_all_of_labels import PAMAssetCategoriesAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.pam_asset_tags import PAMAssetTags
from openapi_client.models.pam_asset_tags_all_of_embedded import PAMAssetTagsAllOfEmbedded
from openapi_client.models.pam_asset_tags_all_of_embedded_items_inner import PAMAssetTagsAllOfEmbeddedItemsInner
from openapi_client.models.pam_assets import PAMAssets
from openapi_client.models.pam_assets_all_of_embedded import PAMAssetsAllOfEmbedded
from openapi_client.models.pam_assets_all_of_embedded_items_inner import PAMAssetsAllOfEmbeddedItemsInner
from openapi_client.models.pam_assets_all_of_embedded_items_inner_all_of_reference_files_inner import PAMAssetsAllOfEmbeddedItemsInnerAllOfReferenceFilesInner
from openapi_client.models.pam_assets_all_of_embedded_items_inner_all_of_reference_files_inner_link import PAMAssetsAllOfEmbeddedItemsInnerAllOfReferenceFilesInnerLink
from openapi_client.models.pam_assets_all_of_embedded_items_inner_all_of_reference_files_inner_link_download import PAMAssetsAllOfEmbeddedItemsInnerAllOfReferenceFilesInnerLinkDownload
from openapi_client.models.pam_assets_all_of_embedded_items_inner_all_of_reference_files_inner_link_self import PAMAssetsAllOfEmbeddedItemsInnerAllOfReferenceFilesInnerLinkSelf
from openapi_client.models.pam_assets_all_of_embedded_items_inner_all_of_variation_files_inner import PAMAssetsAllOfEmbeddedItemsInnerAllOfVariationFilesInner
from openapi_client.models.pam_assets_all_of_embedded_items_inner_all_of_variation_files_inner_link import PAMAssetsAllOfEmbeddedItemsInnerAllOfVariationFilesInnerLink
from openapi_client.models.pam_assets_all_of_embedded_items_inner_all_of_variation_files_inner_link_download import PAMAssetsAllOfEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload
from openapi_client.models.pam_assets_all_of_embedded_items_inner_all_of_variation_files_inner_link_self import PAMAssetsAllOfEmbeddedItemsInnerAllOfVariationFilesInnerLinkSelf
from openapi_client.models.pagination import Pagination
from openapi_client.models.patch_asset_categories_request import PatchAssetCategoriesRequest
from openapi_client.models.patch_assets_request_inner import PatchAssetsRequestInner
from openapi_client.models.patch_attributes_attribute_code_options_request import PatchAttributesAttributeCodeOptionsRequest
from openapi_client.models.patch_attributes_request import PatchAttributesRequest
from openapi_client.models.patch_categories_request import PatchCategoriesRequest
from openapi_client.models.patch_families_family_code_variants_request import PatchFamiliesFamilyCodeVariantsRequest
from openapi_client.models.patch_families_request import PatchFamiliesRequest
from openapi_client.models.patch_measurement_families200_response_inner import PatchMeasurementFamilies200ResponseInner
from openapi_client.models.patch_measurement_families200_response_inner_errors_inner import PatchMeasurementFamilies200ResponseInnerErrorsInner
from openapi_client.models.patch_pam_assets_request import PatchPamAssetsRequest
from openapi_client.models.patch_product_models_request import PatchProductModelsRequest
from openapi_client.models.patch_products200_response import PatchProducts200Response
from openapi_client.models.patch_products_request import PatchProductsRequest
from openapi_client.models.patch_products_uuid200_response import PatchProductsUuid200Response
from openapi_client.models.patch_products_uuid_request import PatchProductsUuidRequest
from openapi_client.models.patch_reference_entity_code_request import PatchReferenceEntityCodeRequest
from openapi_client.models.patch_reference_entity_records200_response_inner import PatchReferenceEntityRecords200ResponseInner
from openapi_client.models.patch_reference_entity_records_code_request import PatchReferenceEntityRecordsCodeRequest
from openapi_client.models.patch_reference_entity_records_request_inner import PatchReferenceEntityRecordsRequestInner
from openapi_client.models.post_app_catalog201_response import PostAppCatalog201Response
from openapi_client.models.post_app_catalog_request import PostAppCatalogRequest
from openapi_client.models.post_asset_categories_request import PostAssetCategoriesRequest
from openapi_client.models.post_attributes_attribute_code_options_request import PostAttributesAttributeCodeOptionsRequest
from openapi_client.models.post_attributes_request import PostAttributesRequest
from openapi_client.models.post_categories_request import PostCategoriesRequest
from openapi_client.models.post_categories_request_values_inner import PostCategoriesRequestValuesInner
from openapi_client.models.post_category_media_files_request import PostCategoryMediaFilesRequest
from openapi_client.models.post_families_family_code_variants_request import PostFamiliesFamilyCodeVariantsRequest
from openapi_client.models.post_families_request import PostFamiliesRequest
from openapi_client.models.post_media_files_request import PostMediaFilesRequest
from openapi_client.models.post_pam_assets_request import PostPamAssetsRequest
from openapi_client.models.post_product_models_request import PostProductModelsRequest
from openapi_client.models.post_products_request import PostProductsRequest
from openapi_client.models.post_products_uuid_request import PostProductsUuidRequest
from openapi_client.models.post_reference_entity_media_files_request import PostReferenceEntityMediaFilesRequest
from openapi_client.models.post_reference_files_locale_code201_response import PostReferenceFilesLocaleCode201Response
from openapi_client.models.post_reference_files_locale_code201_response_errors_inner import PostReferenceFilesLocaleCode201ResponseErrorsInner
from openapi_client.models.post_reference_files_locale_code_request import PostReferenceFilesLocaleCodeRequest
from openapi_client.models.post_token200_response import PostToken200Response
from openapi_client.models.post_token_request import PostTokenRequest
from openapi_client.models.product import Product
from openapi_client.models.product_list import ProductList
from openapi_client.models.product_list_all_of_values import ProductListAllOfValues
from openapi_client.models.product_list_all_of_values_attribute_code import ProductListAllOfValuesAttributeCode
from openapi_client.models.product_list_all_of_values_linked_data import ProductListAllOfValuesLinkedData
from openapi_client.models.product_model import ProductModel
from openapi_client.models.product_model_list import ProductModelList
from openapi_client.models.product_model_list_all_of_values import ProductModelListAllOfValues
from openapi_client.models.product_model_list_all_of_values_attribute_code import ProductModelListAllOfValuesAttributeCode
from openapi_client.models.product_model_list_all_of_values_linked_data import ProductModelListAllOfValuesLinkedData
from openapi_client.models.product_models import ProductModels
from openapi_client.models.product_models_all_of_embedded import ProductModelsAllOfEmbedded
from openapi_client.models.product_models_all_of_embedded_items_inner import ProductModelsAllOfEmbeddedItemsInner
from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_associations import ProductModelsAllOfEmbeddedItemsInnerAllOfAssociations
from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_metadata import ProductModelsAllOfEmbeddedItemsInnerAllOfMetadata
from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_quantified_associations import ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociations
from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code import ProductModelsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode
from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_values import ProductModelsAllOfEmbeddedItemsInnerAllOfValues
from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_values_attribute_code_inner import ProductModelsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner
from openapi_client.models.product_models_all_of_embedded_items_inner_all_of_values_attribute_code_inner_linked_data import ProductModelsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInnerLinkedData
from openapi_client.models.product_uuid import ProductUuid
from openapi_client.models.product_uuid_list import ProductUuidList
from openapi_client.models.product_uuids import ProductUuids
from openapi_client.models.product_uuids_all_of_embedded import ProductUuidsAllOfEmbedded
from openapi_client.models.products import Products
from openapi_client.models.products1 import Products1
from openapi_client.models.products1_all_of_embedded import Products1AllOfEmbedded
from openapi_client.models.products1_all_of_embedded_items_inner import Products1AllOfEmbeddedItemsInner
from openapi_client.models.products1_all_of_embedded_items_inner_all_of_associations import Products1AllOfEmbeddedItemsInnerAllOfAssociations
from openapi_client.models.products1_all_of_embedded_items_inner_all_of_associations_association_type_code import Products1AllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode
from openapi_client.models.products1_all_of_embedded_items_inner_all_of_quantified_associations import Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociations
from openapi_client.models.products1_all_of_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code import Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode
from openapi_client.models.products1_all_of_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_products_inner import Products1AllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner
from openapi_client.models.products2 import Products2
from openapi_client.models.products_all_of_embedded import ProductsAllOfEmbedded
from openapi_client.models.products_all_of_embedded_items_inner import ProductsAllOfEmbeddedItemsInner
from openapi_client.models.products_all_of_embedded_items_inner_all_of_associations import ProductsAllOfEmbeddedItemsInnerAllOfAssociations
from openapi_client.models.products_all_of_embedded_items_inner_all_of_associations_association_type_code import ProductsAllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode
from openapi_client.models.products_all_of_embedded_items_inner_all_of_completenesses_inner import ProductsAllOfEmbeddedItemsInnerAllOfCompletenessesInner
from openapi_client.models.products_all_of_embedded_items_inner_all_of_links import ProductsAllOfEmbeddedItemsInnerAllOfLinks
from openapi_client.models.products_all_of_embedded_items_inner_all_of_links_self import ProductsAllOfEmbeddedItemsInnerAllOfLinksSelf
from openapi_client.models.products_all_of_embedded_items_inner_all_of_metadata import ProductsAllOfEmbeddedItemsInnerAllOfMetadata
from openapi_client.models.products_all_of_embedded_items_inner_all_of_quantified_associations import ProductsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociations
from openapi_client.models.products_all_of_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code import ProductsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode
from openapi_client.models.products_all_of_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_product_models_inner import ProductsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCodeProductModelsInner
from openapi_client.models.products_all_of_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_products_inner import ProductsAllOfEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner
from openapi_client.models.products_all_of_embedded_items_inner_all_of_values import ProductsAllOfEmbeddedItemsInnerAllOfValues
from openapi_client.models.products_all_of_embedded_items_inner_all_of_values_attribute_code_inner import ProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner
from openapi_client.models.products_all_of_embedded_items_inner_all_of_values_attribute_code_inner_linked_data import ProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInnerLinkedData
from openapi_client.models.products_all_of_links import ProductsAllOfLinks
from openapi_client.models.products_all_of_links_first import ProductsAllOfLinksFirst
from openapi_client.models.products_all_of_links_next import ProductsAllOfLinksNext
from openapi_client.models.products_all_of_links_previous import ProductsAllOfLinksPrevious
from openapi_client.models.products_all_of_links_self import ProductsAllOfLinksSelf
from openapi_client.models.published_product import PublishedProduct
from openapi_client.models.published_product_list import PublishedProductList
from openapi_client.models.published_product_list_all_of_values import PublishedProductListAllOfValues
from openapi_client.models.published_product_list_all_of_values_attribute_code import PublishedProductListAllOfValuesAttributeCode
from openapi_client.models.published_products import PublishedProducts
from openapi_client.models.published_products_all_of_embedded import PublishedProductsAllOfEmbedded
from openapi_client.models.published_products_all_of_embedded_items_inner import PublishedProductsAllOfEmbeddedItemsInner
from openapi_client.models.published_products_all_of_embedded_items_inner_all_of_associations import PublishedProductsAllOfEmbeddedItemsInnerAllOfAssociations
from openapi_client.models.published_products_all_of_embedded_items_inner_all_of_associations_association_type_code import PublishedProductsAllOfEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode
from openapi_client.models.published_products_all_of_embedded_items_inner_all_of_values import PublishedProductsAllOfEmbeddedItemsInnerAllOfValues
from openapi_client.models.published_products_all_of_embedded_items_inner_all_of_values_attribute_code_inner import PublishedProductsAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner
from openapi_client.models.reference_entities import ReferenceEntities
from openapi_client.models.reference_entities_all_of_embedded import ReferenceEntitiesAllOfEmbedded
from openapi_client.models.reference_entities_all_of_embedded_items_inner import ReferenceEntitiesAllOfEmbeddedItemsInner
from openapi_client.models.reference_entities_all_of_embedded_items_inner_all_of_labels import ReferenceEntitiesAllOfEmbeddedItemsInnerAllOfLabels
from openapi_client.models.reference_entities_all_of_embedded_items_inner_all_of_links import ReferenceEntitiesAllOfEmbeddedItemsInnerAllOfLinks
from openapi_client.models.reference_entities_all_of_embedded_items_inner_all_of_links_image_download import ReferenceEntitiesAllOfEmbeddedItemsInnerAllOfLinksImageDownload
from openapi_client.models.reference_entities_all_of_links import ReferenceEntitiesAllOfLinks
from openapi_client.models.reference_entity import ReferenceEntity
from openapi_client.models.reference_entity_attribute import ReferenceEntityAttribute
from openapi_client.models.reference_entity_attribute_option import ReferenceEntityAttributeOption
from openapi_client.models.reference_entity_item_list import ReferenceEntityItemList
from openapi_client.models.reference_entity_list import ReferenceEntityList
from openapi_client.models.reference_entity_record import ReferenceEntityRecord
from openapi_client.models.reference_entity_record_all_of_embedded import ReferenceEntityRecordAllOfEmbedded
from openapi_client.models.reference_entity_record_all_of_embedded_items_inner import ReferenceEntityRecordAllOfEmbeddedItemsInner
from openapi_client.models.reference_entity_record_all_of_embedded_items_inner_all_of_values import ReferenceEntityRecordAllOfEmbeddedItemsInnerAllOfValues
from openapi_client.models.reference_entity_record_all_of_embedded_items_inner_all_of_values_attribute_code_inner import ReferenceEntityRecordAllOfEmbeddedItemsInnerAllOfValuesAttributeCodeInner
from openapi_client.models.reference_entity_record_item_list import ReferenceEntityRecordItemList
from openapi_client.models.reference_entity_record_list import ReferenceEntityRecordList
from openapi_client.models.reference_entity_record_list_all_of_values import ReferenceEntityRecordListAllOfValues
from openapi_client.models.reference_entity_record_list_all_of_values_attribute_code import ReferenceEntityRecordListAllOfValuesAttributeCode
from openapi_client.models.search_after_pagination import SearchAfterPagination
from openapi_client.models.several_association_types_patch_request import SeveralAssociationTypesPatchRequest
from openapi_client.models.several_attribute_groups_patch_request import SeveralAttributeGroupsPatchRequest
from openapi_client.models.several_channels_patch_request import SeveralChannelsPatchRequest