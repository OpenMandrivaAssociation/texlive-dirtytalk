# revision 20520
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-dirtytalk
Version:	20111103
Release:	1
Summary:	TeXLive dirtytalk package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
TeXLive dirtytalk package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dirtytalk/dirtytalk.sty
%doc %{_texmfdistdir}/doc/latex/dirtytalk/README
%doc %{_texmfdistdir}/doc/latex/dirtytalk/dirtytalk.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dirtytalk/dirtytalk.dtx
%doc %{_texmfdistdir}/source/latex/dirtytalk/dirtytalk.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
