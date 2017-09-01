@echo off
set JAVA_HOME=%JAVA_8_HOME%
echo JAVA_HOME=%JAVA_HOME%
set JRE_HOME=%JRE_8_HOME%
echo JRE_HOME=%JRE_8_HOME%
set PATH=%JAVA_HOME%;%JRE_HOME%\bin;%PATH%
java -version
