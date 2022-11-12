Name:		texlive-dirtytalk
Version:	20520
Release:	1
Summary:	TeXLive dirtytalk package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
