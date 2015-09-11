from django.conf.urls import url, patterns

from ..views import (
    OptionGroupDetailView,
    OptionGroupListView,
    FacilityStatusListView,
    FacilityStatusDetailView,
    JobTitleListView,
    JobTitleDetailView,
    OfficerListView,
    OfficerDetailView,
    RegulatingBodyListView,
    RegulatingBodyDetailView,
    OwnerTypeListView,
    OwnerTypeDetailView,
    OfficerContactListView,
    OfficerContactDetailView,
    OwnerListView,
    OwnerDetailView,
    FacilityListView,
    FacilityDetailView,
    FacilityContactListView,
    FacilityContactDetailView,
    FacilityRegulationStatusListView,
    FacilityRegulationStatusDetailView,
    FacilityTypeListView,
    FacilityTypeDetailView,
    RegulationStatusListView,
    RegulationStatusDetailView,
    FacilityUnitsListView,
    FacilityUnitDetailView,
    ServiceCategoryListView,
    ServiceCategoryDetailView,
    OptionListView,
    OptionDetailView,
    ServiceListView,
    ServiceDetailView,
    FacilityServiceListView,
    FacilityServiceDetailView,
    FacilityApprovalListView,
    FacilityApprovalDetailView,
    FacilityOperationStateListView,
    FacilityOperationStateDetailView,
    FacilityUpgradeListView,
    FacilityUpgradeDetailView,
    FacilityServiceRatingDetailView,
    FacilityServiceRatingListView,
    FacilityCoverTemplate,
    FacilityInspectionReport,
    RegulatingBodyContactListView,
    RegulatingBodyContactDetailView,
    FacilityCorrectionTemplate,
    DashBoard,
    FacilityListReadOnlyView,
    FacilityOfficerDetailView,
    FacilityOfficerListView,
    RegulatoryBodyUserListView,
    RegulatoryBodyUserDetailView,
    FacilityUnitRegulationListView,
    FacilityUnitRegulationDetailView,
    FacilityUpdatesListView,
    FacilityUpdatesDetailView,
    CustomFacilityOfficerView,
    KephLevelListView,
    KephLevelDetailView,
    FacilityLevelChangeReasonDetailView,
    FacilityLevelChangeReasonListView,
    PostOptionGroupWithOptionsView,
    FacilityDepartmentDetailView,
    FacilityDepartmentListView
)


urlpatterns = patterns(
    '',
    url(r'^option_group_with_options/$',
        PostOptionGroupWithOptionsView.as_view(),
        name='post_option_group_with_options'),

    url(r'^option_group_with_options/(?P<pk>[^/]+)/$',
        PostOptionGroupWithOptionsView.as_view(),
        name='delete_option_group_with_options'),

    url(r'^level_change_reasons/$',
        FacilityLevelChangeReasonListView.as_view(),
        name='facility_level_change_reasons_list'),
    url(r'^level_change_reasons/(?P<pk>[^/]+)/$',
        FacilityLevelChangeReasonDetailView.as_view(),
        name='facility_level_change_reason_detail'),

    url(r'^keph/$', KephLevelListView.as_view(),
        name='keph_levels_list'),
    url(r'^keph/(?P<pk>[^/]+)/$',
        KephLevelDetailView.as_view(),
        name='keph_level_detail'),

    url(r'^officer_facade/$',
        CustomFacilityOfficerView.as_view(),
        name='officer_facade_create'),

    url(r'^officer_facade/(?P<facility_id>[^/]+)/$',
        CustomFacilityOfficerView.as_view(),
        name='officer_facade_list'),

    url(r'^officer_facade/delete/(?P<pk>[^/]+)/$',
        CustomFacilityOfficerView.as_view(),
        name='officer_facade_delete'),

    url(r'^facility_updates/$',
        FacilityUpdatesListView.as_view(),
        name='facility_updatess_list'),
    url(r'^facility_updates/(?P<pk>[^/]+)/$',
        FacilityUpdatesDetailView.as_view(),
        name='facility_updates_detail'),

    url(r'^facility_unit_regulation/$',
        FacilityUnitRegulationListView.as_view(),
        name='facility_unit_regulations_list'),
    url(r'^facility_unit_regulation/(?P<pk>[^/]+)/$',
        FacilityUnitRegulationDetailView.as_view(),
        name='facility_unit_regulation_detail'),

    url(r'^regulatory_body_users/$', RegulatoryBodyUserListView.as_view(),
        name='regulatory_body_users_list'),
    url(r'^regulatory_body_users/(?P<pk>[^/]+)/$',
        RegulatoryBodyUserDetailView.as_view(),
        name='regulatory_body_user_detail'),

    url(r'^facility_officers/$', FacilityOfficerListView.as_view(),
        name='facility_officers_list'),
    url(r'^facility_officers/(?P<pk>[^/]+)/$',
        FacilityOfficerDetailView.as_view(),
        name='facility_officer_detail'),

    url(r'^dashboard/$', DashBoard.as_view(),
        name='dashboard'),

    url(r'^facility_correction_template/(?P<facility_id>[^/]+)/$',
        FacilityCorrectionTemplate.as_view(),
        name='facility_correction_template'),

    url(r'^facility_inspection_report/(?P<facility_id>[^/]+)/$',
        FacilityInspectionReport.as_view(),
        name='facility_inspection_report'),

    url(r'^facility_cover_report/(?P<facility_id>[^/]+)/$',
        FacilityCoverTemplate.as_view(),
        name='facility_cover_report'),

    url(r'^regulating_body_contacts/$',
        RegulatingBodyContactListView.as_view(),
        name='regulating_body_contacts_list'),
    url(r'^regulating_body_contacts/(?P<pk>[^/]+)/$',
        RegulatingBodyContactDetailView.as_view(),
        name='regulating_body_contact_detail'),

    url(r'^facility_upgrade/$',
        FacilityUpgradeListView.as_view(),
        name='facility_upgrades_list'),
    url(r'^facility_upgrade/(?P<pk>[^/]+)/$',
        FacilityUpgradeDetailView.as_view(),
        name='facility_upgrade_detail'),

    url(r'^facility_operation_state/$',
        FacilityOperationStateListView.as_view(),
        name='facility_operation_states_list'),
    url(r'^facility_operation_state/(?P<pk>[^/]+)/$',
        FacilityOperationStateDetailView.as_view(),
        name='facility_operation_state_detail'),

    url(r'^facility_approvals/$', FacilityApprovalListView.as_view(),
        name='facility_approvals_list'),
    url(r'^facility_approvals/(?P<pk>[^/]+)/$',
        FacilityApprovalDetailView.as_view(),
        name='facility_approval_detail'),

    url(r'^facility_service_ratings/$',
        FacilityServiceRatingListView.as_view(),
        name='facility_service_ratings_list'),
    url(r'^facility_service_ratings/(?P<pk>[^/]+)/$',
        FacilityServiceRatingDetailView.as_view(),
        name='facility_service_rating_detail'),

    url(r'^service_categories/$', ServiceCategoryListView.as_view(),
        name='service_categories_list'),
    url(r'^service_categories/(?P<pk>[^/]+)/$',
        ServiceCategoryDetailView.as_view(),
        name='service_category_detail'),

    url(r'^services/$', ServiceListView.as_view(),
        name='services_list'),
    url(r'^services/(?P<pk>[^/]+)/$', ServiceDetailView.as_view(),
        name='service_detail'),

    url(r'^options/$', OptionListView.as_view(),
        name='options_list'),
    url(r'^options/(?P<pk>[^/]+)/$', OptionDetailView.as_view(),
        name='option_detail'),

    url(r'^facility_services/$', FacilityServiceListView.as_view(),
        name='facility_services_list'),
    url(r'^facility_services/(?P<pk>[^/]+)/$',
        FacilityServiceDetailView.as_view(),
        name='facility_service_detail'),

    url(r'^facility_units/$', FacilityUnitsListView.as_view(),
        name='facility_units_list'),
    url(r'^facility_units/(?P<pk>[^/]+)/$', FacilityUnitDetailView.as_view(),
        name='facility_unit_detail'),

    url(r'^regulating_bodies/$', RegulatingBodyListView.as_view(),
        name='regulating_bodies_list'),
    url(r'^regulating_bodies/(?P<pk>[^/]+)/$',
        RegulatingBodyDetailView.as_view(),
        name='regulating_body_detail'),

    url(r'^facility_types/$', FacilityTypeListView.as_view(),
        name='facility_types_list'),
    url(r'^facility_types/(?P<pk>[^/]+)/$', FacilityTypeDetailView.as_view(),
        name='facility_type_detail'),

    url(r'^facility_status/$', FacilityStatusListView.as_view(),
        name='facility_statuses_list'),
    url(r'^facility_status/(?P<pk>[^/]+)/$',
        FacilityStatusDetailView.as_view(),
        name='facility_status_detail'),

    url(r'^officer_contacts/$', OfficerContactListView.as_view(),
        name='officer_contacts_list'),
    url(r'^officer_contacts/(?P<pk>[^/]+)/$',
        OfficerContactDetailView.as_view(),
        name='officer_contact_detail'),

    url(r'^job_titles/$', JobTitleListView.as_view(),
        name='job_titles_list'),
    url(r'^job_titles/(?P<pk>[^/]+)/$', JobTitleDetailView.as_view(),
        name='job_title_detail'),

    url(r'^facility_regulation_status/$',
        FacilityRegulationStatusListView.as_view(),
        name='facility_regulation_statuses_list'),
    url(r'^facility_regulation_status/(?P<pk>[^/]+)/$',
        FacilityRegulationStatusDetailView.as_view(),
        name='facility_regulation_status_detail'),

    url(r'^regulation_status/$', RegulationStatusListView.as_view(),
        name='regulation_statuses_list'),
    url(r'^regulation_status/(?P<pk>[^/]+)/$',
        RegulationStatusDetailView.as_view(),
        name='regulation_status_detail'),

    url(r'^officers/$', OfficerListView.as_view(),
        name='officers_in_charge_list'),
    url(r'^officers_incharge/(?P<pk>[^/]+)/$',
        OfficerDetailView.as_view(),
        name='officer_detail'),

    url(r'^owner_types/$', OwnerTypeListView.as_view(),
        name='owner_types_list'),
    url(r'^owner_types/(?P<pk>[^/]+)/$', OwnerTypeDetailView.as_view(),
        name='owner_type_detail'),

    url(r'^owners/$', OwnerListView.as_view(), name='owners_list'),
    url(r'^owners/(?P<pk>[^/]+)/$', OwnerDetailView.as_view(),
        name='owner_detail'),

    url(r'^contacts/$', FacilityContactListView .as_view(),
        name='facility_contacts_list'),
    url(r'^contacts/(?P<pk>[^/]+)/$', FacilityContactDetailView.as_view(),
        name='facility_contact_detail'),

    url(r'^facilities_list/$', FacilityListReadOnlyView.as_view(),
        name='facilities_read_list'),
    url(r'^facilities/$', FacilityListView.as_view(), name='facilities_list'),
    url(r'^facilities/(?P<pk>[^/]+)/$', FacilityDetailView.as_view(),
        name='facility_detail'),

    url(r'^option_groups/$',
        OptionGroupListView.as_view(),
        name='option_groups_list'),
    url(r'^option_groups/(?P<pk>[^/]+)/$', OptionGroupDetailView.as_view(),
        name='option_group_detail'),


    url(
        r'^facility_depts/$',
        FacilityDepartmentListView.as_view(), name='facility_depts_list'
    ),
    url(
        r'^facility_depts/(?P<pk>[^/]+)/$',
        FacilityDepartmentDetailView.as_view(), name='facility_depts_detail'
    ),
)
