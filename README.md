# comuniobot
Programm zur automatisierten Vergabe von Prämien nach einem Spieltag.

<h1>Verwendung</h1>
<h2>Installation auf Windows</h2>
Auf dem System muss Python 3.x mit den Pythonmodulen requests und wxPython installiert sein.<br>
Zuerst Python 3.x installieren: https://www.python.org/downloads/<br>
Wichtig, den Haken bei 'Add Python to Path' setzen:
<img src=http://otree.readthedocs.io/en/latest/_images/py-win-installer.png /> <br>
Anschließend cmd Shell öffnen und 'python --version' eingeben, um sicherzustellen, dass Python korrekt installiert ist. Das Ergebnis sollte folgendermaßen aussehen:<br>
<img src="https://raw.githubusercontent.com/nliakm/comuniobot/master/ReadmeImages/cmdPythonVersion.png" /><br>
Als letztes requests und wxPython mit folgendem Befehl installieren:<br>
<img src="https://raw.githubusercontent.com/nliakm/comuniobot/master/ReadmeImages/pythonInstallRequestAndWxPython.png" />
Nun sind alle Voraussetzungen installiert und das Programm kann gestartet werden. 

<h2>Ausführung</h2>
Das Projekt klonen und anschließend die Datei ComunioBot.py ausführen
<h2>Login</h2>
Zum Login einfach Benutzername und Passwort in die entsprechenden Felder eingeben und einloggen.
Nach ein paar Sekunden wird es eine Rückmeldung geben, ob der Login erfolgreich war.
<h2>Einstellungen vornehmen</h2>
<h3>Modus</h3>
Über den Tab Modus kann man folgende Einstellungen vornehmen:<br><br>
1. Feste Praemien<br>
Hier werden pro Platzierung feste Betraege dem jeweiligen Spieler gutgeschrieben.<br><br>
2. Punkte basiert<br>
Hier werden die Punkte mit einem selbst definierbaren Wert multipliziert, dessen Ergebnis die Praemie des jeweiligen Spielers ist.
<h3>Datei</h3>
Über den Tab "Datei" kann man folgende Einstellungen vornehmen:<br><br>
1. Letzte Platzierung fuer Pramie<br>
Dieser Wert legt fest, bis zu welcher Platzierung (ausgehend von Platz 1) Praemien vergeben werden sollen.<br><br>
2. Feste Praemien setzen<br>
Hier laesst sich einstellen, welche Platzierung welchen festen Betrag als Praemie bekommt (sofern der Modus 'Feste Praemien' aktiv ist)<br><br>
3. Multiplikator anpassen<br>
Hier kann man den Multiplikator einstellen, der mit den Punkten eines Spielers multipliziert wird, dessen Ergebnis die Praemie ist (sofern der Modus 'Punkte basiert' aktiv ist))

<h3>Troubleshooting</h3>
Sollte in der cmd-Shell der Befehl python nicht gefunden werden, ist normalerweise die Umgebungsvariable für Python nicht (korrekt) gesetzt.<br>
Dies tut man manuell folgendermaßen:<br>
<img src="https://raw.githubusercontent.com/nliakm/comuniobot/master/ReadmeImages/pythonInstallationWin10PS.png" /> <br><br>
