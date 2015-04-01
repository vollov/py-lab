@ECHO OFF
SET PYTHONPATH=C:\opt\projects\py-lab\src
@REM stage_to_secure secure_to_prod postrun
python C:\opt\projects\py-lab\src\argparser\__init__.py %1 %2
