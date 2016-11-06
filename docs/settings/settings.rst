

.. _settings:

===================================
The settings
===================================

.. contents::
   :depth: 3


TIME_ZONE
==========

Default: None

A string representing the time zone for datetimes stored in this database 
(assuming that it doesn’t support time zones) or None. 
The same values are accepted as in the general TIME_ZONE setting.

This allows interacting with third-party databases that store datetimes 
in local time rather than UTC. To avoid issues around DST changes, you 
shouldn’t set this option for databases managed by Django.

When USE_TZ is True and the database doesn’t support time zones 
(e.g. SQLite, MySQL, Oracle), Django reads and writes datetimes in local 
time according to this option if it is set and in UTC if it isn’t.

When USE_TZ is True and the database supports time zones (e.g. PostgreSQL), 
it is an error to set this option.

When USE_TZ is False, it is an error to set this option.


.. seealso:: https://docs.djangoproject.com/fr/1.10/ref/settings/#std:setting-TIME_ZONE

Valeur par défaut : 'America/Chicago'

Une chaîne représentant le fuseau horaire pour cette installation, ou 
None. Voir la liste des fuseaux horaires.

Note

Comme Django a été initialement publié avec le réglage TIME_ZONE 
contenant 'America/Chicago', le réglage global (utilisé si aucun n’est 
défini dans le settings.py du projet) reste 'America/Chicago' pour 
garantir la rétrocompatibilité. Les nouveaux gabarits de projet par 
défaut utilisent 'UTC'.

Notez que cela ne correspond pas forcément au fuseau horaire du serveur. 
Par exemple, il est imaginable qu’un site serve plusieurs instances de 
sites Django, chacun ayant leur propre réglage de fuseau horaire.

Lorsque USE_TZ est défini à False, ce réglage définit le fuseau horaire 
avec lequel Django stocke tous les objets dates/heures. 

Lorsque USE_TZ est défini à True, il s’agit alors du fuseau horaire que 
Django utilise par défaut pour afficher les dates/heures dans les 
gabarits et pour interpréter les valeurs dates/heures saisies dans 
les formulaires.

Django définit la variable os.environ['TZ'] au fuseau horaire défini 
dans le réglage TIME_ZONE. Ainsi, toutes les vues et tous les modèles 
opèrent automatiquement dans ce fuseau horaire. Cependant, Django ne 
définit pas la variable d’environnement TZ dans les conditions suivantes :

    si vous utilisez l’option de configuration manuelle telle que 
    décrite dans configuration manuelle des réglages, ou

    si vous indiquez TIME_ZONE = None. Django se synchronise alors 
    sur le fuseau horaire du système. Toutefois, nous décourageons 
    ce cas de figure lorsque USE_TZ = True, parce qu’il fragilise 
    les conversions entre le temps local et le temps UTC.

Quand Django ne définit pas la variable d’environnement TZ, il est de 
votre responsabilité de contrôler que les processus fonctionnent dans 
un environnement correct.

Note

Django ne peut pas utiliser de fuseaux horaires différents du système 
de façon fiable dans un environnement Windows. 
Si vous faites fonctionner Django avec Windows, TIME_ZONE doit être réglé 
sur le même fuseau horaire que le système.


USE_TZ
=======

Default: False

A boolean that specifies if datetimes will be timezone-aware by default 
or not. If this is set to True, Django will use timezone-aware datetimes 
internally. Otherwise, Django will use naive datetimes in local time.

See also TIME_ZONE, USE_I18N and USE_L10N.

Note

The default settings.py file created by django-admin startproject 
includes USE_TZ = True for convenience.


.. seealso:: https://docs.djangoproject.com/fr/1.10/ref/settings/#use-tz

Valeur par défaut : False

Une valeur booléenne indiquant si les dates/heures sont conscientes de 
leur fuseau horaire. Si défini à True, Django utilise en interne des 
dates/heures conscientes de leur fuseau horaire. 
Sinon, Django utilise des dates/heures naïves en temps local.

Voir aussi TIME_ZONE, USE_I18N et USE_L10N.

Note

Le fichier settings.py créé par défaut par django-admin startproject 
définit USE_TZ = True par commodité.


