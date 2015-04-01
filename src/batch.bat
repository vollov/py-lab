@ ECHO OFF

@rem IF [%1] EQU [] (
@rem echo 1st parameter missing
@rem GOTO END
@rem )

@rem IF [%2] EQU [] (
@rem echo 2nd parameter missing
@rem GOTO END
@rem )

@rem echo "GOT %1 %2"


for /f %%a IN ('dir /b "data\*.txt"') do (
	set file_name=%%~na
	echo %file_name%
	@rem  set str=%file_name:.-.=.%
	@rem echo %str%
        @rem rename "%%a" %str%
)

:END