



=============
Requirements
=============

.. contents::
   :depth: 3


pip install django
===================

.. seealso::

   - https://docs.djangoproject.com/en/dev/intro/install/
   

::

    pip install django
    
::

	Downloading/unpacking django
	  Downloading Django-1.10.3-py2.py3-none-any.whl (6.8MB): 6.8MB downloaded
	Installing collected packages: django
	Successfully installed django
	Cleaning up...
		
python -m django --version
---------------------------

::

    (django_test_dates)assr38@vercors:~/Documents/django_test_dates$ python -m django --version
    
::
    
    1.10.3



pip install pendulum
=====================

::
		
    (django_test_dates) $ pip install pendulum
    
::
    
	Collecting pendulum
	  Downloading pendulum-0.6.5-cp35-cp35m-manylinux1_i686.whl (92kB)
		100% |████████████████████████████████| 102kB 1.6MB/s 
	Collecting python-dateutil (from pendulum)
	  Using cached python_dateutil-2.5.3-py2.py3-none-any.whl
	Collecting tzlocal (from pendulum)
	Collecting pytz (from pendulum)
	  Using cached pytz-2016.7-py2.py3-none-any.whl
	Collecting six>=1.5 (from python-dateutil->pendulum)
	  Using cached six-1.10.0-py2.py3-none-any.whl
	Installing collected packages: six, python-dateutil, pytz, tzlocal, pendulum
	Successfully installed pendulum-0.6.5 python-dateutil-2.5.3 pytz-2016.7 six-1.10.0 tzlocal-1.3



.. _install_django_extensions:

pip install django-extensions
==============================

.. seealso:: https://django-extensions.readthedocs.io/en/latest/installation_instructions.html

::

	Collecting django-extensions
	  Using cached django_extensions-1.7.4-py2.py3-none-any.whl
	Requirement already satisfied: six>=1.2 in /home/assr38/Envs/django_test_dates/lib/python3.5/site-packages (from django-extensions)
	Installing collected packages: django-extensions
	Successfully installed django-extensions-1.7.4


Add django_extensions in the list of installed applications
------------------------------------------------------------



::

	INSTALLED_APPS += [
		'transactions',
		'django_extensions',
	]
	
	
.. _install_ipython:
	
pip install ipython
====================


::

    (django_test_dates) project_dates$ pip install ipython
    
::
    
	Collecting ipython
	  Using cached ipython-5.1.0-py3-none-any.whl
	Collecting decorator (from ipython)
	  Using cached decorator-4.0.10-py2.py3-none-any.whl
	Collecting traitlets>=4.2 (from ipython)
	  Using cached traitlets-4.3.1-py2.py3-none-any.whl
	Collecting pygments (from ipython)
	  Using cached Pygments-2.1.3-py2.py3-none-any.whl
	Requirement already satisfied: setuptools>=18.5 in /home/assr38/Envs/django_test_dates/lib/python3.5/site-packages (from ipython)
	Collecting pexpect; sys_platform != "win32" (from ipython)
	  Using cached pexpect-4.2.1-py2.py3-none-any.whl
	Collecting prompt-toolkit<2.0.0,>=1.0.3 (from ipython)
	  Using cached prompt_toolkit-1.0.8-py3-none-any.whl
	Collecting pickleshare (from ipython)
	  Using cached pickleshare-0.7.4-py2.py3-none-any.whl
	Collecting simplegeneric>0.8 (from ipython)
	Collecting ipython-genutils (from traitlets>=4.2->ipython)
	  Using cached ipython_genutils-0.1.0-py2.py3-none-any.whl
	Requirement already satisfied: six in /home/assr38/Envs/django_test_dates/lib/python3.5/site-packages (from traitlets>=4.2->ipython)
	Collecting ptyprocess>=0.5 (from pexpect; sys_platform != "win32"->ipython)
	  Using cached ptyprocess-0.5.1-py2.py3-none-any.whl
	Collecting wcwidth (from prompt-toolkit<2.0.0,>=1.0.3->ipython)
	  Using cached wcwidth-0.1.7-py2.py3-none-any.whl
	Installing collected packages: decorator, ipython-genutils, traitlets, pygments, ptyprocess, pexpect, wcwidth, prompt-toolkit, pickleshare, simplegeneric, ipython
	Successfully installed decorator-4.0.10 ipython-5.1.0 ipython-genutils-0.1.0 pexpect-4.2.1 pickleshare-0.7.4 prompt-toolkit-1.0.8 ptyprocess-0.5.1 pygments-2.1.3 simplegeneric-0.8.1 traitlets-4.3.1 wcwidth-0.1.7





	



		
