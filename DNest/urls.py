from django.urls import path
from DNest import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('widgets/', views.widgets, name='widgets'),
  path('charts/', views.charts, name='charts'),
  path('calendar/', views.calendar, name='calendar'),
  path('template/', views.templates, name='template'),

  # Components
  path('components/buttons/', views.buttons, name='buttons'),
  path('components/grid/', views.grid, name='grid'),
  path('components/panels/', views.panels, name='panels'),
  path('components/sweet-alert/', views.sweet_alert, name='sweet_alert'),
  path('components/notifications/', views.notifications, name='notifications'),
  path('components/icons/', views.icons, name='icons'),
  path('components/typography/', views.typography, name='typography'),

  # Forms
  path('forms/regular-forms/', views.regular_forms, name='regular_forms'),
  path('forms/extended-forms/', views.extended_forms, name='extended_forms'),
  path('forms/validation-forms/', views.validation_forms, name='validation_forms'),
  path('forms/wizard/', views.wizard, name='wizard'),

  # Tables
  path('tables/regular-tables/', views.regular_tables, name='regular_tables'),
  path('tables/extended-tables/', views.extended_tables, name='extended_tables'),
  path('tables/datatables/', views.datatables, name='datatables'),

  # Maps
  path('maps/google-maps/', views.google_maps, name='google_maps'),
  path('maps/fullscreen-map/', views.fullscreen_map, name='fullscreen_map'),
  path('maps/vector-map/', views.vector_map, name='vector_map'),

  # Pages
  path('pages/pricing/', views.pricing, name='pricing'),
  path('pages/timeline/', views.timeline, name='timeline'),
  path('pages/user-profile/', views.user_profile, name='user_profile'),
  path('pages/rtl/', views.rtl, name='rtl'),

  # Authentication
  path('accounts/login/', views.UserLoginView.as_view(), name='login'),
  path('accounts/register/', views.register, name='register'),
  path('accounts/logout/', views.user_logout, name='logout'),

  path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
  path('accounts/password-change-done/', views.UserPasswordChangeDoneView.as_view(), name='password_change_done'),

  path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
  path('accounts/password-reset-confirm/<uidb64>/<token>/',
    views.UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"
  ),
  path('accounts/password-reset-done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
  path('accounts/password-reset-complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

  path('accounts/lock/', views.lock, name='lock'),
]
