# revision 20520
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-dirtytalk
Version:	20111103
Release:	6
Summary:	TeXLive dirtytalk package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive dirtytalk package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dirtytalk/dirtytalk.sty
%doc %{_texmfdistdir}/doc/latex/dirtytalk/README
%doc %{_texmfdistdir}/doc/latex/dirtytalk/dirtytalk.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dirtytalk/dirtytalk.dtx
%doc %{_texmfdistdir}/source/latex/dirtytalk/dirtytalk.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 751000
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718237
- texlive-dirtytalk
- texlive-dirtytalk
- texlive-dirtytalk
- texlive-dirtytalk

