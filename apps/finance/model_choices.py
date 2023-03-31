from django.utils.translation import gettext_lazy as _

STATUS_DepIn = 10
STATUS_DepOut = 20
STATUS_Packages = 30
STATUS_SENT_TO_RECIPIENT = 40
STATUS_PercentPackages = 50
STATUS_Referral = 60


REQUEST_STATUSES = (
    (STATUS_DepIn, _('Зачисление Денег')),
    (STATUS_DepOut, _('Списание Вывод')),
    (STATUS_Packages, _('Инвестиционный пакет')),
    (STATUS_PercentPackages, _('Зачисление с Инвест Пакета')),
    (STATUS_Referral, _('Зачисления Реф')),
    )
