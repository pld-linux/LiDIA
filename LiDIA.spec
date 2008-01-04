Summary:	C++ library for number theoretical computations
Summary(pl.UTF-8):	Biblioteka C++ do teoretycznych obliczeń numerycznych
Name:		LiDIA
Version:	2.2.0
Release:	0.1
License:	non-commercial
Group:		Libraries
Source0:	ftp://ftp.informatik.tu-darmstadt.de/pub/TI/systems/LiDIA/current/lidia-%{version}.tar.gz
# Source0-md5:	d9e012bb666e7a7ba1b45283aa3bfe03
Patch0:		lidia-fixes.patch
URL:		http://www.informatik.tu-darmstadt.de/TI/LiDIA/
BuildRequires:	gmp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-latex-ae
BuildRequires:	texinfo-texi2dvi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LiDIA is a C++ library for number-theoretical computations.

LiDIA provides parameterized as well as specialized classes together
with advanced methods for computing in a large variety of mathematical
groups, rings, and fields, ranging from arbitrary-length integers,
fractions, and floating-point approximations, over vectors and
matrices, to high-level constructs of finite fields, lattices,
quadratic and higher-order number fields, polynomial rings, and
elliptic curves. In addition to a rich set of methods for basic
structural operations, I/O, arithmetic, and common number-theoretical
primitives, there are functions for computationally intensive tasks:
reducing lattice bases; factoring polynomials, integers, or algebraic
ideals; computing discrete logarithms; determining group orders on
elliptic curves; and more...

LiDIA is free for non-commercial use. See the copyright notice in the
file COPYING. Contributors are welcome.

%description -l pl.UTF-8
LiDIA to biblioteka C++ do teoretycznych obliczeń numerycznych.
Udostępnia sparametryzowane oraz wyspecjalizowane klasy wraz z
zaawansowanymi metodami do obliczeń w wielu grupach, pierścieniach i
przestrzeniach, od liczb całkowitych dowolnej długości, ułamków i
przybliżeń zmiennoprzecinkowych przez wektory i macierze do
konstrukcji wysokopoziomowych, takich jak przestrzenie skończone,
kraty, przestrzenie kwadratowe i wyższego stopnia, pierścienie
wielomianów i krzywe eliptyczne. Oprócz bogatego zbioru metod do
podstawowych operacji strukturalnych, wejścia/wyjścia, arytmetycznych
i ogólnych prymitywów teoretycznonumerycznych są także funkcje do
bardziej złożonych obliczeń: redukcji baz krat; rozkładu wielomianów,
liczb całkowitych i ideałów algebraicznych; obliczania logarytmów
dyskretnych; określania porządku w grupie na krzywych eliptycznych;
itp.

LiDIA jest darmowa do użytku niekomercyjnego. Informacje o prawach
autorskich znajdują się w pliku COPYING. Wspieranie rozwoju jest mile
widziane.

%package devel
Summary:	Header files for LiDIA library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LiDIA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LiDIA library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LiDIA.

%package static
Summary:	Static LiDIA library
Summary(pl.UTF-8):	Statyczna biblioteka LiDIA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LiDIA library.

%description static -l pl.UTF-8
Statyczna biblioteka LiDIA.

%prep
%setup -q -n lidia-%{version}
%patch0 -p1

%build
%configure \
	--enable-shared
%{__make}
%{__make} examples
# "unknown language: LaTeX"
%{__make} pdf \
	LATEX2DVI='$(TEXI2DVI) -l latex'

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf lidia $RPM_BUILD_ROOT%{_includedir}/%{name}
ln -sf lidia $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libLiDIA.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libLiDIA.so.5
%{_datadir}/lidia
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc doc/LiDIA.pdf
%attr(755,root,root) %{_libdir}/libLiDIA.so
%{_libdir}/libLiDIA.la
%{_includedir}/lidia
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libLiDIA.a
