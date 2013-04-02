%define		srcname		jts
%include	/usr/lib/rpm/macros.java
Summary:	JTS Topology Suite
Name:		java-%{srcname}
Version:	1.11
Release:	0.1
License:	LGPL v2.1
Group:		Libraries/Java
Source0:	http://downloads.sourceforge.net/jts-topo-suite/jts-%{version}.zip
# Source0-md5:	fdf2401361290c73cb0785bb25c9257f
Source1:	build.xml
URL:		http://tsusiatsoftware.net/jts/main.html
BuildRequires:	ant
BuildRequires:	jpackage-utils
BuildRequires:	jre
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	java-jdom
Requires:	java-xerces
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JTS is a java library which provides:
- an implementation of the spatial data model defined in the OGC
  Simple Features Specification for SQL (SFS)
- a complete, consistent, implementation of fundamental 2D spatial
  algorithms
- an explicit precision model, with algorithms that gracefully handle
  situations that result in dimensional collapse
- robust implementations of key computational geometric operations
- I/O in Well-Known Text format

%prep
%setup -qc
cp -p %{SOURCE1} .

%build
%ant -Dbasedir=.

%install
rm -rf $RPM_BUILD_ROOT

# jars
install -d $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{srcname}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/%{srcname}-%{version}.jar
%{_javadir}/%{srcname}.jar
