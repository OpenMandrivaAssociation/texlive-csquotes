%global tl_name csquotes
%global tl_revision 79060

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.2p
Release:	%{tl_revision}.1
Summary:	Context sensitive quotation facilities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/csquotes
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(etoolbox)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides advanced facilities for inline and display
quotations. It is designed for a wide range of tasks ranging from the
most simple applications to the more complex demands of formal
quotations. The facilities include commands, environments, and user-
definable 'smart quotes' which dynamically adjust to their context.
Quotation marks are switched automatically if quotations are nested and
they can be adjusted to the current language if the babel package is
available. There are additional facilities designed to cope with the
more specific demands of academic writing, especially in the humanities
and the social sciences. All quote styles as well as the optional active
quotes are freely configurable. The package is dependent on e-TeX, and
requires the author's etoolbox package.

