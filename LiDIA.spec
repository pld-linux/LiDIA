Summary:	C++ library for number theoretical computations
Summary(pl.UTF-8):	Biblioteka C++ do teoretycznych obliczeń numerycznych
Name:		LiDIA
Version:	2.2.0
Release:	0.1
License:	non-commercial
Group:		Development/Libraries
Source0:	ftp://ftp.informatik.tu-darmstadt.de/pub/TI/systems/LiDIA/current/lidia-%{version}.tar.gz
# Source0-md5:	d9e012bb666e7a7ba1b45283aa3bfe03
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

%prep
%setup -q -n lidia-%{version}

%build
%configure \
	--enable-shared
%{__make}
%{__make} examples
%{__make} pdf

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf lidia $RPM_BUILD_ROOT%{_includedir}/%{name}
ln -sf lidia $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README TODO
%doc doc/LiDIA.pdf
%attr(755,root,root) %{_libdir}/lib*.so*
%{_libdir}/lib*.la
%{_includedir}/lidia
%{_includedir}/%{name}
%{_datadir}/lidia
%{_datadir}/%{name}
