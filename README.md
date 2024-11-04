# PangDats
Bisa install camelot di terminal dulu
`pip install camelot-py[cv]`

install camelot dan pandas juga
`pip install camelot-py[cv] pandas`

Habis itu, download GhostScript
https://ghostscript.com/releases/gsdnld.html

klik yang Windows 32/64 bit yang bagian GNU Affero General Public License

Habis itu, ikutin arahan ini.
Cari installan ghostscript di file explorer dengan path ini "C:\Program Files\gs\gs<version>\bin"
Copy path nya
Buka System Properties > Environment Variables.
Di System Variables, Cari bagian "Path", Klik Edit, habis itu tambahin Ghostscript path yang dah di copy tadi.
Klik OK, habis itu restart Vscode, CMD, atau IDE lain yang dah di buka.

Next, buka Terminal di vscode atau cmd, terus masukkin kode ini.
`gswin64c -version`

Done dah
