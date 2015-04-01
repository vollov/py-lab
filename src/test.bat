   @echo off
   setlocal enabledelayedexpansion

   set str=The fat cat
   set f=fat

   echo.
   echo          f = [%f%]

   echo.
   echo        str = [%str%]

   set str=!str:%f%=thin!

   echo str:f=thin = [%str%]