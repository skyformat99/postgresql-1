#
# Conditional build:
# _with_jdbc		- with JDBC driver
#

# todo:
# 1. pam_xauth problem
#    - change pam_xauth behaviour?
#    - change postgres user home directory?
# 2. dump is required before upgrade
#    if [ -f /etc/sysconfig/postgresql ]; then
#      POSTGRES_DATA_DIR=/var/lib/pgsql
#      . /etc/sysconfig/postgresql
#      if [ -f $POSTGRES_DATA_DIR/PG_VERSION ]; then
#        if [ `cat $POSTGRES_DATA_DIR/PG_VERSION` != '7.2' ]; then
#          echo "Database in older, incompatible format exists in $POSTGRES_DATA_DIR."
#          echo "Dump it and clean $POSTGRES_DATA_DIR, then upgrade postgresql and"
#          echo "restore database"
#          exit 1
#        fi
#      fi
#    fi


%include	/usr/lib/rpm/macros.perl
%include	/usr/lib/rpm/macros.python

Summary:	PostgreSQL Data Base Management System
Summary(de):	PostgreSQL Datenbankverwaltungssystem
Summary(es):	Gestor de Banco de Datos PostgreSQL
Summary(fr):	Sys�me de gestion de base de donn�es PostgreSQL
Summary(pl):	PostgreSQL - system bazodanowy
Summary(pt_BR):	Gerenciador de Banco de Dados PostgreSQL
Summary(tr):	Veri Taban� Y�netim Sistemi
Name:		postgresql
Version:	7.2
Release:	2
License:	BSD
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Source0:	ftp://ftp.postgresql.org/pub/source/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	pgsql-Database-HOWTO-html.tar.gz
Source3:	%{name}.sysconfig
Source4:	pgaccess.desktop
Source5:	pgaccess.png
Patch0:		%{name}-no_libnsl.patch
Patch1:		%{name}-configure.patch
Patch2:		%{name}-ac_fixes.patch
Patch3:		%{name}-pg_ctl-silent.patch
Patch4:		%{name}-DESTDIR.patch
Icon:		postgresql.xpm
URL:		http://www.postgresql.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tcl-devel >= 8.3.2
BuildRequires:	tk-devel >= 8.3.2
BuildRequires:	readline-devel >= 4.2
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	perl-devel >= 5.6
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		/sbin/chkconfig
Prereq:		rc-scripts
Prereq:		%{name}-clients = %{version}
Requires:	%{name}-libs = %{version}
Obsoletes:	postgresql-server
Obsoletes:	postgresql-test

%define		_pgmoduledir	%{_libdir}/postgresql
%define		_pgsqldir	%{_pgmoduledir}/sql

%description
PostgreSQL Data Base Management System (formerly known as Postgres,
then as Postgres95).

PostgreSQL is an enhancement of the POSTGRES database management
system, a next-generation DBMS research prototype. While PostgreSQL
retains the powerful data model and rich data types of POSTGRES, it
replaces the PostQuel query language with an extended subset of SQL.
PostgreSQL is free and the complete source is available.

PostgreSQL development is being performed by a team of Internet
developers who all subscribe to the PostgreSQL development mailing
list. The current coordinator is Marc G. Fournier
(scrappy@postgreSQL.org). This team is now responsible for all current
and future development of PostgreSQL.

The authors of PostgreSQL 1.01 were Andrew Yu and Jolly Chen. Many
others have contributed to the porting, testing, debugging and
enhancement of the code. The original Postgres code, from which
PostgreSQL is derived, was the effort of many graduate students,
undergraduate students, and staff programmers working under the
direction of Professor Michael Stonebraker at the University of
California, Berkeley.

The original name of the software at Berkeley was Postgres. When SQL
functionality was added in 1995, its name was changed to Postgres95.
The name was changed at the end of 1996 to PostgreSQL.

PostgreSQL runs on Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD,
and most flavours of Unix.

%description -l de
PostgreSQL Datenbank-Managementsystem (fr�her als Postgres, dann als
Postgres95 bekannt).

PostgreSQL ist eine Verbesserung des POSTGRES-DB-Managementsystems,
ein DBMS-Forschungsprototyp der n�chsten Generation. W�hrend es das
leistungsf�hige Datenmodell und die reichhaltigen Datentypen von
POSTGRES beibeh�lt, ersetzt es die PostQuel-Abfragesprache durch ein
Subset von SQL. PostgreSQL ist gratis, der gesamte Quellcode ist
verf�gbar.

Ein Team von Internet-Entwicklern befa�t sich mit PostgreSQL. Sie alle
sind auf der PostgreSQL-Entwickleradre�liste. Koordinator ist Marc G.
Fournier (scrappy@postgreSQL.org). Das Team ist verantwortlich f�r
alle aktuellen und k�nftigen Entwicklungen von PostgreSQL.

Die Autoren von PostgreSQL 1.01 waren Andrew Yu und Jolly Chen.
Zahlreiche andere haben zur Portierung, zum Testen, Debugging und zur
Verbesserung des Code beigetragen. Den Original-Postgres-Code, von dem
sich PostgreSQL ableitet, verdanken wir der Arbeit vieler Doktoranden,
Studenten und Programmierern unter der Leitung von Professor Michael
Stonebraker an der University of California, Berkeley.

Der urspr�ngliche Name war Postgres. Als 1995 SQL-Funktionalit�t
hinzukam, wurde der Name in Postgres95 ge�ndert. Ende 1996 schlie�lich
entschied man sich f�r PostgreSQL.

PostgreSQL l�uft auf Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD
und den meisten Unix-Systemen.

%description -l es
Administrador de Banco de Datos PostgreSQL (conocido anteriormente
como Postgres, y despu�s como Postgres95). PostgreSQL es una
continuaci�n mejorada del Sistema Administrador de Banco de Datos
POSTGRES, que era un prototipo de pesquisa para un SGBD de nueva
generaci�n. Mientras PostgreSQL mantiene el potente modelo de datos y
los varios tipos de datos del POSTGRES, substituye el lenguaje de
consulta PostQuel por un subconjunto extendido de la SQL. PostgreSQL
es libre y tiene los fuentes disponibles. El desarrollo del PostgreSQL
se ejecutado por un equipo de estudiosos de Internet, todos suscritos
en la lista de desarrollo del PostgreSQL. El coordinador actual es
Marc G. Fournier (scrappy@postgreSQL.org). Este equipo es ahora
responsable por el desarrollo actual y futuro del PostgreSQL.

%description -l fr
Syst�me de gestion de bases de donn�es PostgreSQL (D'abord nomm�
Postgres, puis Postgres95).

PostgreSQL est une am�lioration du syst�me de gestion de bases de
donn�es POSTGRES, un prototype de recherche de la g�n�ration suivant
DBMS. Tout en conservant le puissant mod�le de donn�e de et les types
de don�e riches de Postgres, il remplace le langage de requ�tes de
Postgres par un sous ensemble etendu de commandes SQL. PosrgreSQL est
libre, et ses sources sont disponibles.

Le d�veloppement de PostgreSQL est actuellement r�alis� via internet
parune �quipe de d�veloppeurs inscrits sur la mailing-list de
d�veloppement de PostgreSQL. Le coordinateur actuel est Marc G
Fournier (scrappy@postgreSQL.org). Cette �quipe est responsable du
d�veloppemen actuel et � venir de PostgreSQL.

Les auteurs de PostgreSQL 1.01 �taient Andrew Yu et Jolly Chen.
Beaucoup d'autres ont contribu� au portage, au test, au d�bogage et �
l'am�lioration du code. Le code original de Postgres, duquel
PostgreSQL est d�riv�, a �t� l'oeuvre d'�tudiants de haut niveau, de
moins haut niveau, et de programmeurs travaillant sous la direction du
professeur Michael Stonebraker � l'universit� de Berkeley Californie.

Le nom original du logiciel �tait Postgres. Quand les fonctionnalit�es
SQL furent ajout�es en 1995, son nom est devenu Postgres95. Il a �t�
rebaptis� PostgreSQL en 1996.

PostgreSQL tourne sur Solaris, SunOS, HPUX, AIX, Linux, Irix, FreeBSD,
et la plupart des Unix.

%description -l pl
System Zarz�dzania Baz� Danych PostgreSQL (dawniej znany jako Postgres,
nast�pnie jako Postgres95).

PostgreSQL jest rozszerzeniem systemu zarz�dzania baz danych POSTGRES,
prototypu DBMS nast�pnej generacji. Co prawda PostgreSQL odziedziczy� model
danych oraz bogaty zbi�r r�nych typ�w danych, to jednak j�zyk zapyta�
PostQuel zosta� zast�piony rozszerzonym SQL-em. PostgreSQL jest wolnym
oprogramowaniem i kody �r�d�owe tego oprogramowania s� w pe�ni dost�pne. 

System PostgreSQL jest tworzony przez zesp� ludzi, kt�rzy s� zapisani na
list� dyskusyjn� dotycz�c� PostgreSQL-a. Obecnym koordynatorem jest  Marc
G. Fournier (scrappy@postgreSQL.org).  Wymieniony wy�ej zesp� jest
odpowiedzialny za aktualny i przysz�y rozw�j systemu PostgreSQL.

Autorami PostgreSQL-a 1.01 byli Andrew Yu oraz Jolly Chen. Wielu innych
pomaga�o przenosz�c na r�ne platformy, testuj�c, analizuj�c i rozszerzaj�c
kod. Oryginalny kod Postgres-a, na podstawie kt�rego PostgreSQL powsta�,
by� wysi�kiem wielu absolwent�w, student�w oraz zespo�u programist�w,
kt�rzy pracowali pod kierunkiem profesora Michaela Stonebrakera z
Uniwersytetu Kalifornii w Berkeley.

Nazwa oryginalna oprogramowania tworzonego w Berkeley brzmia�a Postgres.
W 1995 roku dodano j�zyk zapyta� SQL i nazw� zmieniono na Postgres95.
W ko�cu roku 1996 nazw� ostatecznie zmieniono na PostgreSQL.

PostgreSQL mo�e by� uruchominy pod nast�puj�cymi systemami: Solaris, SunOS,
HPUX, AIX, Linux, Irix, FreeBSD i innych systemach Unix.

%description -l pt_BR
Gerenciador de Banco de Dados PostgreSQL (conhecido anteriormente como
Postgres, e depois como Postgres95).

O PostgreSQL � uma continua��o melhorada do Sistema Gerenciador de
Banco de Dados POSTGRES, que era um prot�tipo de pesquisa para um SGBD
de nova gera��o. Enquanto o PostgreSQL mant�m o poderoso modelo de
dados e os v�rios tipos de dados do POSTGRES, ele substitui a
linguagem de consulta PostQuel por um subconjunto estendido da SQL. O
PostgreSQL � livre e tem os fontes dispon�veis.

O desenvolvimento do PostgreSQL est� sendo executado por uma equipe de
desenvolvedores da Internet, todos subscritores da lista de
desenvolvimento do PostgreSQL. O coordenador atual � Marc G. Fournier
(scrappy@postgreSQL.org). Esta equipe � agora respons�vel pelo
desenvolvimento atual e futuro do PostgreSQL.

%description -l tr
PostgreSQL, POSTGRES'den t�remi� bir veri taban� y�netim sistemidir
(DBMS). G��l� veri modeli ve zengin POSTGRES veri tiplerini
desteklerken SQL'in geni�letilmi� bir altk�mesi yerine PostQuel
sorgulama dilini koyar.

%package devel
Summary:	PostgreSQL development header files and libraries
Summary(de):	PostgreSQL-Entwicklungs-Header-Dateien und Libraries 
Summary(es):	Archivos de inclusi�n y bibliotecas PostgreSQL
Summary(fr):	En-t�tes et biblioth�ques de d�veloppement PostgreSQL
Summary(pl):	PostgreSQL - pliki nag��wkowe i biblioteki
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para desenvolvimento com o PostgreSQL
Summary(tr):	PostgreSQL ba�l�k dosyalar� ve kitapl�klar
Group:		Development/Libraries
Group(cs):	V�vojov� prost�edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	�r�unart�l/A�ger�as�fn
Group(it):	Sviluppo/Librerie
Group(ja):	��ȯ/�饤�֥��
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(sl):	Razvoj/Knji�nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	��������/��̦�����
Requires:	%{name}-libs = %{version}

%description devel
This package contains header files and libraries required to compile
applications that are talking directly to the PostgreSQL backend
server.

%description devel -l de
Dieses Paket enth�lt die Header-Dateien und Libraries, die zum
Kompilieren von Applikationen notwendig sind, die direkt mit dem
PostgreSQL-Backend-Server kommunizieren.

%description devel -l es
Este paquete contiene archivos de inclusi�n y bibliotecas requeridas
para compilaci�n de aplicativos que se comunican directamente con el
servidor backend PostgreSQL.

%description devel -l fr
Ce package contient les fichiers d'en-t�te et les biblioth�ques
n�cessaires pour compiler des applications ayant des �changes directs
avec le serveur du backend PostgreSQL.

%description devel -l pl
Pakiet zawiera nag��wki oraz biblioteki wymagane do kompilacji
aplikacji ��cz�cych si� bezpo�rednio z serwerem PostgreSQL.

%description devel -l pt_BR
Este pacote cont�m arquivos de inclus�o e bibliotecas requeridas para
compila��o de aplicativos que se comunicam diretamente com o servidor
backend PostgreSQL.

%description devel -l tr
Bu paket, PostgreSQL sunucusuyla konu�acak yaz�l�mlar geli�tirmek i�in
gereken ba�l�k dosyalar�n� ve kitapl�klar� i�erir.


%package backend-devel
Summary:	PostgreSQL backend development header files
Summary(pl):	PostgreSQL - pliki nag��wkowe dla backendu
Group:		Development/Libraries
Group(cs):	V�vojov� prost�edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	�r�unart�l/A�ger�as�fn
Group(it):	Sviluppo/Librerie
Group(ja):	��ȯ/�饤�֥��
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(sl):	Razvoj/Knji�nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	��������/��̦�����
Requires:	%{name}-libs = %{version}

%description backend-devel
This package contains header files required to compile functions that
could be loaded directly by backend

%description backend-devel -l pl
Pakiet zawiera nag��wki wymagane do kompilacji funkcji ktore moga byc
bezposrednio ladowane przez beckend serwera PostgreSQL.

%package clients
Summary:	Clients needed to access a PostgreSQL server
Summary(es):	Clientes necesarios para acceder al servidor PostgreSQL
Summary(pl):	Klienci wymagani do dost�pu do serwera PostgreSQL
Summary(pt_BR):	Clientes necess�rios para acessar o servidor PostgreSQL
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name}-libs = %{version}

%description clients
This package includes only the clients and client libraries needed to
access an PostgreSQL server. The server is included in the main
package. If all you need is to connect to another PostgreSQL server,
the this is the only package you need to install.

In this package there are client libraries available for C and C++, as
well as several command-line utilities you can use to manage your
databases on a remote PostgreSQL server.

%description clients -l es
Este paquete incluye solamente los clientes necesarios para acceder un
servidor PostgreSQL. El servidor est� en el paquete principal.

%description clients -l pl
Pakiet zawiera klient�w oraz biblioteki niezb�dne dla dost�pu do
serwera PostgreSQL. Serwer znajduje si� w g��wnym pakiecie.

%description clients -l pt_BR
Este pacote inclui somente os clientes necess�rios para acessar um
servidor PostgreSQL. O servidor est� no pacote principal.

%package perl
Summary:	Perl interface to PostgreSQL database
Summary(es):	M�dulo Perl para acceder un servidor PostgreSQL
Summary(pl):	Interfejs dla Perla umo�liwiaj�cy dost�p do baz PostgreSQL
Summary(pt_BR):	M�dulo Perl para acesso ao servidor PostgreSQL
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	perl >= 5.004
Requires:	%{name}-libs = %{version}

%description perl
This package includes only perl modules needed to access an PostgreSQL
server.

%description perl -l es
M�dulo Perl para acceder un servidor PostgreSQL

%description perl -l pl
Pakiet ten zawiera tylko modu�y Perla wymagane dla dost�pu do serwera
PostgreSQL.

%description perl -l pt_BR
M�dulo Perl para acesso ao servidor PostgreSQL.

%package -n python-postgresql
Summary:	The python-based client programs needed for accessing a PostgreSQL server
Summary(es):	M�dulo Python para acceder un servidor PostgreSQL
Summary(pl):	Programy klienckie do dost�pu do serwera PostgreSQL napisane w Pythonie
Summary(pt_BR):	M�dulo Python para acesso ao servidor PostgreSQL.
Group:		Development/Languages/Python
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Python
Group(da):	Udvikling/Sprog/Python
Group(de):	Entwicklung/Sprachen/Python
Group(es):	Desarrollo/Lenguajes/Python
Group(fr):	Development/Langues/Python
Group(is):	�r�unart�l/Forritunarm�l/Python
Group(it):	Sviluppo/Linguaggi/Python
Group(ja):	��ȯ/����/Python
Group(no):	Utvikling/Programmeringsspr�k/Python
Group(pl):	Programowanie/J�zyki/Python
Group(pt):	Desenvolvimento/Linguagens/Python
Group(ru):	����������/�����/Python
Group(sl):	Razvoj/Jeziki/Python
Group(sv):	Utveckling/Spr�k/Python
Group(uk):	��������/����/Python
Requires:	python >= 2.0
Requires:	%{name}-libs = %{version}
Obsoletes:	python-PyGreSQL
Obsoletes:	postgresql-python

%description -n python-postgresql
postgresql-python includes the python-based client programs and client
libraries that you'll need to access a PostgreSQL database management
system server.

%description -n python-postgresql -l es
M�dulo Python para acceder un servidor PostgreSQL

%description -n python-postgresql -l pl
Pakiet ten zawiera napisane w Pythonie programy i biblioteki klienckie
do dost�pu do serwera baz danych PostgreSQL.

%description -n python-postgresql -l pt_BR
M�dulo Python para acesso ao servidor PostgreSQL.

%package doc
Summary:	Documentation for PostgreSQL
Summary(pl):	Dodatkowa dokumantacja dla PostgreSQL
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����

%description doc
This package includes documentation and HOWTO for programmer, admin
etc., in HTML format.

%description doc -l pl
Pakiet ten zawiera dokumentacj� oraz HOWTO m.in. dla programist�w,
administrator�w w formacie HTML.

%package libs
Summary:	PostgreSQL libraries
Summary(es):	Biblioteca compartida del PostgreSQL
Summary(pl):	Biblioteki dzielone programu PostgreSQL
Summary(pt_BR):	Biblioteca compartilhada do PostgreSQL
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	A�ger�as�fn
Group(it):	Librerie
Group(ja):	�饤�֥��
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(sl):	Knji�nice
Group(sv):	Bibliotek
Group(uk):	��̦�����

%description libs
PostgreSQL libraries.

%description libs -l es
Este paquete contiene la biblioteca compartida para acceso al
postgresql.

%description libs -l pl
Biblioteki dzielone programu PostgreSQL.

%description libs -l pt_BR
Este pacote cont�m a biblioteca compartilhada para acesso ao
postgresql.

%package static
Summary:	PostgreSQL static libraries
Summary(es):	Bibliotecas estaticas PostgreSQL
Summary(pl):	Biblioteki statyczne programu PostgreSQL
Summary(pt_BR):	Bibliotecas est�ticas PostgreSQL
Group:		Development/Libraries
Group(cs):	V�vojov� prost�edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	�r�unart�l/A�ger�as�fn
Group(it):	Sviluppo/Librerie
Group(ja):	��ȯ/�饤�֥��
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(sl):	Razvoj/Knji�nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
PostgreSQL static libraries.

%description static -l es
Este paquete contiene bibliotecas estaticas requerida para compilaci�n
de aplicativos que se comunican directamente con el servidor backend
PostgreSQL.

%description static -l pl
Biblioteki statyczne programu PostgreSQL.

%description static -l pt_BR
Este pacote cont�m as bibliotecas est�ticas requeridas para compila��o
de aplicativos que se comunicam diretamente com o servidor backend
PostgreSQL.

%package c++
Summary:	C++ interface to PostgreSQL
Summary(pl):	Interfejs C++ do PostgreSQL
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name}-libs = %{version}

%description c++
This package includes library for C++ interface to PostgreSQL.

%description c++ -l pl
Pakiet ten zawiera biblioteki dla interfejsu C++ do PostgreSQL.

%package c++-devel
Summary:	C++ interface to PostgreSQL - development part
Summary(pl):	Interfejs C++ do PostgreSQL - cze�� programistyczna
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name}-c++ = %{version}
Requires:	%{name}-devel = %{version}

%description c++-devel
This package includes library and header files for C++ interface.

%description c++-devel -l pl
Pakiet ten zawiera biblioteki i pliki nag��wkowe dla interfejsu C++.

%package c++-static
Summary:	C++ interface to PostgreSQL - static libraries
Summary(pl):	Interfejs C++ do PostgreSQL - biblioteki statyczne
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name}-c++-devel = %{version}

%description c++-static
This package includes static library for interface C++.

%description c++-static -l pl
Pakiet ten zawiera biblioteki statyczne dla interfejsu C++.

%package odbc
Summary:	ODBC interface to PostgreSQL
Summary(es):	Driver ODBC para acceder un servidor PostgreSQL
Summary(pl):	Interfejs ODBC do PostgreSQL
Summary(pt_BR):	Driver ODBC necess�rio para acessar um servidor PostgreSQL
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name}-libs = %{version}

%description odbc
This package includes library for interface ODBC.

%description odbc -l es
Driver para acceder un servidor PostgreSQL, a trav�s de ODBC.

%description odbc -l pl
Pakiet ten zawiera biblioteki dla interfejsu ODBC.

%description odbc -l pt_BR
Driver ODBC necess�rio para acessar um servidor PostgreSQL.

%package odbc-devel
Summary:	ODBC interface to PostgreSQL - development part
Summary(pl):	Interfejs ODBC do PostgreSQL - cze�� programistyczna
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name}-odbc = %{version}
Requires:	%{name}-devel = %{version}

%description odbc-devel
This package includes library and header files for interface ODBC.

%description odbc-devel -l pl
Pakiet ten zawiera biblioteki i pliki nag��wkowe dla interfejsu ODBC.

%package odbc-static
Summary:	ODBC interface to PostgreSQL - static libraries
Summary(pl):	Interfejs ODBC do PostgreSQL - biblioteki statyczne
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name}-odbc-devel = %{version}

%description odbc-static
This package includes static library for interface ODBC.

%description odbc-static -l pl
Pakiet ten zawiera biblioteki statyczne dla interfejsu ODBC.

%package -n pgaccess
Summary:	A free graphical database management tool for PostgreSQL
Summary(pl):	Graficzne narz�dzie do obs�ugi baz danych PostgreSQL
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name}-tcl = %{version}

%description -n pgaccess
A free graphical database management tool for PostgreSQL.

%description -n pgaccess -l pl
Graficzne narz�dzie do obs�ugi baz danych PostgreSQL.

%package tcl
Summary:	tcl interface for PostgreSQL
Summary(es):	Bibliotecas y shell TCL para acceder un servidor PostgreSQL
Summary(pl):	Interfejs tcl dla PostgreSQL
Summary(pt_BR):	Bibliotecas e shell para programas em TCL acessarem o servidor PostgreSQL
Group:		Development/Languages/Tcl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Tcl
Group(da):	Udvikling/Sprog/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(es):	Desarrollo/Lenguajes/Tcl
Group(fr):	Development/Langues/Tcl
Group(is):	�r�unart�l/Forritunarm�l/Tcl
Group(it):	Sviluppo/Linguaggi/Tcl
Group(ja):	��ȯ/����/Tcl
Group(no):	Utvikling/Programmeringsspr�k/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Group(pt):	Desenvolvimento/Linguagens/Tcl
Group(ru):	����������/�����/Tcl
Group(sl):	Razvoj/Jeziki/Tcl
Group(sv):	Utveckling/Spr�k/Tcl
Group(uk):	��������/����/Tcl
Requires:	%{name}-libs = %{version}

%description tcl
tcl interface for PostgreSQL.

%description tcl -l es
Bibliotecas y shell TCL para acceder un servidor PostgreSQL

%description tcl -l pl
Interfejs tcl dla PostgreSQL.

%description tcl -l pt_BR
Bibliotecas e shell para programas em TCL acessarem o servidor
PostgreSQL

%package tcl-devel
Summary:	Development part of tcl interface for PostgreSQL
Summary(pl):	Cz�� dla programist�w interfejsu tcl dla PostgreSQL
Group:		Development/Languages/Tcl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Tcl
Group(da):	Udvikling/Sprog/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(es):	Desarrollo/Lenguajes/Tcl
Group(fr):	Development/Langues/Tcl
Group(is):	�r�unart�l/Forritunarm�l/Tcl
Group(it):	Sviluppo/Linguaggi/Tcl
Group(ja):	��ȯ/����/Tcl
Group(no):	Utvikling/Programmeringsspr�k/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Group(pt):	Desenvolvimento/Linguagens/Tcl
Group(ru):	����������/�����/Tcl
Group(sl):	Razvoj/Jeziki/Tcl
Group(sv):	Utveckling/Spr�k/Tcl
Group(uk):	��������/����/Tcl
Requires:	%{name}-tcl = %{version}
Requires:	%{name}-devel = %{version}

%description tcl-devel
Development part of tcl interface for PostgreSQL.

%description tcl-devel -l pl
Cz�� interfejsu tcl dla PostgreSQL przeznaczona dla programist�w.

%package tcl-static
Summary:	Static libraries of tcl interface for PostgreSQL
Summary(pl):	Biblioteki statyczne interfejsu tcl dla PostgreSQL
Group:		Development/Languages/Tcl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Tcl
Group(da):	Udvikling/Sprog/Tcl
Group(de):	Entwicklung/Sprachen/Tcl
Group(es):	Desarrollo/Lenguajes/Tcl
Group(fr):	Development/Langues/Tcl
Group(is):	�r�unart�l/Forritunarm�l/Tcl
Group(it):	Sviluppo/Linguaggi/Tcl
Group(ja):	��ȯ/����/Tcl
Group(no):	Utvikling/Programmeringsspr�k/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Group(pt):	Desenvolvimento/Linguagens/Tcl
Group(ru):	����������/�����/Tcl
Group(sl):	Razvoj/Jeziki/Tcl
Group(sv):	Utveckling/Spr�k/Tcl
Group(uk):	��������/����/Tcl
Requires:	%{name}-tcl-devel = %{version}

%description tcl-static
Static libraries of tcl interface for PostgreSQL.

%description tcl-devel -l pl
Biblioteki statyczne interfejsu tcl dla PostgreSQL.

%package module-plpgsql
Summary:	PL/pgSQL - PostgreSQL procedural language
Summary(pl):	PL/pgSQL j�zyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name} = %{version}

%description module-plpgsql
From PostgreSQL documentation.

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/pgSQL procedural language for your database you have to
run createlang command.

%description module-plpgsql -l pl
Z dokumentacji PostgreSQL.

Postgres ma wsparcie dla j�zyk�w proceduralnych. W przypadku, kiedy
programista zdefiniuje procedur� wyzwalacza lub funkcj� w j�zyku
proceduralnym, baza danych nie ma poj�cia jak interpretowa� tego typu
funkcj�. Funkcja lub procedura ta jest przekazywana do interpretera,
kt�ry wie jak j� wykona�. Interpreter jest odpowiedni�, specjaln�
funkcj�, kt�ra jest skompilowana w obiekt dzielony i �adowany w razie
potrzeby.

Za pomoc� komendy createlang mo�na doda� wsparcie dla j�zyka
proceduralnego PL/pgSQL dla swojej bazy danych.

%package module-plperl
Summary:	PL/perl - PostgreSQL procedural language
Summary(pl):	PL/perl j�zyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name} = %{version}
%requires_eq	perl

%description module-plperl
From PostgreSQL documentation.

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/perl procedural language for your database you have to
run createlang command.

%description module-plperl -l pl
Z dokumentacji PostgreSQL.

Postgres ma wsparcie dla j�zyk�w proceduralnych. W przypadku, kiedy
programista zdefiniuje procedur� wyzwalacza lub funkcj� w j�zyku
proceduralnym, baza danych nie ma poj�cia jak interpretowa� tego typu
funkcj�. Funkcja lub procedura ta jest przekazywana do interpretera,
kt�ry wie jak j� wykona�. Interpreter jest odpowiedni�, specjaln�
funkcj�, kt�ra jest skompilowana w obiekt dzielony i �adowany w razie
potrzeby.

Za pomoc� komendy createlang mo�na doda� wsparcie dla j�zyka
proceduralnego PL/perl dla swojej bazy danych.

%package module-plpython
Summary:	PL/python - PostgreSQL procedural language
Summary(pl):	PL/python j�zyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name} = %{version}
%requires_eq	python

%description module-plpython
From PostgreSQL documentation.

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/python procedural language for your database you have to
run createlang command.

%description module-plpython -l pl
Z dokumentacji PostgreSQL.

Postgres ma wsparcie dla j�zyk�w proceduralnych. W przypadku, kiedy
programista zdefiniuje procedur� wyzwalacza lub funkcj� w j�zyku
proceduralnym, baza danych nie ma poj�cia jak interpretowa� tego typu
funkcj�. Funkcja lub procedura ta jest przekazywana do interpretera,
kt�ry wie jak j� wykona�. Interpreter jest odpowiedni�, specjaln�
funkcj�, kt�ra jest skompilowana w obiekt dzielony i �adowany w razie
potrzeby.

Za pomoc� komendy createlang mo�na doda� wsparcie dla j�zyka
proceduralnego PL/python dla swojej bazy danych.

%package module-pltcl
Summary:	PL/TCL - PostgreSQL procedural language
Summary(pl):	PL/TCL - j�zyk proceduralny bazy danych PostgreSQL
Group:		Applications/Databases
Group(cs):	Aplikace/Datab�ze
Group(da):	Programmer/Databaser
Group(de):	Applikationen/Datenbanken
Group(es):	Aplicaciones/Bases de Datos
Group(fr):	Applications/Bases de Donn�es
Group(id):	Aplikasi/Database
Group(is):	Forrit/Gagnagrunnar
Group(it):	Applicazioni/Database
Group(ja):	���ץꥱ�������/�ǡ����١���
Group(no):	Applikasjoner/Databaser
Group(pl):	Aplikacje/Bazy Danych
Group(pt):	Aplica��es/Bases de Dados
Group(ru):	����������/���� ������
Group(sl):	Programi/Zbirke podatkov
Group(sv):	Till�mpningar/Databaser
Group(uk):	�������Φ ��������/���� �����
Requires:	%{name} = %{version}

%description module-pltcl
From PostgreSQL documentation.

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/TCL procedural language for your database you have to run
createlang command.

%description module-pltcl -l pl
Z dokumentacji PostgreSQL.

Postgres ma wsparcie dla j�zyk�w proceduralnych. W przypadku, kiedy
programista zdefiniuje procedur� wyzwalacza lub funkcj� w j�zyku
proceduralnym, baza danych nie ma poj�cia jak interpretowa� tego typu
funkcj�. Funkcja lub procedura ta jest przekazywana do interpretera,
kt�ry wie jak j� wykona�. Interpreter jest odpowiedni�, specjaln�
funkcj�, kt�ra jest skompilowana w obiekt dzielony i �adowany w razie
potrzeby.

Za pomoc� komendy createlang mo�na doda� wsparcie dla j�zyka
proceduralnego PL/TCL dla swojej bazy danych.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

tar xzf doc/man*.tar.gz

mkdir doc/unpacked
tar zxf doc/postgres.tar.gz -C doc/unpacked

# Erase all CVS dir
rm -fR `find contrib/ -type d -name CVS`

%build
rm -f config/libtool.m4
aclocal -I config
autoconf
%configure \
	%{!?_without_pgsql_locale:--enable-locale} \
	%{!?_without_pgsql_multibyte:--enable-multibyte} \
	--disable-rpath \
	--enable-depend \
	--enable-odbc \
	--enable-recode \
	--enable-syslog \
	--enable-unicode-conversion \
	--with-CXX \
	--with-tcl \
	--with-tk \
	--with-perl \
	--with-python \
	--with-openssl \
	--with-perl \
	--enable-odbc \
	--with-odbcinst=%{_sysconfdir} \
	--with-x \
%{?_with_jdbc:	--with-java}

%{__make}
%ifnarch sparc sparcv9 sparc64 alpha
%{!?_without_tests: %{__make} check }
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/etc/{rc.d/init.d,sysconfig}} \
        $RPM_BUILD_ROOT{/var/{lib/pgsql,log},%{_pgsqldir}} \
	$RPM_BUILD_ROOT{%{_applnkdir}/System,%{_pixmapsdir}} \

%{__make} install install-all-headers \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C src/pl/plperl \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT/var/log/pgsql

# Move PL/pgSQL procedural language to %{_pgmoduledir}
( cd $RPM_BUILD_ROOT%{_libdir}
  mv -f plpgsql.so $RPM_BUILD_ROOT%{_pgmoduledir}
)

# Move PL/TCL procedural language to %{_pgmoduledir}
( cd $RPM_BUILD_ROOT%{_libdir}
  mv -f pltcl.so $RPM_BUILD_ROOT%{_pgmoduledir}
)

# odbc
install src/interfaces/odbc/odbcinst.ini $RPM_BUILD_ROOT%{_sysconfdir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/postgresql
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/postgresql
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/System
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}

cp -a man?	   $RPM_BUILD_ROOT%{_mandir}

install -d howto
( cd howto
  tar xzf $RPM_SOURCE_DIR/pgsql-Database-HOWTO-html.tar.gz
)

%py_comp $RPM_BUILD_ROOT%{py_libdir}
%py_ocomp $RPM_BUILD_ROOT%{py_libdir}

gzip -9nf doc/FAQ doc/README* COPYRIGHT README HISTORY doc/bug.template \
	src/interfaces/odbc/readme.txt \
	src/interfaces/odbc/notice.txt

%clean
rm -rf $RPM_BUILD_ROOT
rm -f /tmp/tmp_perl_info

%pre
getgid postgres >/dev/null 2>&1 || /usr/sbin/groupadd -g 88 -r -f postgres
id postgres >/dev/null 2>&1 || /usr/sbin/useradd -M -o -r -u 88 \
	-d /var/lib/pgsql -s /bin/sh -g postgres \
	-c "PostgreSQL Server" postgres

%post
/sbin/chkconfig --add postgresql

if [ -f /var/lock/subsys/postgresql ]; then
	/etc/rc.d/init.d/postgresql restart >&2
else
	echo "Run \"/etc/rc.d/init.d/postgresql start\" to start postgresql server."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/postgresql ]; then
		/etc/rc.d/init.d/postgresql stop
	fi
	/sbin/chkconfig --del postgresql
fi

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post   tcl -p /sbin/ldconfig
%postun tcl -p /sbin/ldconfig

%post   clients -p /sbin/ldconfig
%postun clients -p /sbin/ldconfig

%post   c++ -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig

%post   odbc -p /sbin/ldconfig
%postun odbc -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/*

%attr(755,root,root) %{_bindir}/createdb
%attr(755,root,root) %{_bindir}/createuser
%attr(755,root,root) %{_bindir}/dropdb
%attr(755,root,root) %{_bindir}/dropuser
%attr(755,root,root) %{_bindir}/initdb
%attr(755,root,root) %{_bindir}/initlocation
%attr(755,root,root) %{_bindir}/pg_ctl
%attr(755,root,root) %{_bindir}/pg_config
%attr(755,root,root) %{_bindir}/pg_encoding
%attr(755,root,root) %{_bindir}/pg_passwd
%attr(755,root,root) %{_bindir}/postgres
%attr(755,root,root) %{_bindir}/postmaster
%attr(755,root,root) %{_bindir}/ipcclean
%attr(755,root,root) %{_bindir}/createlang
%attr(755,root,root) %{_bindir}/droplang

%dir %{_pgsqldir}
%dir %{_pgmoduledir}
%{_datadir}/postgresql/*.bki
%{_datadir}/postgresql/*.sample
%{_datadir}/postgresql/*.description

%attr(700,postgres,postgres) %dir /var/lib/pgsql
%attr(640,postgres,postgres) %config(noreplace) %verify(not md5 size mtime) /var/log/pgsql

%{_mandir}/man1/createdb.1*
%{_mandir}/man1/createlang.1*
%{_mandir}/man1/createuser.1*
%{_mandir}/man1/dropdb.1*
%{_mandir}/man1/droplang.1*
%{_mandir}/man1/dropuser.1*
%{_mandir}/man1/initdb.1*
%{_mandir}/man1/initlocation.1*
%{_mandir}/man1/pg_passwd.1*
%{_mandir}/man1/pg_ctl.1*
%{_mandir}/man1/pg_config.1*
%{_mandir}/man1/postgres.1*
%{_mandir}/man1/postmaster.1*
%{_mandir}/man1/ipcclean.1*

%doc contrib 
%doc doc/FAQ* doc/README* 
%doc COPYRIGHT.gz README.gz HISTORY.gz doc/bug.template.gz

%files doc
%defattr(644,root,root,755)
%doc doc/unpacked/*
%doc howto

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpq.so.*.*
%attr(755,root,root) %{_libdir}/libpgeasy.so.*.*
%attr(755,root,root) %{_libdir}/libecpg.so.*.*
%attr(755,root,root) %{_bindir}/pg_id

%files devel
%defattr(644,root,root,755)
%doc doc/internals.ps*
%attr(755,root,root) %{_bindir}/ecpg
%attr(755,root,root) %{_libdir}/libecpg.so
%attr(755,root,root) %{_libdir}/libpgeasy.so
%attr(755,root,root) %{_libdir}/libpq.so
%dir %{_includedir}/postgresql
%{_includedir}/pg_config.h
%{_includedir}/pg_config_os.h
%{_includedir}/ecpgerrno.h
%{_includedir}/ecpglib.h
%{_includedir}/ecpgtype.h
%{_includedir}/libpgeasy.h
%{_includedir}/libpq-fe.h
%{_includedir}/postgres_ext.h
%{_includedir}/sql3types.h
%{_includedir}/sqlca.h
%dir %{_includedir}/postgresql/internal
%{_includedir}/postgresql/internal/c.h
%{_includedir}/postgresql/internal/libpq-int.h
%{_includedir}/postgresql/internal/postgres_fe.h
%{_includedir}/postgresql/internal/pqexpbuffer.h
%{_includedir}/postgresql/internal/lib
%{_includedir}/postgresql/internal/libpq
%{_mandir}/man1/ecpg.1*

%files backend-devel
%defattr(644,root,root,755)
%{_includedir}/postgresql/server

%files static
%defattr(644,root,root,755)
%{_libdir}/libecpg.a
%{_libdir}/libpgeasy.a
%{_libdir}/libpq.a

%files clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pg_dump
%attr(755,root,root) %{_bindir}/pg_dumpall
%attr(755,root,root) %{_bindir}/pg_restore
%attr(755,root,root) %{_bindir}/psql
%attr(755,root,root) %{_bindir}/vacuumdb

%{_mandir}/man1/pg_dump.1*
%{_mandir}/man1/pg_dumpall.1*
%{_mandir}/man1/pg_restore.1*
%{_mandir}/man1/psql.1*
%{_mandir}/man1/vacuumdb.1*
%{_mandir}/manl/*.l*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpq++.so.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpq++.so
%{_includedir}/libpq++.h
%{_includedir}/libpq++

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libpq++.a

%files perl
%defattr(644,root,root,755)
%dir %{perl_sitearch}/auto/Pg
%{perl_sitearch}/auto/Pg/Pg.bs
%attr(755,root,root) %{perl_sitearch}/auto/Pg/Pg.so
%{perl_sitearch}/auto/Pg/autosplit.ix
%{perl_sitearch}/Pg.pm
%{_mandir}/man3/*


%files -n python-postgresql
%defattr(644,root,root,755)
%{py_sitedir}/*.pyc
%{py_sitedir}/*.pyo
%attr(755,root,root) %{py_sitedir}/*.so

%files -n pgaccess
%defattr(644,root,root,755)
%doc src/bin/pgaccess/doc/html/*
%attr(755,root,root) %{_bindir}/pgaccess
%dir %{_datadir}/postgresql/pgaccess
%attr(755, root, root) %{_datadir}/postgresql/pgaccess/main.tcl
%{_datadir}/postgresql/pgaccess/images
%{_datadir}/postgresql/pgaccess/lib
%{_applnkdir}/System/pgaccess.desktop
%{_pixmapsdir}/pgaccess.png
%{_mandir}/man1/pgaccess.1*

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpgtcl.so
%attr(755,root,root) %{_libdir}/libpgtcl.so.*.*
%attr(755,root,root) %{_bindir}/pgtclsh
%attr(755,root,root) %{_bindir}/pgtksh
%{_mandir}/man1/pgtclsh.1*
%{_mandir}/man1/pgtksh.1*

%files tcl-devel
%defattr(644,root,root,755)
%{_includedir}/libpgtcl.h

%files tcl-static
%defattr(644,root,root,755)
%{_libdir}/libpgtcl.a

%files odbc
%defattr(644,root,root,755)
%doc src/interfaces/odbc/readme.txt.gz src/interfaces/odbc/notice.txt.gz
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/odbc*
%attr(755,root,root) %{_libdir}/libpsqlodbc.so.*.*
%{_datadir}/postgresql/odbc.sql

%files odbc-devel
%defattr(644,root,root,755)
#%{_includedir}/postgresql/iodbc
%attr(755,root,root) %{_libdir}/libpsqlodbc.so

%files odbc-static
%defattr(644,root,root,755)
%{_libdir}/libpsqlodbc.a

%files module-plpgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/plpgsql.so

%files module-plperl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/plperl.so

%files module-plpython
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/plpython.so

%files module-pltcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pgmoduledir}/pltcl.so
