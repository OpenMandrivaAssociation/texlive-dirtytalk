%global tl_name dirtytalk
%global tl_revision 20520

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A package to typeset quotations easier
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dirtytalk
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dirtytalk.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a macro to typeset quotations, using the command
\say{stuff}. The quotation mark glyphs are inserted by the macro; nested
quotations are detected.

