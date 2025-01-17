from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'history/',
        views.scan_history,
        name="scan_history"),
    path(
        'scheduled/',
        views.scheduled_scan_view,
        name="scheduled_scan_view"),
    path(
        'detail/<int:id>',
        views.detail_scan,
        name='detail_scan'),
    path(
        'all/subdomains',
        views.all_subdomains,
        name='all_subdomains'),
    path(
        'detail/vuln/<int:id>',
        views.detail_vuln_scan,
        name='detail_vuln_scan'),
    path(
        'detail/vuln',
        views.detail_vuln_scan,
        name='all_vulns'),
    path(
        'visualise/<int:id>',
        views.visualise,
        name='visualise'),
    path(
        'detail/all/endpoint',
        views.all_endpoints,
        name='all_endpoints'),
    path(
        'start/<int:domain_id>',
        views.start_scan_ui,
        name='start_scan'),
    path(
        'schedule/target/<int:host_id>',
        views.schedule_scan,
        name='schedule_scan'),
    path(
        'schedule/organization/<int:id>',
        views.schedule_organization_scan,
        name='schedule_organization_scan'),
    path(
        'export/subdomains/<int:scan_id>',
        views.export_subdomains,
        name='export_subdomains'),
    path(
        'export/endpoints/<int:scan_id>',
        views.export_endpoints,
        name='export_endpoints'),
    path(
        'export/urls/<int:scan_id>',
        views.export_urls,
        name='export_http_urls'),
    path(
        'delete/scan/<int:id>',
        views.delete_scan,
        name='delete_scan'),
    path(
        'stop/scan/<str:id>',
        views.stop_scan,
        name='stop_scan'),
    path(
        'delete/scheduled_task/<int:id>',
        views.delete_scheduled_task,
        name='delete_scheduled_task'),
    path(
        'toggle/scheduled_task/<int:id>',
        views.change_scheduled_task_status,
        name='change_scheduled_task_status'),
    path(
        'toggle/vuln_status/<int:id>',
        views.change_vuln_status,
        name='change_vuln_status'),
    path(
        'toggle/subdomain_status/<int:id>',
        views.change_subdomain_status,
        name='change_subdomain_status'),
    path(
        'toggle/subdomain/important/<int:id>',
        views.change_subdomain_important_status,
        name='change_subdomain_important_status'),
    path(
        'start/multiple/',
        views.start_multiple_scan,
        name='start_multiple_scan'),
    path(
        'start/organization/<int:id>',
        views.start_organization_scan,
        name='start_organization_scan'),
    path(
        'delete/scan_results/',
        views.delete_all_scan_results,
        name='delete_all_scan_results'),
    path(
        'delete/screenshots/',
        views.delete_all_screenshots,
        name='delete_all_screenshots'),
]
