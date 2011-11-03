# revision 24393
# category Package
# catalog-ctan /macros/latex/contrib/csquotes
# catalog-date 2011-10-24 17:03:17 +0200
# catalog-license lppl
# catalog-version 5.1d
Name:		texlive-csquotes
Version:	5.1d
Release:	1
Summary:	Context sensitive quotation facilities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/csquotes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csquotes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%{_texmfdistdir}/tex/latex/csquotes/csq-compat.def
%{_texmfdistdir}/tex/latex/csquotes/csquotes.cfg
%{_texmfdistdir}/tex/latex/csquotes/csquotes.def
%{_texmfdistdir}/tex/latex/csquotes/csquotes.sty
%doc %{_texmfdistdir}/doc/latex/csquotes/README
%doc %{_texmfdistdir}/doc/latex/csquotes/RELEASE
%doc %{_texmfdistdir}/doc/latex/csquotes/csquotes.pdf
%doc %{_texmfdistdir}/doc/latex/csquotes/csquotes.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
