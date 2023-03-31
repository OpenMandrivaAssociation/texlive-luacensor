Name:		texlive-luacensor
Version:	62167
Release:	2
Summary:	Securely redact sensitive information using Lua
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luacensor
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luacensor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luacensor.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides simple tools for creating redacted Its
tools are useful for lawyers, workers in sensitive industries,
and others who need to easily produce both unrestricted
versions of documents (for limited, secure release) and
restricted versions of documents (for general release)
Redaction is done both by hiding all characters and by slightly
varying the length of strings to prevent jigsaw identification.
It also is friendly to screen readers by adding alt-text
indicating redacted content.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/luacensor
%doc %{_texmfdistdir}/doc/lualatex/luacensor

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
