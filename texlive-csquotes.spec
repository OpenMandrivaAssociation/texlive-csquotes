Name:		texlive-csquotes
Version:	5.2d
Release:	2
Summary:	Context sensitive quotation facilities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/csquotes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides advanced facilities for inline and
display quotations. It is designed for a wide range of tasks
ranging from the most simple applications to the more complex
demands of formal quotations. The facilities include commands,
environments, and user-definable 'smart quotes' which
dynamically adjust to their context. Quotation marks are
switched automatically if quotations are nested and they can be
adjusted to the current language if the babel package is
available. There are additional facilities designed to cope
with the more specific demands of academic writing, especially
in the humanities and the social sciences. All quote styles as
well as the optional active quotes are freely configurable. The
package is dependent on e-TeX, and requires the author's
etoolbox package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/csquotes
%doc %{_texmfdistdir}/doc/latex/csquotes

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
