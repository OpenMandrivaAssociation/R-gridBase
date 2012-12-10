%global packname  gridBase
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.4_4
Release:          1
Summary:          Integration of base and grid graphics
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-4.tar.gz
Requires:         R-graphics R-grid 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-graphics R-grid

%description
Integration of base and grid graphics

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4_4-1
+ Revision: 777728
- Import R-gridBase
- Import R-gridBase

